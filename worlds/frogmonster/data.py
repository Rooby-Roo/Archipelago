from typing import NamedTuple
from enum import Enum
from .names import item_names as i
from .names import combat_names as c

class BugType(NamedTuple):
    name: str
    bug_id: int
    slot_cost: int
    regions: list[str]

every_bug = [  # Regions values are noncomprehensive. Regions are excluded if there's a current overlap in access requirements.
    BugType(name=i.glowbug,        bug_id=1,  slot_cost=2, regions=["Lost Swamp"]),
    BugType(name=i.frog,           bug_id=2,  slot_cost=1, regions=["Lost Swamp"]),
    BugType(name=i.fly,            bug_id=3,  slot_cost=2, regions=["Lost Swamp"]),
    BugType(name=i.dragonfly,      bug_id=4,  slot_cost=2, regions=["Lost Swamp"]),
    BugType(name=i.eel,            bug_id=5,  slot_cost=2, regions=["Lost Swamp"]),  # Requires Dash or Frog. Eel requires Groth defeat
    BugType(name=i.bass,           bug_id=6,  slot_cost=1, regions=["Lost Swamp"]),  # Where?
    BugType(name=i.blue_snack,     bug_id=7,  slot_cost=3, regions=["Marvin's Domain", "Bins' Machine"]),
    BugType(name=i.purple_snack,   bug_id=8,  slot_cost=4, regions=["Marvin's Domain"]),	
    BugType(name=i.magnet_roach,   bug_id=9,  slot_cost=1, regions=["Yellow Forest", "Ridge"]),  # For sale, or eatable during Runi fight
    BugType(name=i.mushroll,       bug_id=10, slot_cost=2, regions=["Marvin's Domain"]),
    BugType(name=i.mushfrog,       bug_id=11, slot_cost=1, regions=["Marvin's Domain", "Treetops"]),
    BugType(name=i.beet,           bug_id=12, slot_cost=3, regions=["Outskirts", "Ridge", "Forest Floor"]),
    BugType(name=i.skater,         bug_id=13, slot_cost=2, regions=["Very Lost Swamp", "Forest Floor"]),
    BugType(name=i.soul_frog,      bug_id=14, slot_cost=1, regions=["Anywhere"]),
    BugType(name=i.river_fish,     bug_id=15, slot_cost=1, regions=["Yellow Forest"]),
    BugType(name=i.bird,           bug_id=16, slot_cost=1, regions=["Yellow Forest"]),
    BugType(name=i.leafbug,        bug_id=17, slot_cost=3, regions=["Yellow Forest"]),
    BugType(name=i.wormy,          bug_id=18, slot_cost=2, regions=["Bins' Machine"]),
    BugType(name=i.minnow,         bug_id=19, slot_cost=2, regions=["Green Sea"]),
    BugType(name=i.turtle,         bug_id=20, slot_cost=2, regions=["Green Sea"]),
    BugType(name=i.blue_jelly,     bug_id=21, slot_cost=3, regions=["Green Sea", "Deep"]),  # Green Sea location is Behind Key Door	
    BugType(name=i.roof_snail,     bug_id=22, slot_cost=2, regions=["City"]),
    BugType(name=i.crab,           bug_id=23, slot_cost=0, regions=["Lost Swamp"]),
    BugType(name=i.bridge_frog,    bug_id=24, slot_cost=0, regions=["City"]),
    BugType(name=i.cricket,        bug_id=25, slot_cost=3, regions=["City"]),
    BugType(name=i.spider,         bug_id=26, slot_cost=2, regions=["Old Road"]),
    BugType(name=i.moth,           bug_id=27, slot_cost=2, regions=["Old Road"]),
    BugType(name=i.ammofly,        bug_id=28, slot_cost=2, regions=["Treetops, Old Wood"]),
    BugType(name=i.pecker,         bug_id=29, slot_cost=3, regions=["Thickness", "Moridono's Domain"]),  # verify these
    BugType(name=i.soul_fish,      bug_id=30, slot_cost=1, regions=["Anywhere"]),  # Death possible in water in Lost Swamp, so anywhere.
    BugType(name=i.fog_fly,        bug_id=31, slot_cost=3, regions=["Fog Fly", "Temple"]),
    BugType(name=i.cicada,         bug_id=32, slot_cost=2, regions=["Cicada Cove"]),
    BugType(name=i.mantis,         bug_id=33, slot_cost=2, regions=["Forest Floor"]),
    BugType(name=i.jungle_snack,   bug_id=34, slot_cost=2, regions=["Forest Floor", "Rootden"]),
    BugType(name=i.gecko,          bug_id=35, slot_cost=2, regions=["Forest Floor"]),
    BugType(name=i.mushroom,       bug_id=36, slot_cost=3, regions=["Moridono's Domain"]),
    BugType(name=i.bee,            bug_id=37, slot_cost=3, regions=["Hive"]),
    BugType(name=i.tang,           bug_id=38, slot_cost=3, regions=["Reef"]),
    BugType(name=i.axolotyl,       bug_id=39, slot_cost=3, regions=["Quarry", "Temple"]),
    BugType(name=i.mite,           bug_id=40, slot_cost=2, regions=["Ridge"]),
]

