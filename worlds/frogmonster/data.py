from typing import NamedTuple
from .names import item_names as i

class BugType(NamedTuple):
    name: str
    bug_id: int
    slot_cost: int

every_bug = [
    BugType(name=i.glowbug,        bug_id=1,  slot_cost=0),
    BugType(name=i.frog,           bug_id=2,  slot_cost=0),
    BugType(name=i.fly,            bug_id=3,  slot_cost=0),
    BugType(name=i.dragonfly,      bug_id=4,  slot_cost=0),
    BugType(name=i.eel,            bug_id=5,  slot_cost=0),
    BugType(name=i.bass,           bug_id=6,  slot_cost=0),
    BugType(name=i.blue_snack,     bug_id=7,  slot_cost=0),
    BugType(name=i.purple_snack,   bug_id=8,  slot_cost=0),
    BugType(name=i.magnet_roach,   bug_id=9,  slot_cost=0),
    BugType(name=i.mushroll,       bug_id=10, slot_cost=0),
    BugType(name=i.mushfrog,       bug_id=11, slot_cost=0),
    BugType(name=i.beet,           bug_id=12, slot_cost=0),
    BugType(name=i.skater,         bug_id=13, slot_cost=0),
    BugType(name=i.soul_frog,      bug_id=14, slot_cost=0),
    BugType(name=i.river_fish,     bug_id=15, slot_cost=0),
    BugType(name=i.bird,           bug_id=16, slot_cost=0),
    BugType(name=i.leafbug,        bug_id=17, slot_cost=0),
    BugType(name=i.wormy,          bug_id=18, slot_cost=0),
    BugType(name=i.minnow,         bug_id=19, slot_cost=0),
    BugType(name=i.turtle,         bug_id=20, slot_cost=0),
    BugType(name=i.blue_jelly,     bug_id=21, slot_cost=0),
    BugType(name=i.roof_snail,     bug_id=22, slot_cost=0),
    BugType(name=i.crab,           bug_id=23, slot_cost=0),
    BugType(name=i.bridge_frog,    bug_id=24, slot_cost=0),
    BugType(name=i.cricket,        bug_id=25, slot_cost=0),
    BugType(name=i.spider,         bug_id=26, slot_cost=0),
    BugType(name=i.moth,           bug_id=27, slot_cost=0),
    BugType(name=i.ammofly,        bug_id=28, slot_cost=0),
    BugType(name=i.pecker,         bug_id=29, slot_cost=0),
    BugType(name=i.soul_fish,      bug_id=30, slot_cost=0),
    BugType(name=i.fog_fly,        bug_id=31, slot_cost=0),
    BugType(name=i.cicada,         bug_id=32, slot_cost=0),
    BugType(name=i.mantis,         bug_id=33, slot_cost=0),
    BugType(name=i.jungle_snack,   bug_id=34, slot_cost=0),
    BugType(name=i.gecko,          bug_id=35, slot_cost=0),
    BugType(name=i.mushroom,       bug_id=36, slot_cost=0),
    BugType(name=i.bee,            bug_id=37, slot_cost=0),
    BugType(name=i.tang,           bug_id=38, slot_cost=0),
    BugType(name=i.axolotyl,       bug_id=39, slot_cost=0),
    BugType(name=i.mite,           bug_id=40, slot_cost=0)
]
