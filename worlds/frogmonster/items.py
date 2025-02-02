from typing import NamedTuple, Dict

from BaseClasses import Item, ItemClassification
from __init__ import base_id
from .names.item_names import item_names as i

class FrogmonsterItem(Item):
    game = "Frogmonster"

class FrogmonsterItemData(NamedTuple):
    id: int = None
    type: ItemClassification = ItemClassification.filler
    category: (str) = None
    count: int = 1

item_data_table = Dict[str, FrogmonsterItemData] = {
    i.victory: FrogmonsterItemData(
        type=ItemClassification.progression,
        category=("Event")
    ),
    i.dash: FrogmonsterItemData(
        id=base_id + 0,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    i.sticky_hands: FrogmonsterItemData(
        id=base_id + 1,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    i.tongue_swing: FrogmonsterItemData(
        id=base_id + 2,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    i.runi_key: FrogmonsterItemData(
        id=base_id + 3,
        type=ItemClassification.progression,
        category=()
    ),
    i.glowbug: FrogmonsterItemData(
        id=base_id + 4,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.frog: FrogmonsterItemData(
        id=base_id + 5,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.fly: FrogmonsterItemData(
        id=base_id + 6,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.dragonfly: FrogmonsterItemData(
        id=base_id + 7,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.eel: FrogmonsterItemData(
        id=base_id + 8,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bass: FrogmonsterItemData(
        id=base_id + 9,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.blue_snack: FrogmonsterItemData(
        id=base_id + 10,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.purple_snack: FrogmonsterItemData(
        id=base_id + 11,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.magnet_roach: FrogmonsterItemData(
        id=base_id + 12,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mushroll: FrogmonsterItemData(
        id=base_id + 13,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mushfrog: FrogmonsterItemData(
        id=base_id + 14,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.beet: FrogmonsterItemData(
        id=base_id + 15,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.skater: FrogmonsterItemData(
        id=base_id + 16,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.soul_frog: FrogmonsterItemData(
        id=base_id + 17,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.river_fish: FrogmonsterItemData(
        id=base_id + 18,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bird: FrogmonsterItemData(
        id=base_id + 19,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.leafbug: FrogmonsterItemData(
        id=base_id + 20,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.wormy: FrogmonsterItemData(
        id=base_id + 21,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.minnow: FrogmonsterItemData(
        id=base_id + 22,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.turtle: FrogmonsterItemData(
        id=base_id + 23,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.blue_jelly: FrogmonsterItemData(
        id=base_id + 24,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.roof_snail: FrogmonsterItemData(
        id=base_id + 25,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.crab: FrogmonsterItemData(
        id=base_id + 26,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bridge_frog: FrogmonsterItemData(
        id=base_id + 27,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.cricket: FrogmonsterItemData(
        id=base_id + 28,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.spider: FrogmonsterItemData(
        id=base_id + 29,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.moth: FrogmonsterItemData(
        id=base_id + 30,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.ammofly: FrogmonsterItemData(
        id=base_id + 31,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.pecker: FrogmonsterItemData(
        id=base_id + 32,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.soul_fish: FrogmonsterItemData(
        id=base_id + 33,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.fog_fly: FrogmonsterItemData(
        id=base_id + 34,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.cicada: FrogmonsterItemData(
        id=base_id + 35,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mantis: FrogmonsterItemData(
        id=base_id + 36,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.jungle_snack: FrogmonsterItemData(
        id=base_id + 37,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.gecko: FrogmonsterItemData(
        id=base_id + 38,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bee: FrogmonsterItemData(
        id=base_id + 39,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mushroom: FrogmonsterItemData(
        id=base_id + 40,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.tang: FrogmonsterItemData(
        id=base_id + 41,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.axolotyl: FrogmonsterItemData(
        id=base_id + 42,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mite: FrogmonsterItemData(
        id=base_id + 43,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.health_1: FrogmonsterItemData(
        id=base_id + 44,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_2: FrogmonsterItemData(
        id=base_id + 45,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_3: FrogmonsterItemData(
        id=base_id + 46,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_4: FrogmonsterItemData(
        id=base_id + 47,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_5: FrogmonsterItemData(
        id=base_id + 48,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_6: FrogmonsterItemData(
        id=base_id + 49,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.mana_1: FrogmonsterItemData(
        id=base_id + 50,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_2: FrogmonsterItemData(
        id=base_id + 51,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_3: FrogmonsterItemData(
        id=base_id + 52,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_4: FrogmonsterItemData(
        id=base_id + 53,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_5: FrogmonsterItemData(
        id=base_id + 54,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_6: FrogmonsterItemData(
        id=base_id + 55,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.reeder: FrogmonsterItemData(
        id=base_id + 56,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.machine_gun: FrogmonsterItemData(
        id=base_id + 57,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.weepwood_bow: FrogmonsterItemData(
        id=base_id + 58,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.finisher: FrogmonsterItemData(
        id=base_id + 59,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.fire_fruit_juicer: FrogmonsterItemData(
        id=base_id + 60,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.gatling_gun: FrogmonsterItemData(
        id=base_id + 61,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.wooden_cannon: FrogmonsterItemData(
        id=base_id + 62,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.fireball: FrogmonsterItemData(
        id=base_id + 63,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.mushbomb: FrogmonsterItemData(
        id=base_id + 64,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.sharap_shot: FrogmonsterItemData(
        id=base_id + 65,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.bean: FrogmonsterItemData(
        id=base_id + 66,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.zap: FrogmonsterItemData(
        id=base_id + 67,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.slam: FrogmonsterItemData(
        id=base_id + 68,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.hive: FrogmonsterItemData(
        id=base_id + 69,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.puff: FrogmonsterItemData(
        id=base_id + 70,
        type=ItemClassification.useful,
        category=("Spell")
    ),
}

item_id_table = {name: data.id for name, data in item_data_table.items() if data.id is not None}