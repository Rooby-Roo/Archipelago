from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification
from __init__ import base_id

class FrogmonsterItem(Item):
    game = "Frogmonster"

class FrogmonsterItemData(NamedTuple):
    id: int = None
    type: ItemClassification = ItemClassification.filler
    category: (str) = None
    count: int = 1

item_data_table = Dict[str, FrogmonsterItemData] = {
    "Victory": FrogmonsterItemData(
        type=ItemClassification.progression,
        category=("Event")
    ),
    "Dash": FrogmonsterItemData(
        id=base_id + 0,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    "Sticky Hands": FrogmonsterItemData(
        id=base_id + 1,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    "Tongue Swing": FrogmonsterItemData(
        id=base_id + 2,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    "Runi Key": FrogmonsterItemData(
        id=base_id + 3,
        type=ItemClassification.progression,
        category=()
    ),
    "Glowbug": FrogmonsterItemData(
        id=base_id + 4,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Frog": FrogmonsterItemData(
        id=base_id + 5,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Fly": FrogmonsterItemData(
        id=base_id + 6,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Dragonfly": FrogmonsterItemData(
        id=base_id + 7,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Eel": FrogmonsterItemData(
        id=base_id + 8,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bass": FrogmonsterItemData(
        id=base_id + 9,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Blue Snack": FrogmonsterItemData(
        id=base_id + 10,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Purple Snack": FrogmonsterItemData(
        id=base_id + 11,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Magnet Roach": FrogmonsterItemData(
        id=base_id + 12,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mushroll": FrogmonsterItemData(
        id=base_id + 13,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mushfrog": FrogmonsterItemData(
        id=base_id + 14,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Beet": FrogmonsterItemData(
        id=base_id + 15,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Skater": FrogmonsterItemData(
        id=base_id + 16,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Soulfrog": FrogmonsterItemData(
        id=base_id + 17,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "River Fish": FrogmonsterItemData(
        id=base_id + 18,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bird": FrogmonsterItemData(
        id=base_id + 19,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Leafbug": FrogmonsterItemData(
        id=base_id + 20,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Wormy": FrogmonsterItemData(
        id=base_id + 21,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Minnow": FrogmonsterItemData(
        id=base_id + 22,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Turtle": FrogmonsterItemData(
        id=base_id + 23,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Blue Jelly": FrogmonsterItemData(
        id=base_id + 24,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Roof Snail": FrogmonsterItemData(
        id=base_id + 25,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Crab": FrogmonsterItemData(
        id=base_id + 26,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bridge Frog": FrogmonsterItemData(
        id=base_id + 27,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Cricket": FrogmonsterItemData(
        id=base_id + 28,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Spider": FrogmonsterItemData(
        id=base_id + 29,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Moth": FrogmonsterItemData(
        id=base_id + 30,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Ammofly": FrogmonsterItemData(
        id=base_id + 31,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Pecker": FrogmonsterItemData(
        id=base_id + 32,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Soul Fish": FrogmonsterItemData(
        id=base_id + 33,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Fog Fly": FrogmonsterItemData(
        id=base_id + 34,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Cicada": FrogmonsterItemData(
        id=base_id + 35,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mantis": FrogmonsterItemData(
        id=base_id + 36,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Jungle Snack": FrogmonsterItemData(
        id=base_id + 37,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Gecko": FrogmonsterItemData(
        id=base_id + 38,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bee": FrogmonsterItemData(
        id=base_id + 39,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mushroom": FrogmonsterItemData(
        id=base_id + 40,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Tang": FrogmonsterItemData(
        id=base_id + 41,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Axolotyl": FrogmonsterItemData(
        id=base_id + 42,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mite": FrogmonsterItemData(
        id=base_id + 43,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Health 1": FrogmonsterItemData(
        id=base_id + 44,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 2": FrogmonsterItemData(
        id=base_id + 45,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 3": FrogmonsterItemData(
        id=base_id + 46,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 4": FrogmonsterItemData(
        id=base_id + 47,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 5": FrogmonsterItemData(
        id=base_id + 48,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 6": FrogmonsterItemData(
        id=base_id + 49,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Mana 1": FrogmonsterItemData(
        id=base_id + 50,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 2": FrogmonsterItemData(
        id=base_id + 51,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 3": FrogmonsterItemData(
        id=base_id + 52,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 4": FrogmonsterItemData(
        id=base_id + 53,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 5": FrogmonsterItemData(
        id=base_id + 54,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 6": FrogmonsterItemData(
        id=base_id + 55,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Reeder": FrogmonsterItemData(
        id=base_id + 56,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Machine Gun": FrogmonsterItemData(
        id=base_id + 57,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Weepwood Bow": FrogmonsterItemData(
        id=base_id + 58,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Finisher": FrogmonsterItemData(
        id=base_id + 59,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Fire Fruit Juicer": FrogmonsterItemData(
        id=base_id + 60,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Gatling Gun": FrogmonsterItemData(
        id=base_id + 61,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Wooden Cannon": FrogmonsterItemData(
        id=base_id + 62,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Fireball": FrogmonsterItemData(
        id=base_id + 63,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Mushbomb": FrogmonsterItemData(
        id=base_id + 64,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Sharap Shot": FrogmonsterItemData(
        id=base_id + 65,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Bean": FrogmonsterItemData(
        id=base_id + 66,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Zap": FrogmonsterItemData(
        id=base_id + 67,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Slam": FrogmonsterItemData(
        id=base_id + 68,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Hive": FrogmonsterItemData(
        id=base_id + 69,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Puff": FrogmonsterItemData(
        id=base_id + 70,
        type=ItemClassification.useful,
        category=("Spell")
    ),
}

item_id_table = {name: data.id for name, data in item_data_table.items() if data.id is not None}