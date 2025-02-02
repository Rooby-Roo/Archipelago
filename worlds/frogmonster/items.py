from typing import NamedTuple, Dict

from BaseClasses import Item, ItemClassification
from .names import item_names as i

BASE_ID = 0  # Starting ID for both Frogmonster items and locations, moved out of __init__ to avoid circular imports

class FrogmonsterItem(Item):
    game = "Frogmonster"

class FrogmonsterItemData(NamedTuple):
    id: int = None
    type: ItemClassification = ItemClassification.filler
    category: (str) = None
    count: int = 1

item_data_table: Dict[str, FrogmonsterItemData] = {

    # Items
    i.dash: FrogmonsterItemData(
        id=BASE_ID + 0,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    i.sticky_hands: FrogmonsterItemData(
        id=BASE_ID + 1,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    i.tongue_swing: FrogmonsterItemData(
        id=BASE_ID + 2,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    i.runi_key: FrogmonsterItemData(
        id=BASE_ID + 3,
        type=ItemClassification.progression,
        category=()
    ),
    i.glowbug: FrogmonsterItemData(
        id=BASE_ID + 4,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.frog: FrogmonsterItemData(
        id=BASE_ID + 5,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.fly: FrogmonsterItemData(
        id=BASE_ID + 6,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.dragonfly: FrogmonsterItemData(
        id=BASE_ID + 7,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.eel: FrogmonsterItemData(
        id=BASE_ID + 8,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bass: FrogmonsterItemData(
        id=BASE_ID + 9,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.blue_snack: FrogmonsterItemData(
        id=BASE_ID + 10,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.purple_snack: FrogmonsterItemData(
        id=BASE_ID + 11,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.magnet_roach: FrogmonsterItemData(
        id=BASE_ID + 12,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mushroll: FrogmonsterItemData(
        id=BASE_ID + 13,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mushfrog: FrogmonsterItemData(
        id=BASE_ID + 14,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.beet: FrogmonsterItemData(
        id=BASE_ID + 15,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.skater: FrogmonsterItemData(
        id=BASE_ID + 16,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.soul_frog: FrogmonsterItemData(
        id=BASE_ID + 17,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.river_fish: FrogmonsterItemData(
        id=BASE_ID + 18,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bird: FrogmonsterItemData(
        id=BASE_ID + 19,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.leafbug: FrogmonsterItemData(
        id=BASE_ID + 20,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.wormy: FrogmonsterItemData(
        id=BASE_ID + 21,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.minnow: FrogmonsterItemData(
        id=BASE_ID + 22,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.turtle: FrogmonsterItemData(
        id=BASE_ID + 23,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.blue_jelly: FrogmonsterItemData(
        id=BASE_ID + 24,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.roof_snail: FrogmonsterItemData(
        id=BASE_ID + 25,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.crab: FrogmonsterItemData(
        id=BASE_ID + 26,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bridge_frog: FrogmonsterItemData(
        id=BASE_ID + 27,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.cricket: FrogmonsterItemData(
        id=BASE_ID + 28,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.spider: FrogmonsterItemData(
        id=BASE_ID + 29,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.moth: FrogmonsterItemData(
        id=BASE_ID + 30,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.ammofly: FrogmonsterItemData(
        id=BASE_ID + 31,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.pecker: FrogmonsterItemData(
        id=BASE_ID + 32,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.soul_fish: FrogmonsterItemData(
        id=BASE_ID + 33,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.fog_fly: FrogmonsterItemData(
        id=BASE_ID + 34,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.cicada: FrogmonsterItemData(
        id=BASE_ID + 35,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mantis: FrogmonsterItemData(
        id=BASE_ID + 36,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.jungle_snack: FrogmonsterItemData(
        id=BASE_ID + 37,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.gecko: FrogmonsterItemData(
        id=BASE_ID + 38,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.bee: FrogmonsterItemData(
        id=BASE_ID + 39,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mushroom: FrogmonsterItemData(
        id=BASE_ID + 40,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.tang: FrogmonsterItemData(
        id=BASE_ID + 41,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.axolotyl: FrogmonsterItemData(
        id=BASE_ID + 42,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.mite: FrogmonsterItemData(
        id=BASE_ID + 43,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    i.health_1: FrogmonsterItemData(
        id=BASE_ID + 44,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_2: FrogmonsterItemData(
        id=BASE_ID + 45,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_3: FrogmonsterItemData(
        id=BASE_ID + 46,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_4: FrogmonsterItemData(
        id=BASE_ID + 47,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_5: FrogmonsterItemData(
        id=BASE_ID + 48,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.health_6: FrogmonsterItemData(
        id=BASE_ID + 49,
        type=ItemClassification.useful,
        category=("Health")
    ),
    i.mana_1: FrogmonsterItemData(
        id=BASE_ID + 50,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_2: FrogmonsterItemData(
        id=BASE_ID + 51,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_3: FrogmonsterItemData(
        id=BASE_ID + 52,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_4: FrogmonsterItemData(
        id=BASE_ID + 53,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_5: FrogmonsterItemData(
        id=BASE_ID + 54,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.mana_6: FrogmonsterItemData(
        id=BASE_ID + 55,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    i.reeder: FrogmonsterItemData(
        id=BASE_ID + 56,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.machine_gun: FrogmonsterItemData(
        id=BASE_ID + 57,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.weepwood_bow: FrogmonsterItemData(
        id=BASE_ID + 58,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.finisher: FrogmonsterItemData(
        id=BASE_ID + 59,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.fire_fruit_juicer: FrogmonsterItemData(
        id=BASE_ID + 60,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.gatling_gun: FrogmonsterItemData(
        id=BASE_ID + 61,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.wooden_cannon: FrogmonsterItemData(
        id=BASE_ID + 62,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    i.fireball: FrogmonsterItemData(
        id=BASE_ID + 63,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.mushbomb: FrogmonsterItemData(
        id=BASE_ID + 64,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.sharap_shot: FrogmonsterItemData(
        id=BASE_ID + 65,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.beans: FrogmonsterItemData(
        id=BASE_ID + 66,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.zap: FrogmonsterItemData(
        id=BASE_ID + 67,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.slam: FrogmonsterItemData(
        id=BASE_ID + 68,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.hive: FrogmonsterItemData(
        id=BASE_ID + 69,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.puff: FrogmonsterItemData(
        id=BASE_ID + 70,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    i.coins: FrogmonsterItemData(
        id=BASE_ID + 71,
        type=ItemClassification.filler,
    ),
    
    # Events
    i.victory: FrogmonsterItemData(
        type=ItemClassification.progression,
        category=("Event")
    ),
}

item_id_table = {name: data.id for name, data in item_data_table.items() if data.id is not None}