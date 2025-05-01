"""Holds additional rules for alternative settings, to be iterated over."""
from typing import Callable, TYPE_CHECKING
from functools import partial

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule
from .combat import Difficulty
from .rules_helpers import can_fight
from .names import item_names as i
from .names import location_names as l
from .names import region_names as r
from .names import combat_names as c

if TYPE_CHECKING:
    from __init__ import FrogmonsterWorld

def parse_access_rule_group(world: FrogmonsterWorld, group: dict[str, dict[str, tuple[str, Callable[[int, Difficulty, CollectionState], bool]]]]) -> None:

    for location_data in group["locations"].items():
        location = world.multiworld.get_location(location_data[0], world.player)
        if location_data[0] == "replace":
            location.access_rule = partial(location_data[1][1], world.player, world.difficulty)
        elif location_data[0] in ["or", "and"]:
            add_rule(location, partial(location_data[1][1], world.player, world.difficulty), combine=location_data[0])
        else:
            raise ValueError(f"Invalid access rule type {location_data[0]} for location {location_data[1][0]}.")
        
    for entrance_data in group["entrances"].items():
        entrance = world.multiworld.get_entrance(entrance_data[0], world.player)
        if entrance_data[0] == "replace":
            entrance.access_rule = partial(entrance_data[1][1], world.player, world.difficulty)
        elif entrance_data[0] in ["or", "and"]:
            add_rule(entrance, partial(entrance_data[1][1], world.player, world.difficulty), combine=entrance_data[0])
        else:
            raise ValueError(f"Invalid access rule type {entrance_data[0]} for entrance {entrance_data[1][0]}.")  

parkour_rules = {
    "locations": {
        l.sparkling_gem_1: ("replace", lambda player, dif, state: True),  # There's a mushroom in the poison fields you can stand on just off to the side of the chest.
        l.metal_ore_10: ("or", lambda player, dif, state: state.has_all([i.sticky_hands, i.dash, i.cricket], player)),  # A well-timed wavedash and cricket can bypass the tongue swing.
        l.sparkling_gem_2: ("replace", lambda player, dif, state: True),  # There's a part of the tree that you can stand on. Jump to it from Trench's house.
    },
    "entrances": {
        f"{r.hive} -> {r.treetops}": ("or", lambda player, dif, state: can_fight(c.hive_general, player, dif, state) and state.has(i.dash, player))  # Climb on top of the hive to get height.
    }
} 