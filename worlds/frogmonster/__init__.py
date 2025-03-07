from typing import Any, TextIO
from functools import partial

from BaseClasses import Region, LocationProgressType
from worlds.AutoWorld import World
from .options import FrogmonsterOptions
from .items import item_id_table, item_data_table, item_name_groups, FrogmonsterItem
from .locations import location_id_table, location_data_table, location_name_groups, FrogmonsterLocation
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

    # Options, to be sent to slot data.
    shuffled_bug_effects: dict[int, int]
    shop_multiplier: float

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
        self.shuffled_bug_effects = shuffled_bugs

        # Handling option: Game Difficulty
        self.difficulty = Difficulty(self.options.game_difficulty)

    def create_regions(self) -> None:
        for region_name in region_data_table.keys():
            # Create base regions.
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            # Create base locations, add locations to regions.
            current_region_locations = {key:val.id for key,val in location_data_table.items() if val.region == region_name}
            region.add_locations(current_region_locations, FrogmonsterLocation)
            # Add access connections between regions.
            
    def create_items(self) -> None:
        item_pool = []
        for name, item in item_data_table.items():
            if item.id:
                for _ in range(item_data_table[name].qty):
                    item_pool.append(self.create_item(name))
        
        self.multiworld.itempool += item_pool

    def set_rules(self) -> None:
        for location in location_data_table.items():
            current_location = self.multiworld.get_location(location[0], self.player)
            current_location.access_rule = partial(location[1].access_rule, self.player, self.difficulty)

        self.multiworld.get_location(l.goal, self.player).place_locked_item(self.create_event(i.victory))
        self.multiworld.get_location(l.workshop_access, self.player).place_locked_item(self.create_event(i.workshop_key))
        self.multiworld.completion_condition[self.player] = lambda state: True # state.has(i.victory, self.player)

        # Exclude or prioritize locations according to locations.py. This will be overridden by any YAML declarations.
        for location in location_data_table.items():
            if location[1].progress_type != LocationProgressType.DEFAULT:
                self.multiworld.get_location(location[0], self.player).progress_type = location[1].progress_type

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data: dict[str, Any] = {}

        slot_data["shuffled_bug_effects"] = self.shuffled_bug_effects
        slot_data["shop_multiplier"] = float(self.options.shop_multiplier / 100) # Convert to decimal for client

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
