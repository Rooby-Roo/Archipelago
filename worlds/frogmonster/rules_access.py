"""Holds additional rules for alternative settings, to be iterated over."""

from .rules_helpers import can_fight
from .names import item_names as i
from .names import location_names as l
from .names import region_names as r
from .names import combat_names as c

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