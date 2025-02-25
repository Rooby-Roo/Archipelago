from typing import NamedTuple, Dict

from BaseClasses import Location, LocationProgressType
from .names import location_names as l
from .items import BASE_ID

class FrogmonsterLocation(Location):
    game = "Frogmonster"

class FrogmonsterLocationData(NamedTuple):
    region: str
    id: int | None = None
    progress_type: LocationProgressType = LocationProgressType.DEFAULT
    groups: list[str] = []

location_data_table: Dict[str, FrogmonsterLocationData] = {

    # Locations
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
    l.sharp_shot: FrogmonsterLocationData(
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
    l.bug_slot_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 71
    ),
    l.bug_slot_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 72
    ),
    l.bug_slot_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 73
    ),
    l.bug_slot_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 74
    ),
    l.bug_slot_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 75,
        progress_type=LocationProgressType.EXCLUDED # 30 bugs potentially being required is kinda miserable. Excluded for now.
    ),
    l.bug_slot_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 76,
        progress_type=LocationProgressType.EXCLUDED # 40 bugs potentially being required is kinda miserable. Excluded for now.
    ),
    l.bug_slot_7: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 77
    ),
    l.metal_ore_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 78
    ),
    l.metal_ore_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 79
    ),
    l.metal_ore_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 80
    ),
    l.metal_ore_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 81
    ),
    l.metal_ore_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 82
    ),
    l.metal_ore_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 83
    ),
    l.metal_ore_7: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 84
    ),
    l.metal_ore_8: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 85
    ),
    l.metal_ore_9: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 86
    ),
    l.metal_ore_10: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 87
    ),
    l.metal_ore_11: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 88
    ),
    l.metal_ore_12: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 89
    ),
    l.metal_ore_13: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 90
    ),
    l.metal_ore_14: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 91
    ),
    l.metal_ore_15: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 92
    ),
    l.metal_ore_16: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 93
    ),
    l.metal_ore_17: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 94
    ),
    l.metal_ore_18: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 95
    ),
    l.metal_ore_19: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 96
    ),
    l.eel_trophy: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 97
    ),
    l.eye_fragment: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 98
    ),
    l.key_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 99
    ),
    l.key_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 100
    ),
    l.key_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 101
    ),
    l.smooth_stone_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 102
    ),
    l.smooth_stone_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 103
    ),
    l.smooth_stone_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 104
    ),
    l.smooth_stone_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 105
    ),
    l.smooth_stone_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 106
    ),
    l.smooth_stone_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 107
    ),
    l.smooth_stone_7: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 108
    ),
    l.smooth_stone_8: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 109
    ),
    l.smooth_stone_9: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 110
    ),
    l.smooth_stone_10: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 111
    ),
    l.smooth_stone_11: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 112
    ),
    l.smooth_stone_12: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 113
    ),
    l.square_rock_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 114
    ),
    l.square_rock_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 115
    ),
    l.square_rock_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 116
    ),
    l.square_rock_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 117
    ),
    l.square_rock_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 118
    ),
    l.square_rock_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 119
    ),
    l.square_rock_7: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 120
    ),
    l.square_rock_8: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 121
    ),
    l.square_rock_9: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 122
    ),
    l.square_rock_10: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 123
    ),
    l.dark_pebble_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 124
    ),
    l.dark_pebble_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 125
    ),
    l.dark_pebble_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 126
    ),
    l.dark_pebble_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 127
    ),
    l.dark_pebble_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 128
    ),
    l.dark_pebble_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 129
    ),
    l.dark_pebble_7: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 130
    ),
    l.dark_pebble_8: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 131
    ),
    l.sparkling_gem_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 132
    ),
    l.sparkling_gem_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 133
    ),
    l.sparkling_gem_3: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 134
    ),
    l.sparkling_gem_4: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 135,
        progress_type=LocationProgressType.EXCLUDED # Possible to permanently miss this if you kill Supo, force excluded for now.
    ),
    l.sparkling_gem_5: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 136
    ),
    l.sparkling_gem_6: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 137
    ),
    l.seedling_myzand_ugrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 138
    ),
    l.reeder_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 139
    ),
    l.machine_gun_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 140
    ),
    l.weepwood_bow_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 141
    ),
    l.finisher_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 142
    ),
    l.fire_fruit_juicer_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 143
    ),
    l.gatling_gun_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 144
    ),
    l.wooden_cannon_myzand_upgrade: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 145
    ),
    l.yellow_forest_puzzle: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 146
    ),
    l.city_puzzle_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 147
    ),
    l.city_puzzle_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 148
    ),
    l.mansion_puzzle_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 149
    ),
    l.mansion_puzzle_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 150
    ),
    l.fog_garden_puzzle_1: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 151
    ),
    l.fog_garden_puzzle_2: FrogmonsterLocationData(
        region="Anywhere",
        id=BASE_ID + 152
    ),
    # Coin chests to be added when they are documented

    # Events
    l.goal: FrogmonsterLocationData(
        region="Anywhere",
    ),
}

location_id_table = {name: data.id for name, data in location_data_table.items() if data.id is not None}

location_name_groups = {
    "Puzzles": {
        l.yellow_forest_puzzle,
        l.city_puzzle_1,
        l.city_puzzle_2,
        l.mansion_puzzle_1,
        l.mansion_puzzle_2,
        l.fog_garden_puzzle_1,
        l.fog_garden_puzzle_2
    }
}