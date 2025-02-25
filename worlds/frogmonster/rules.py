from typing import Callable, TYPE_CHECKING

from BaseClasses import CollectionState
from .data import combat_data, Difficulty

if TYPE_CHECKING:
    from . import FrogmonsterWorld


def can_beat(world: FrogmonsterWorld, name: str) -> Callable[[CollectionState], bool]:
    pass

def get_combat_data(name: str, difficulty: Difficulty) -> tuple[int, list[str], list[str], list[str]]:
    for combat in combat_data:
        if combat.name == name:
            if difficulty == Difficulty.EASY:
                return combat.score_easy, combat.need, combat.want, combat.tags
            elif difficulty == Difficulty.NORMAL:
                return combat.score_normal, combat.need, combat.want, combat.tags
            elif difficulty == Difficulty.HARD:
                return combat.score_hard, combat.need, combat.want, combat.tags
            elif difficulty == Difficulty.VERY_HARD:
                return combat.score_very_hard, combat.need, combat.want, combat.tags
            else:
                raise ValueError(f"Difficulty {difficulty} not found in Difficulty enum. Something is wrong with the Frogmonster world.")
    raise ValueError(f"Combat {name} not found in data.py. Something is wrong with the Frogmonster world.")