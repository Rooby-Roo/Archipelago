from typing import NamedTuple, Dict

from BaseClasses import Location
from .names import location_names as l
from .items import BASE_ID

class FrogmonsterLocation(Location):
    game = "Frogmonster"

class FrogmonsterLocationData(NamedTuple):
    region: str
    id: int = None

location_data_table: Dict[str, FrogmonsterLocationData] = {
    l.goal: FrogmonsterLocationData(
        region="Anywhere",
    ),
    l.dash: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 0
    ),
    l.sticky_hands: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 1
    ),
    l.tongue_swing: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 2
    ),
    l.runi_key: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 3
    ),
    l.glowbug: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 4
    ),
    l.frog: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 5
    ),
    l.fly: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 6
    ),
    l.dragonfly: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 7
    ),
    l.eel: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 8
    ),
    l.bass: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 9
    ),
    l.blue_snack: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 10
    ),
    l.purple_snack: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 11
    ),
    l.magnet_roach: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 12
    ),
    l.mushroll: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 13
    ),
    l.mushfrog: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 14
    ),
    l.beet: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 15
    ),
    l.skater: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 16
    ),
    l.soul_frog: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 17
    ),
    l.river_fish: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 18
    ),
    l.bird: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 19
    ),
    l.leafbug: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 20
    ),
    l.wormy: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 21
    ),
    l.minnow: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 22
    ),
    l.turtle: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 23
    ),
    l.blue_jelly: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 24
    ),
    l.roof_snail: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 25
    ),
    l.crab: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 26
    ),
    l.bridge_frog: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 27
    ),
    l.cricket: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 28
    ),
    l.spider: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 29
    ),
    l.moth: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 30
    ),
    l.ammofly: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 31
    ),
    l.pecker: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 32
    ),
    l.soul_fish: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 33
    ),
    l.fog_fly: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 34
    ),
    l.cicada: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 35
    ),
    l.mantis: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 36
    ),
    l.jungle_snack: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 37
    ),
    l.gecko: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 38
    ),
    l.bee: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 39
    ),
    l.mushroom: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 40
    ),
    l.tang: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 41
    ),
    l.axolotyl: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 42
    ),
    l.mite: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 43
    ),
    l.health_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 44
    ),
    l.health_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 45
    ),
    l.health_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 46
    ),
    l.health_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 47
    ),
    l.health_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 48
    ),
    l.health_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 49
    ),
    l.mana_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 50
    ),
    l.mana_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 51
    ),
    l.mana_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 52
    ),
    l.mana_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 53
    ),
    l.mana_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 54
    ),
    l.mana_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 55
    ),
    l.reeder: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 56
    ),
    l.machine_gun: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 57
    ),
    l.weepwood_bow: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 58
    ),
    l.finisher: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 59
    ),
    l.fire_fruit_juicer: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 60
    ),
    l.gatling_gun: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 61
    ),
    l.wooden_cannon: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 62
    ),
    l.fireball: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 63
    ),
    l.mushbomb: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 64
    ),
    l.sharap_shot: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 65
    ),
    l.beans: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 66
    ),
    l.zap: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 67
    ),
    l.slam: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 68
    ),
    l.hive: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 69
    ),
    l.puff: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 70
    ),
}

location_id_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}