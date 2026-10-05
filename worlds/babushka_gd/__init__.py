from collections.abc import Mapping
from typing import Any

from worlds.AutoWorld import World, WebWorld
from BaseClasses import Tutorial

from . import items, locations, regions, rules
from . import options as babushka_options  # rename due to a name conflict with World.options
from .options import option_groups, option_presets
from .names import ItemNames as i

class BabushkaWorld(World):
    """
    Babushka's Glitch Dungeon is a game about being a grandma who fell into an underground dungeon. Tidy things
    up with your broom by smacking them. Learn (and then forget) magic spells. Build a coven of other old ladies
    to fight god. Collect hats.
    """

    game = "Babushka's Glitch Dungeon"

    web = BabushkaWebWorld()

    options_dataclass = babushka_options.BabushkaOptions
    options: babushka_options.BabushkaOptions

    location_name_to_id = locations.LOCATION_NAME_TO_ID
    item_name_to_id = items.ITEM_NAME_TO_ID

    origin_region_name = "Overworld"

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.BabushkaItemItem:
        return items.create_item_with_class(self, name)

    def get_filler_item_name(self) -> str:
        return i.forget_trap

    # There may be data that the game client will need to modify the behavior of the game.
    # This is what slot_data exists for. Upon every client connection, the slot's slot_data is sent to the client.
    # slot_data is just a dictionary using basic types, that will be converted to json when sent to the client.
    def fill_slot_data(self) -> Mapping[str, Any]:
        # If you need access to the player's chosen options on the client side, there is a helper for that.
        return self.options.as_dict(
            "hard_mode", "hammer", "extra_starting_chest", "confetti_explosiveness", "player_sprite"
        )

class BabushkaWebWorld(WebWorld):

    game = "Babushka's Glitch Dungeon"

    # Your game pages will have a visual theme (affecting e.g. the background image).
    # You can choose between dirt, grass, grassFlowers, ice, jungle, ocean, partyTime, and stone.
    theme = "dirt"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Babushka's Glitch Dungeon for Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["RoobyRoo"],
    )

    setup_tok = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Babushka's Glitch Dungeon for Archipelago.",
        "toki pona",
        "setup_tok.md",
        "setup/tok",
        ["RoobyRoo"],
    )

    tutorials = [setup_en, setup_tok]

    # If we have option groups and/or option presets, we need to specify these here as well.
    option_groups = option_groups
    options_presets = option_presets
