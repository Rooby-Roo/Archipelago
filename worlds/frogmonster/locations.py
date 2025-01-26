from typing import NamedTuple, Dict

from .items import BASE_ID
from BaseClasses import Location

class FrogmonsterLocation(Location):
    game = "FrogMonster"

class FrogmonsterLocationData(NamedTuple):
    region: str
    id: int = None

location_data_table: Dict[str, FrogmonsterLocationData] = {
    "Goal": FrogmonsterLocationData(
        region="Anywhere",
    ),
    "Dash": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 0
    ),
    "Sticky Hands": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 1
    ),
    "Tongue Swing": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 2
    ),
    "Runi Key": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 3
    ),
    "Glowbug": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 4
    ),
    "Frog": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 5
    ),
    "Fly": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 6
    ),
    "Dragonfly": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 7
    ),
    "Eel": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 8
    ),
    "Bass": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 9
    ),
    "Blue Snack": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 10
    ),
    "Purple Snack": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 11
    ),
    "Magnet Roach": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 12
    ),
    "Mushroll": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 13
    ),
    "Mushfrog": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 14
    ),
    "Beet": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 15
    ),
    "Skater": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 16
    ),
    "Soul Frog": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 17
    ),
    "River Fish": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 18
    ),
    "Bird": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 19
    ),
    "Leafbug": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 20
    ),
    "Wormy": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 21
    ),
    "Minnow": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 22
    ),
    "Turtle": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 23
    ),
    "Blue Jelly": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 24
    ),
    "Roof Snail": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 25
    ),
    "Crab": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 26
    ),
    "Bridge Frog": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 27
    ),
    "Cricket": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 28
    ),
    "Spider": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 29
    ),
    "Moth": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 30
    ),
    "Ammofly": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 31
    ),
    "Pecker": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 32
    ),
    "Soul Fish": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 33
    ),
    "Fog Fly": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 34
    ),
    "Cicada": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 35
    ),
    "Mantis": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 36
    ),
    "Jungle Snack": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 37
    ),
    "Gecko": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 38
    ),
    "Bee": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 39
    ),
    "Mushroom": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 40
    ),
    "Tang": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 41
    ),
    "Axolotyl": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 42
    ),
    "Mite": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 43
    ),
    "Health 1": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 44
    ),
    "Health 2": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 45
    ),
    "Health 3": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 46
    ),
    "Health 4": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 47
    ),
    "Health 5": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 48
    ),
    "Health 6": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 49
    ),
    "Mana 1": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 50
    ),
    "Mana 2": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 51
    ),
    "Mana 3": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 52
    ),
    "Mana 4": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 53
    ),
    "Mana 5": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 54
    ),
    "Mana 6": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 55
    ),
    "Reeder": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 56
    ),
    "Machine Gun": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 57
    ),
    "Weepwood Bow": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 58
    ),
    "Finisher": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 59
    ),
    "Fire Fruit Juicer": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 60
    ),
    "Gatling Gun": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 61
    ),
    "Wooden Cannon": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 62
    ),
    "Fireball": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 63
    ),
    "Mushbomb": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 64
    ),
    "Sharap Shot": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 65
    ),
    "Beanshot": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 66
    ),
    "Zap": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 67
    ),
    "Slam": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 68
    ),
    "Hive": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 69
    ),
    "Puff": FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 70
    ),
}

location_id_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}