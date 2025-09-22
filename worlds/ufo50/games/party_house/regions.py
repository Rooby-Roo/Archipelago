from typing import Dict, TYPE_CHECKING
from BaseClasses import Region

from .locations import create_locations

if TYPE_CHECKING:
    from ... import UFO50World

def create_regions_and_rules(world: "UFO50World") -> Dict[str, Region]:
    party_house_menu = Region("Party House - Menu", world.player, world.multiworld)
    create_locations(world, {"Party House - Menu": party_house_menu})
    return {"Party House - Menu": party_house_menu}