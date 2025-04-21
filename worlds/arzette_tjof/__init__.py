from worlds.AutoWorld import WebWorld, World
from BaseClasses import Region, Location, Item, Tutorial, ItemClassification, MultiWorld

from .locations import all_locations
from .options import ArzetteOptions


class ArzetteWebWorld(WebWorld):
    pass  # todo

class ArzetteItem(Item):
    game: str = "Arzette: The Jewel of Faramore"

class ArzetteLocation(Location):
    game: str = "Arzette: The Jewel of Faramore"

class ArzetteWorld(World):
    game: str = "Arzette: The Jewel of Faramore"
    web = ArzetteWebWorld()
    options: ArzetteOptions
    options_dataclass = ArzetteOptions

    item_name_groups = {
        "magic": {"Sword Wave", "Smart Gun"},
#        "bombs": {"Bombs", "Bomb Gauntlet"},  # This doesn't actually work since "Bombs" is in Bombs
        "blue": {"Blue Magic", "Purple Magic"},
    }
    location_name_groups = {
        "candles": {location for location in all_locations if "Candle" in location.split()},
        "coins": {location for location in all_locations if "Coin" in location.split()},
        "jewels": {location for location in all_locations if "Jewel" in location.split()},
        "plants": {location for location in all_locations if "Plant" in location.split()},
        "races": {location for location in all_locations if "Race" in location.split()},
        "rocks": {location for location in all_locations if "Rock" in location.split()},
        "bags": {location for location in all_locations if "Bag" in location.split()},
    }

#    def create_item(self, name: str) -> ArzetteItem:
#        return ArzetteItem(name, self)