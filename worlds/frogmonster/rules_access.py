"""Holds additional rules for alternative settings, to be iterated over."""

from .rules_helpers import can_fight
from .names import item_names as i
from .names import location_names as l
from .names import region_names as r
from .names import combat_names as c

parkour_rules = {
    "locations": {
        l.sparkling_gem_1: ("replace", lambda player, dif, state: True),
        l.metal_ore_10: ("or", lambda player, dif, state: state.has_all([i.sticky_hands, i.dash, i.cricket], player))
    },
    "entrances": {
        f"{r.hive} -> {r.treetops}": ("replace", lambda player, dif, state: can_fight(c.hive_general, player, dif, state) and state.has(i.dash, player))
    }
} 