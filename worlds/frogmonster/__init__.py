from typing import Any, TextIO
from functools import partial

from BaseClasses import Region, LocationProgressType
from worlds.AutoWorld import World
from Utils import visualize_regions
from .options import FrogmonsterOptions
from .items import item_id_table, item_data_table, item_name_groups, FrogmonsterItem
from .locations import location_id_table, location_data_table, location_name_groups, FrogmonsterLocation, FrogmonsterLocationData
from .regions import region_data_table
from .names import item_names as i
from .names import location_names as l
from .names import region_names as r
from .combat import Difficulty
from .bugs import every_bug

class FrogmonsterWorld(World):
    """Frogmonster."""

    game = "Frogmonster"
    options: FrogmonsterOptions
    options_dataclass = FrogmonsterOptions
    location_name_to_id = location_id_table
    item_name_to_id = item_id_table
    origin_region_name = r.anywhere
    location_name_groups = location_name_groups
    item_name_groups = item_name_groups

    shuffled_bug_effects: dict[int, int]
    starter_gun: FrogmonsterItem
    starter_spell: FrogmonsterItem

    def create_item(self, name: str) -> FrogmonsterItem:
        return FrogmonsterItem(name, item_data_table[name].type, item_data_table[name].id, self.player)
    
    def create_event(self, event: str) -> FrogmonsterItem:
        return FrogmonsterItem(event, item_data_table[event].type, None, self.player)
    
    def get_filler_item_name(self) -> str:
        return i.coins

    def generate_early(self) -> None:
        # Handling option: Shuffle Bug-Eating Effects
        bugs = [bug.bug_id for bug in every_bug if bug.name != i.mushroom]  
        shuffled_effects = bugs.copy()
        if self.options.shuffle_bug_effects:
            self.random.shuffle(shuffled_effects)
        shuffled_bugs = dict(zip(bugs, shuffled_effects))
        shuffled_bugs[36] = 36  # Mushroom is not shuffled but the client still expects this, it is always 36 and must be added back in manually.
        self.shuffled_bug_effects = shuffled_bugs  # stored as dict for local purposes, but client expects array (handled in slot data)

        # Handling option: Game Difficulty
        self.difficulty = Difficulty(self.options.game_difficulty.value)

        # Handling option: Start with Gear
        if self.options.i_hate_seedling:
            gun_list = [i.reeder, i.gatling_gun, i.machine_gun, i.finisher, i.weepwood_bow]  # no cannon/flamethrower since they're logical
            self.starter_gun = self.create_item(self.random.choice(gun_list))
            spell_list = [i.fireball, i.sharp_shot, i.beans, i.slam, i.mushbomb, i.zap, i.hive, i.puff]
            self.starter_spell = self.create_item(self.random.choice(spell_list))

    def create_regions(self) -> None:
        for region_name in region_data_table.keys():
            # Create base regions.
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            # Create base locations, add locations to regions.
            current_region_locations = {key:val.id for key,val in location_data_table.items() if val.region == region_name}
            # Handling option: Shuffle Puzzles
            if not self.options.shuffle_puzzles:
                pop_list = []
                for location in current_region_locations.keys():
                    if "Puzzle" in location:
                        pop_list.append(location)
                for location in pop_list:
                    current_region_locations.pop(location)
            region.add_locations(current_region_locations, FrogmonsterLocation)

        # Connect regions to each other.
        for region_name, data in region_data_table.items():
            main_region = self.multiworld.get_region(region_name, self.player)
            for connection in data.connects:
                exit_region = self.multiworld.get_region(connection[0], self.player)
                access_rule = partial(connection[1], self.player, self.difficulty)
                main_region.connect(connecting_region=exit_region, rule=access_rule)

        for bug in every_bug:
            # Create bug region. Bugs can be found in multiple different parts of the map and as such they get their own regions, using region connections as logical access.
            bug_region = Region(bug.name, self.player, self.multiworld)
            for connection in bug.regions:
                home_region = self.multiworld.get_region(connection[0], self.player)
                access_rule = partial(connection[1], self.player, self.difficulty)
                home_region.connect(connecting_region=bug_region, rule=access_rule)
            # Create bug location on region.
            bug_location_data = location_data_table[bug.name]
            bug_location = {bug.name: bug_location_data.id}  # add_locations expects a dict, so we convert here
            bug_region.add_locations(bug_location, FrogmonsterLocation)

        # Handling option: Open City
        if self.options.open_city:
            self.multiworld.get_region(r.lost_swamp, self.player).connect(self.multiworld.get_region(r.city, self.player), None, lambda state: True)

