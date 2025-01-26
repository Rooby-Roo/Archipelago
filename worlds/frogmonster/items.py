from typing import NamedTuple, Dict
from BaseClasses import Item, ItemClassification

BASE_ID = 0  # Starting ID for both Frogmonster items and locations

class FrogmonsterItem(Item):
    game = "Frogmonster"

class FrogmonsterItemData(NamedTuple):
    id: int = None
    type: ItemClassification = ItemClassification.filler
    category: (str) = None
    count: int = 1

item_data_table = Dict[str, FrogmonsterItemData] = {
    "Dash": FrogmonsterItemData(
        id=BASE_ID + 0,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    "Sticky Hands": FrogmonsterItemData(
        id=BASE_ID + 1,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    "Tongue Swing": FrogmonsterItemData(
        id=BASE_ID + 2,
        type=ItemClassification.progression,
        category=("Movement")
    ),
    "Runi Key": FrogmonsterItemData(
        id=BASE_ID + 3,
        type=ItemClassification.progression,
        category=()
    ),
    "Glowbug": FrogmonsterItemData(
        id=BASE_ID + 4,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Frog": FrogmonsterItemData(
        id=BASE_ID + 5,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Fly": FrogmonsterItemData(
        id=BASE_ID + 6,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Dragonfly": FrogmonsterItemData(
        id=BASE_ID + 7,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Eel": FrogmonsterItemData(
        id=BASE_ID + 8,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bass": FrogmonsterItemData(
        id=BASE_ID + 9,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Blue Snack": FrogmonsterItemData(
        id=BASE_ID + 10,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Purple Snack": FrogmonsterItemData(
        id=BASE_ID + 11,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Magnet Roach": FrogmonsterItemData(
        id=BASE_ID + 12,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mushroll": FrogmonsterItemData(
        id=BASE_ID + 13,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mushfrog": FrogmonsterItemData(
        id=BASE_ID + 14,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Beet": FrogmonsterItemData(
        id=BASE_ID + 15,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Skater": FrogmonsterItemData(
        id=BASE_ID + 16,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Soulfrog": FrogmonsterItemData(
        id=BASE_ID + 17,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "River Fish": FrogmonsterItemData(
        id=BASE_ID + 18,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bird": FrogmonsterItemData(
        id=BASE_ID + 19,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Leafbug": FrogmonsterItemData(
        id=BASE_ID + 20,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Wormy": FrogmonsterItemData(
        id=BASE_ID + 21,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Minnow": FrogmonsterItemData(
        id=BASE_ID + 22,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Turtle": FrogmonsterItemData(
        id=BASE_ID + 23,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Blue Jelly": FrogmonsterItemData(
        id=BASE_ID + 24,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Roof Snail": FrogmonsterItemData(
        id=BASE_ID + 25,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Crab": FrogmonsterItemData(
        id=BASE_ID + 26,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bridge Frog": FrogmonsterItemData(
        id=BASE_ID + 27,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Cricket": FrogmonsterItemData(
        id=BASE_ID + 28,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Spider": FrogmonsterItemData(
        id=BASE_ID + 29,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Moth": FrogmonsterItemData(
        id=BASE_ID + 30,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Ammofly": FrogmonsterItemData(
        id=BASE_ID + 31,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Pecker": FrogmonsterItemData(
        id=BASE_ID + 32,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Soul Fish": FrogmonsterItemData(
        id=BASE_ID + 33,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Fog Fly": FrogmonsterItemData(
        id=BASE_ID + 34,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Cicada": FrogmonsterItemData(
        id=BASE_ID + 35,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mantis": FrogmonsterItemData(
        id=BASE_ID + 36,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Jungle Snack": FrogmonsterItemData(
        id=BASE_ID + 37,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Gecko": FrogmonsterItemData(
        id=BASE_ID + 38,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Bee": FrogmonsterItemData(
        id=BASE_ID + 39,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mushroom": FrogmonsterItemData(
        id=BASE_ID + 40,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Tang": FrogmonsterItemData(
        id=BASE_ID + 41,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Axolotyl": FrogmonsterItemData(
        id=BASE_ID + 42,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Mite": FrogmonsterItemData(
        id=BASE_ID + 43,
        type=ItemClassification.useful,
        category=("Bug")
    ),
    "Health 1": FrogmonsterItemData(
        id=BASE_ID + 44,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 2": FrogmonsterItemData(
        id=BASE_ID + 45,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 3": FrogmonsterItemData(
        id=BASE_ID + 46,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 4": FrogmonsterItemData(
        id=BASE_ID + 47,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 5": FrogmonsterItemData(
        id=BASE_ID + 48,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Health 6": FrogmonsterItemData(
        id=BASE_ID + 49,
        type=ItemClassification.useful,
        category=("Health")
    ),
    "Mana 1": FrogmonsterItemData(
        id=BASE_ID + 50,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 2": FrogmonsterItemData(
        id=BASE_ID + 51,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 3": FrogmonsterItemData(
        id=BASE_ID + 52,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 4": FrogmonsterItemData(
        id=BASE_ID + 53,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 5": FrogmonsterItemData(
        id=BASE_ID + 54,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Mana 6": FrogmonsterItemData(
        id=BASE_ID + 55,
        type=ItemClassification.useful,
        category=("Mana")
    ),
    "Reeder": FrogmonsterItemData(
        id=BASE_ID + 56,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Machine Gun": FrogmonsterItemData(
        id=BASE_ID + 57,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Weepwood Bow": FrogmonsterItemData(
        id=BASE_ID + 58,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Finisher": FrogmonsterItemData(
        id=BASE_ID + 59,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Fire Fruit Juicer": FrogmonsterItemData(
        id=BASE_ID + 60,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Gatling Gun": FrogmonsterItemData(
        id=BASE_ID + 61,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Wooden Cannon": FrogmonsterItemData(
        id=BASE_ID + 62,
        type=ItemClassification.progression,
        category=("Gun")
    ),
    "Fireball": FrogmonsterItemData(
        id=BASE_ID + 63,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Mushbomb": FrogmonsterItemData(
        id=BASE_ID + 64,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Sharap Shot": FrogmonsterItemData(
        id=BASE_ID + 65,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Bean": FrogmonsterItemData(
        id=BASE_ID + 66,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Zap": FrogmonsterItemData(
        id=BASE_ID + 67,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Slam": FrogmonsterItemData(
        id=BASE_ID + 68,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Hive": FrogmonsterItemData(
        id=BASE_ID + 69,
        type=ItemClassification.useful,
        category=("Spell")
    ),
    "Puff": FrogmonsterItemData(
        id=BASE_ID + 70,
        type=ItemClassification.useful,
        category=("Spell")
    ),
}

item_id_table = {name: data.id for name, data in item_data_table.items() if data.id is not None}