class CombatType(NamedTuple): 
    name: str
    score_easy: int
    score_normal: int
    score_hard: int
    score_very_hard: int
    need: list[str] | None = None
    want: list[str] | None = None
    tags: list[str] | None = None

class Difficulty(Enum):
    EASY = 0
    NORMAL = 1
    HARD = 2
    VERY_HARD = 3

def score_undefined():
    raise NotImplementedError("A combat has not been scored yet.")

X = score_undefined()

combat_data = [
    CombatType(name=c.marvin_arena_1,          score_easy=X, score_normal=0, score_hard=0, score_very_hard=0, tags=["stationary"]),
    CombatType(name=c.outskirts_arena_1,       score_easy=X, score_normal=1, score_hard=0, score_very_hard=0,),
    CombatType(name=c.very_lost_swamp_general, score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.very_lost_swamp_arena_1, score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.yellow_forest_arena_1,   score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.yellow_forest_arena_2,   score_easy=X, score_normal=X, score_hard=X, score_very_hard=0,),
    CombatType(name=c.green_sea_arena_1,       score_easy=X, score_normal=X, score_hard=0, score_very_hard=0, tags=["underwater", "swarm"]),
    CombatType(name=c.green_sea_arena_2,       score_easy=X, score_normal=X, score_hard=0, score_very_hard=0, tags=["underwater", "swarm"]),
    CombatType(name=c.green_sea_arena_3,       score_easy=X, score_normal=X, score_hard=X, score_very_hard=X, tags=["underwater", "swarm"]),
    CombatType(name=c.old_road_general,        score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.old_road_arena_1,        score_easy=X, score_normal=X, score_hard=X, score_very_hard=0,),
    CombatType(name=c.old_road_arena_2,        score_easy=X, score_normal=X, score_hard=X, score_very_hard=0,),
    CombatType(name=c.under_city_arena_1,      score_easy=X, score_normal=0, score_hard=0, score_very_hard=0, tags=["swarm"]),
    CombatType(name=c.forest_floor_general,    score_easy=X, score_normal=0, score_hard=0, score_very_hard=0,),
    CombatType(name=c.forest_floor_arena_1,    score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.old_wood_general,        score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.hive_general,            score_easy=X, score_normal=X, score_hard=X, score_very_hard=0,),
    # More general combats to come eventually I just need to route them out

    CombatType(name=c.groth,                   score_easy=1, score_normal=0, score_hard=0, score_very_hard=0,),
    CombatType(name=c.marvin,                  score_easy=X, score_normal=0, score_hard=0, score_very_hard=0, tags=["stationary"]),
    CombatType(name=c.snake,                   score_easy=X, score_normal=1, score_hard=0, score_very_hard=0,),
    CombatType(name=c.yanoy,                   score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.placeholder,             score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.limbs,                   score_easy=X, score_normal=X, score_hard=0, score_very_hard=0,),
    CombatType(name=c.eels,                    score_easy=X, score_normal=X, score_hard=X, score_very_hard=0, tags=["underwater"]),
    CombatType(name=c.xoto,                    score_easy=X, score_normal=X, score_hard=0, score_very_hard=0, need=[i.dash, i.sticky_hands]),
    CombatType(name=c.valda,                   score_easy=X, score_normal=X, score_hard=X, score_very_hard=X, tags=["stationary"]),
    CombatType(name=c.djumbo,                  score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.dekula,                  score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.chroma,                  score_easy=X, score_normal=X, score_hard=0, score_very_hard=0, want=[i.machine_gun, i.gatling_gun],),
    CombatType(name=c.tymbal,                  score_easy=X, score_normal=X, score_hard=0, score_very_hard=0, want=[i.sticky_hands], tags=["swarm"]),
    CombatType(name=c.foraz,                   score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.hedgeward,               score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.runi,                    score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.barge,                   score_easy=X, score_normal=X, score_hard=X, score_very_hard=X, need=["burn"]),
    CombatType(name=c.door_crab,               score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.lazaro,                  score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.zythida,                 score_easy=X, score_normal=X, score_hard=X, score_very_hard=X, need=[i.tongue_swing],),
    CombatType(name=c.krogar,                  score_easy=X, score_normal=X, score_hard=X, score_very_hard=X, tags=["underwater"]),
    CombatType(name=c.moridono,                score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.brothers,                score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.myzand_1,                score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
    CombatType(name=c.myzand_2,                score_easy=X, score_normal=X, score_hard=X, score_very_hard=X,),
]