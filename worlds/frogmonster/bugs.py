from typing import NamedTuple, Callable

from BaseClasses import CollectionState
from .names import item_names as i
from .names import combat_names as c
from .names import region_names as r
from .rules import can_fight
from .combat import Difficulty

class BugType(NamedTuple):
    name: str
    bug_id: int
    slot_cost: int
    regions: list[tuple[str, Callable[[int, Difficulty, CollectionState], bool] | None]]

every_bug = [  # Regions values are noncomprehensive. Regions are excluded if there's a current overlap in access requirements.
    BugType(name=i.glowbug,        bug_id=1,  slot_cost=2, regions=[(r.lost_swamp, None)]),
    BugType(name=i.frog,           bug_id=2,  slot_cost=1, regions=[(r.lost_swamp, None)]),
    BugType(name=i.fly,            bug_id=3,  slot_cost=2, regions=[(r.lost_swamp, None)]),
    BugType(name=i.dragonfly,      bug_id=4,  slot_cost=2, regions=[(r.lost_swamp, None)]),
    BugType(name=i.eel,            bug_id=5,  slot_cost=2, regions=[(r.lost_swamp_after_groth, lambda player, dif, state: state.has_any([i.dash, i.frog], player))]),  # Requires Dash or Frog. Eel requires Groth defeat
    BugType(name=i.bass,           bug_id=6,  slot_cost=1, regions=[(r.lost_swamp, None)]),  # Blue's Cabin
    BugType(name=i.blue_snack,     bug_id=7,  slot_cost=3, regions=[(r.marvins, None), (r.workshop, lambda player, dif, state: state.has_all([i.dash, i.sticky_hands], player))]),
    BugType(name=i.purple_snack,   bug_id=8,  slot_cost=4, regions=[(r.marvins, None)]),	
    BugType(name=i.magnet_roach,   bug_id=9,  slot_cost=1, regions=[(r.yellow_forest_town, None), (r.runi_arena, lambda player, dif, state: can_fight(c.runi, player, dif, state))]),  # For sale, or eatable during Runi fight
    BugType(name=i.mushroll,       bug_id=10, slot_cost=2, regions=[(r.marvins, None)]),
    BugType(name=i.mushfrog,       bug_id=11, slot_cost=1, regions=[(r.marvins, None), (r.treetops, None)]),
    BugType(name=i.beet,           bug_id=12, slot_cost=3, regions=[r.outskirts, r.ridge, r.forest_floor]),
    BugType(name=i.skater,         bug_id=13, slot_cost=2, regions=[r.very_lost_swamp, r.forest_floor]),
    BugType(name=i.soul_frog,      bug_id=14, slot_cost=1, regions=[r.anywhere]),
    BugType(name=i.river_fish,     bug_id=15, slot_cost=1, regions=[r.yellow_forest]),
    BugType(name=i.bird,           bug_id=16, slot_cost=1, regions=[r.yellow_forest]),
    BugType(name=i.leafbug,        bug_id=17, slot_cost=3, regions=[r.yellow_forest]),
    BugType(name=i.wormy,          bug_id=18, slot_cost=2, regions=[r.workshop]),
    BugType(name=i.minnow,         bug_id=19, slot_cost=2, regions=[r.green_sea]),
    BugType(name=i.turtle,         bug_id=20, slot_cost=2, regions=[r.green_sea]),
    BugType(name=i.blue_jelly,     bug_id=21, slot_cost=3, regions=[r.green_sea, r.deep]),  # Green Sea location is Behind Key Door	
    BugType(name=i.roof_snail,     bug_id=22, slot_cost=2, regions=[r.city]),
    BugType(name=i.crab,           bug_id=23, slot_cost=0, regions=[r.lost_swamp]),
    BugType(name=i.bridge_frog,    bug_id=24, slot_cost=0, regions=[r.city]),
    BugType(name=i.cricket,        bug_id=25, slot_cost=3, regions=[r.city]),
    BugType(name=i.spider,         bug_id=26, slot_cost=2, regions=[r.old_road]),
    BugType(name=i.moth,           bug_id=27, slot_cost=2, regions=[r.old_road]),
    BugType(name=i.ammofly,        bug_id=28, slot_cost=2, regions=[r.treetops, r.old_wood]),  # after arena 1, before big door
    BugType(name=i.pecker,         bug_id=29, slot_cost=3, regions=[r.thickness, r.moridonos]),  # verify these
    BugType(name=i.soul_fish,      bug_id=30, slot_cost=1, regions=[r.anywhere]),  # Death possible in water in Lost Swamp, so anywhere.
    BugType(name=i.fog_fly,        bug_id=31, slot_cost=3, regions=[r.fog_garden, r.temple]),
    BugType(name=i.cicada,         bug_id=32, slot_cost=2, regions=[r.cicada_cove]),
    BugType(name=i.mantis,         bug_id=33, slot_cost=2, regions=[r.forest_floor]),
    BugType(name=i.jungle_snack,   bug_id=34, slot_cost=2, regions=[r.forest_floor, r.rootden]),
    BugType(name=i.gecko,          bug_id=35, slot_cost=2, regions=[r.forest_floor]),
    BugType(name=i.mushroom,       bug_id=36, slot_cost=3, regions=[r.moridonos]),
    BugType(name=i.bee,            bug_id=37, slot_cost=3, regions=[r.hive]),
    BugType(name=i.tang,           bug_id=38, slot_cost=3, regions=[r.reef]),
    BugType(name=i.axolotyl,       bug_id=39, slot_cost=3, regions=[r.quarry]),
    BugType(name=i.mite,           bug_id=40, slot_cost=2, regions=[r.ridge]),
]