from typing import NamedTuple, Dict

from __init__ import base_id
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
        id=base_id + 0
    ),
    "Sticky Hands": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 1
    ),
    "Tongue Swing": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 2
    ),
    "Runi Key": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 3
    ),
    "Glowbug": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 4
    ),
    "Frog": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 5
    ),
    "Fly": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 6
    ),
    "Dragonfly": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 7
    ),
    "Eel": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 8
    ),
    "Bass": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 9
    ),
    "Blue Snack": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 10
    ),
    "Purple Snack": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 11
    ),
    "Magnet Roach": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 12
    ),
    "Mushroll": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 13
    ),
    "Mushfrog": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 14
    ),
    "Beet": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 15
    ),
    "Skater": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 16
    ),
    "Soul Frog": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 17
    ),
    "River Fish": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 18
    ),
    "Bird": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 19
    ),
    "Leafbug": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 20
    ),
    "Wormy": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 21
    ),
    "Minnow": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 22
    ),
    "Turtle": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 23
    ),
    "Blue Jelly": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 24
    ),
    "Roof Snail": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 25
    ),
    "Crab": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 26
    ),
    "Bridge Frog": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 27
    ),
    "Cricket": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 28
    ),
    "Spider": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 29
    ),
    "Moth": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 30
    ),
    "Ammofly": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 31
    ),
    "Pecker": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 32
    ),
    "Soul Fish": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 33
    ),
    "Fog Fly": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 34
    ),
    "Cicada": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 35
    ),
    "Mantis": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 36
    ),
    "Jungle Snack": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 37
    ),
    "Gecko": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 38
    ),
    "Bee": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 39
    ),
    "Mushroom": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 40
    ),
    "Tang": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 41
    ),
    "Axolotyl": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 42
    ),
    "Mite": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 43
    ),
    "Health 1": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 44
    ),
    "Health 2": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 45
    ),
    "Health 3": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 46
    ),
    "Health 4": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 47
    ),
    "Health 5": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 48
    ),
    "Health 6": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 49
    ),
    "Mana 1": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 50
    ),
    "Mana 2": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 51
    ),
    "Mana 3": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 52
    ),
    "Mana 4": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 53
    ),
    "Mana 5": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 54
    ),
    "Mana 6": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 55
    ),
    "Reeder": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 56
    ),
    "Machine Gun": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 57
    ),
    "Weepwood Bow": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 58
    ),
    "Finisher": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 59
    ),
    "Fire Fruit Juicer": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 60
    ),
    "Gatling Gun": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 61
    ),
    "Wooden Cannon": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 62
    ),
    "Fireball": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 63
    ),
    "Mushbomb": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 64
    ),
    "Sharap Shot": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 65
    ),
    "Beanshot": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 66
    ),
    "Zap": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 67
    ),
    "Slam": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 68
    ),
    "Hive": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 69
    ),
    "Puff": FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 70
    ),
}

location_id_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}