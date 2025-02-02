from typing import NamedTuple, Dict

from __init__ import base_id
from BaseClasses import Location
from .names.location_names import location_names as l

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
        id=base_id + 0
    ),
    l.sticky_hands: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 1
    ),
    l.tongue_swing: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 2
    ),
    l.runi_key: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 3
    ),
    l.glowbug: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 4
    ),
    l.frog: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 5
    ),
    l.fly: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 6
    ),
    l.dragonfly: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 7
    ),
    l.eel: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 8
    ),
    l.bass: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 9
    ),
    l.blue_snack: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 10
    ),
    l.purple_snack: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 11
    ),
    l.magnet_roach: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 12
    ),
    l.mushroll: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 13
    ),
    l.mushfrog: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 14
    ),
    l.beet: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 15
    ),
    l.skater: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 16
    ),
    l.soul_frog: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 17
    ),
    l.river_fish: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 18
    ),
    l.bird: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 19
    ),
    l.leafbug: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 20
    ),
    l.wormy: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 21
    ),
    l.minnow: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 22
    ),
    l.turtle: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 23
    ),
    l.blue_jelly: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 24
    ),
    l.roof_snail: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 25
    ),
    l.crab: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 26
    ),
    l.bridge_frog: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 27
    ),
    l.cricket: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 28
    ),
    l.spider: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 29
    ),
    l.moth: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 30
    ),
    l.ammofly: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 31
    ),
    l.pecker: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 32
    ),
    l.soul_fish: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 33
    ),
    l.fog_fly: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 34
    ),
    l.cicada: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 35
    ),
    l.mantis: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 36
    ),
    l.jungle_snack: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 37
    ),
    l.gecko: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 38
    ),
    l.bee: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 39
    ),
    l.mushroom: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 40
    ),
    l.tang: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 41
    ),
    l.axolotyl: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 42
    ),
    l.mite: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 43
    ),
    l.health_1: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 44
    ),
    l.health_2: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 45
    ),
    l.health_3: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 46
    ),
    l.health_4: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 47
    ),
    l.health_5: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 48
    ),
    l.health_6: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 49
    ),
    l.mana_1: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 50
    ),
    l.mana_2: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 51
    ),
    l.mana_3: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 52
    ),
    l.mana_4: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 53
    ),
    l.mana_5: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 54
    ),
    l.mana_6: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 55
    ),
    l.reeder: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 56
    ),
    l.machine_gun: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 57
    ),
    l.weepwood_bow: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 58
    ),
    l.finisher: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 59
    ),
    l.fire_fruit_juicer: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 60
    ),
    l.gatling_gun: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 61
    ),
    l.wooden_cannon: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 62
    ),
    l.fireball: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 63
    ),
    l.mushbomb: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 64
    ),
    l.sharap_shot: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 65
    ),
    l.beanshot: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 66
    ),
    l.zap: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 67
    ),
    l.slam: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 68
    ),
    l.hive: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 69
    ),
    l.puff: FrogmonsterLocationData(
        region="Anywhere",
        id=base_id + 70
    ),
}

location_id_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}