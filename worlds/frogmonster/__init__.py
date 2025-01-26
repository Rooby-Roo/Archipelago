from worlds.AutoWorld import WebWorld, World
from .options import FrogmonsterOptions
from .items import item_id_table
from .locations import location_id_table

class FrogmonsterWorld(World):
    """Frogmonster."""

    game = "Frogmonster"
    options: FrogmonsterOptions
    options_dataclass: FrogmonsterOptions  # one of these days someone will teach me the difference between options and options_dataclass
    location_name_to_id = location_id_table
    item_name_to_id = item_id_table