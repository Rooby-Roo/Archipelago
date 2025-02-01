from BaseClasses import Region
from worlds.AutoWorld import WebWorld, World
from .options import FrogmonsterOptions
from .items import item_id_table, item_data_table, FrogmonsterItem
from .locations import location_id_table, location_data_table, FrogmonsterLocation
from .regions import region_data_table

class FrogmonsterWorld(World):
    """Frogmonster."""

    game = "Frogmonster"
    options: FrogmonsterOptions
    options_dataclass: FrogmonsterOptions  # one of these days someone will teach me the difference between options and options_dataclass
    location_name_to_id = location_id_table
    item_name_to_id = item_id_table
    origin_region_name = "Anywhere"

    def create_item(self, name: str) -> FrogmonsterItem:
        return FrogmonsterItem(name, item_data_table[name].type, item_data_table[name].id, self.player)
    
    def create_items(self) -> None:
        item_pool = []
        for name, item in item_data_table.items():
            if item.id:
                for i in range(item_data_table[name].count):
                    item_pool.append(self.create_item(name))
        
        self.multiworld.itempool += item_pool

    def create_regions(self) -> None:
        for region in region_data_table.keys():
            # Create regions.
            region = Region(region, self.player, self.multiworld)
            self.multiworld.regions.append(region)
            
            # Create locations, add locations to regions.
            current_region_locations = {key:val for key,val in location_data_table.items() if val.region == region}
            region.add_locations(current_region_locations, FrogmonsterLocation)
