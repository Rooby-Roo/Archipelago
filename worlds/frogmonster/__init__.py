from typing import Any, TextIO

from BaseClasses import Region, MultiWorld
from worlds.AutoWorld import World
from .options import FrogmonsterOptions
from .items import item_id_table, item_data_table, FrogmonsterItem
from .locations import location_id_table, location_data_table, FrogmonsterLocation
from .regions import region_data_table
from .names import item_names as i
from .names import location_names as l
from .data import every_bug_without_mushroom, every_bug

class FrogmonsterWorld(World):
    """Frogmonster."""

    game = "Frogmonster"
    options: FrogmonsterOptions
    options_dataclass = FrogmonsterOptions
    location_name_to_id = location_id_table
    item_name_to_id = item_id_table
    origin_region_name = "Anywhere"

    shuffled_bugs: dict[int, int] = {}  # should these be in an __init__? Instinct says yes, but other worlds don't seem to do this.

    def create_item(self, name: str) -> FrogmonsterItem:
        return FrogmonsterItem(name, item_data_table[name].type, item_data_table[name].id, self.player)
    
    def create_event(self, event: str) -> FrogmonsterItem:
        return FrogmonsterItem(event, item_data_table[event].type, None, self.player)
    
    def get_filler_item_name(self) -> str:
        return i.coins
    
    def create_items(self) -> None:
        item_pool = []
        for name, item in item_data_table.items():
            if item.id:
                for i in range(item_data_table[name].qty):
                    item_pool.append(self.create_item(name))
        
        self.multiworld.itempool += item_pool

    def generate_early(self) -> None:
        # Handling option: Shuffle Bug-Eating Effects
        bugs = list(every_bug_without_mushroom.keys())
        shuffled_effects = bugs.copy()
        if self.options.shuffle_bug_effects:
            self.random.shuffle(shuffled_effects)
        shuffled_bugs = dict(zip(bugs, shuffled_effects))
        shuffled_bugs[36] = 36  # Mushroom is not shuffled but the client still expects this, it is always 36 and must be added back in manually.
        self.shuffled_bugs = shuffled_bugs

    def create_regions(self) -> None:
        for region_name in region_data_table.keys():
            # Create regions.
            region = Region(region_name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

            # Create locations, add locations to regions.
            current_region_locations = {key:val.id for key,val in location_data_table.items() if val.region == region_name}
            region.add_locations(current_region_locations, FrogmonsterLocation)

    def set_rules(self) -> None:
        for location in location_data_table.keys():
            self.multiworld.get_location(location, self.player).access_rule = lambda state: True  # Until I can be bothered to write actual logic

        self.multiworld.get_location(l.goal, self.player).place_locked_item(self.create_event(i.victory))
        self.multiworld.completion_condition[self.player] = lambda state: state.has(i.victory, self.player)

    def fill_slot_data(self) -> dict[str, Any]:
        slot_data: dict[str, Any] = {}

        slot_data["shuffled_bug_effects"] = self.shuffled_bugs

        return slot_data
    
    def write_spoiler(self, spoiler_handle: TextIO) -> None:
        if self.options.shuffle_bug_effects:
            spoiler_handle.write(f"{self.multiworld.get_player_name(self.player)}'s Shuffled Bug Effects:\n")
            for bug, effect in self.shuffled_bugs.items():
                bug_name = every_bug[bug]
                effect_name = every_bug[effect]
                spoiler_handle.write(f"{bug_name}: {effect_name}\n")
            spoiler_handle.write("\n")
