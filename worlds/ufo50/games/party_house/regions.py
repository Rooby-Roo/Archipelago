from typing import Dict, TYPE_CHECKING
from BaseClasses import Region

from .locations import create_locations

if TYPE_CHECKING:
    from ... import UFO50World

def create_regions_and_rules(world: "UFO50World") -> Dict[str, Region]:
    party_house_menu = Region("Party House - The Party House", world.player, world.multiworld)
    party_house_regions = {"The Party House": party_house_menu}
    create_locations(world, party_house_regions)
    return party_house_regions