#        visualize_regions(self.multiworld.get_region(r.anywhere, self.player), "Regions.puml")

    def create_items(self) -> None:
        item_pool = []
        for name, item in item_data_table.items():
            if item.id:  # excludes events
                dont_create = []
                if self.options.goal == 1:
                    dont_create.append(i.eye_fragment)
                if self.options.i_hate_seedling:
                    dont_create.append(self.starter_gun.name)
                    dont_create.append(self.starter_spell.name)
                if name not in dont_create:
                    for _ in range(item_data_table[name].qty):
                        item_pool.append(self.create_item(name))

        if self.options.shuffle_puzzles:
            for _ in range(7):
                item_pool.append(self.create_item(self.get_filler_item_name()))

        self.multiworld.itempool += item_pool

    def set_rules(self) -> None:
        # Set location access requirements.
        for location in location_data_table.items():
            current_location = None
            try:
                current_location = self.multiworld.get_location(location[0], self.player)
            except KeyError:  # if the location does not exist, then it does not need access rules.
                pass
            if current_location:
                current_location.access_rule = partial(location[1].access_rule, self.player, self.difficulty)

        # Set completion condition.
        self.multiworld.completion_condition[self.player] = lambda state: state.has(i.victory, self.player)
        self.multiworld.get_location(l.goal, self.player).place_locked_item(self.create_event(i.victory))

        if self.options.goal == 1:
            self.multiworld.get_location(l.eye_fragment, self.player).place_locked_item(self.create_item(i.eye_fragment))
            self.multiworld.get_location(l.goal, self.player).access_rule = lambda state: state.can_reach(l.eye_fragment, "Location", self.player)

        # Set events.
        self.multiworld.get_location(l.workshop_access, self.player).place_locked_item(self.create_event(i.workshop_key))
        self.multiworld.get_location(l.orchus_key, self.player).place_locked_item(self.create_event(i.orchus_key))

        # Exclude or prioritize locations according to locations.py. This will be overwritten by any YAML declarations.
        for location in location_data_table.items():
            if location[1].progress_type != LocationProgressType.DEFAULT:
                self.multiworld.get_location(location[0], self.player).progress_type = location[1].progress_type

        # Handling Option: Deathlink. If deathlink is on, death-get bugs should be excluded.
        if self.options.death_link:
            for bug in [l.soul_fish, l.soul_frog]:
                self.multiworld.get_location(bug, self.player).access_rule = lambda state: state.can_reach(r.city, "Region", self.player)

        # Handling Option: Start with Gear
        if self.options.i_hate_seedling:
            self.multiworld.get_location(l.reeder, self.player).place_locked_item(self.starter_gun)
            self.multiworld.get_location(l.fireball, self.player).place_locked_item(self.starter_spell)

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data: dict[str, Any] = {}

        # Handling option: Shuffle Bug-Eating Effects
        bug_effect_array = []
        for i in range (1, 41):
            bug_effect_array.append(self.shuffled_bug_effects[i])
        slot_data["shuffled_bug_effects"] = bug_effect_array

        # Other Options:
        slot_data["shop_multiplier"] = self.options.shop_multiplier.value / 100 # Convert to decimal for client
        slot_data["shuffle_puzzles"] = bool(self.options.shuffle_puzzles.value)
        slot_data["open_city"] = bool(self.options.open_city.value)
        slot_data["death_link"] = bool(self.options.death_link.value)
        slot_data["goal"] = self.options.goal.value

        return slot_data
    
    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        if self.options.shuffle_bug_effects:
            spoiler_handle.write("\n")
            spoiler_handle.write(f"{self.multiworld.get_player_name(self.player)}'s Shuffled Bug Effects:\n")
            for bug, effect in self.shuffled_bug_effects.items():
                bug_name = every_bug[bug-1][0]
                effect_name = every_bug[effect-1][0]
                spoiler_handle.write(f"{bug_name}: {effect_name}\n")
            spoiler_handle.write("\n")
