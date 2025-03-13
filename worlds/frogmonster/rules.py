from typing import Iterable

from BaseClasses import CollectionState
from .combat import combat_data, Difficulty, secret_synergies, tanky_bugs
from .names import item_names as i
from .names import combat_names as c

myzand_gun_library = {
        i.seedling: i.seedling_myzand_upgrade,
        i.reeder: i.reeder_myzand_upgrade,
        i.machine_gun: i.machine_gun_myzand_upgrade,
        i.weepwood_bow: i.weepwood_bow_myzand_upgrade,
        i.finisher: i.finisher_myzand_upgrade,
        i.fire_fruit_juicer: i.fire_fruit_juicer_myzand_upgrade,
        i.gatling_gun: i.gatling_gun_myzand_upgrade,
        i.wooden_cannon: i.wooden_cannon_myzand_upgrade
    }

def can_fight(name: str, player: int, difficulty: Difficulty, state: CollectionState) -> bool:

    # First, handle some fights that really can't rely on the default calculations.
    weird_fights = {
        c.barge: can_fight_barge
    }
    if name in weird_fights:
        return weird_fights[name](difficulty, state, player)
    
    score, need, want, tags = get_combat_data(name, difficulty)

    for item in need:
        if not state.has(item, player):
            return False
    
    if score <= 0:
        return True
    elif score == 1:
        return (can_dash(tags, difficulty, state, player) or 
                state.has("Gun", player, 1) or 
                state.has("Spell", player, 1) or
                health_count(state, player) >= 1)
    else:
        raise NotImplementedError(f"get countin bub")

def can_fight_all(names: Iterable[str], player: int, difficulty: Difficulty, state: CollectionState) -> bool:
    for name in names:
        if not can_fight(name, player, difficulty, state):
            return False
    return True

def can_fight_barge(difficulty: Difficulty, state: CollectionState, player: int):
    if difficulty == Difficulty.EASY:
        return (
            state.has_all([i.dash, i.fire_fruit_juicer], player) and 
            state.has_group_unique("Guns", player, 2) and
            health_count(state, player) >= 1
        )
    elif difficulty == Difficulty.NORMAL:
        return (
            state.has_all([i.dash, i.fire_fruit_juicer], player) and 
            state.has_group_unique("Guns", player, 2) and
            health_count(state, player) >= 1
        )
    elif difficulty == Difficulty.HARD:
        return (
            state.has(i.dash, player) and
            (state.has(i.fire_fruit_juicer, player) or has_level_2_gun(i.gatling_gun, state, player))
        )
    elif difficulty == Difficulty.VERY_HARD:
        return (
            state.has(i.fire_fruit_juicer, player) or has_level_2_gun(i.gatling_gun, state, player)
        )
    else:
        raise ValueError(f"Difficulty {difficulty} is not a valid type. Something is wrong with the Frogmonster world.")
    
def get_combat_data(name: str, difficulty: Difficulty) -> tuple[int, list[str], list[str], list[str]]:
    for combat in combat_data:
        if combat.name == name:
            if difficulty == Difficulty.EASY:
                return combat.score_easy, combat.need, combat.want, combat.tags
            elif difficulty == Difficulty.NORMAL:
                return combat.score_hard - 3, combat.need, combat.want, combat.tags
            elif difficulty == Difficulty.HARD:
                return combat.score_hard, combat.need, combat.want, combat.tags
            elif difficulty == Difficulty.VERY_HARD:
                return combat.score_very_hard, combat.need, combat.want, combat.tags
            else:
                raise ValueError(f"Difficulty {difficulty} not found in Difficulty enum. Something is wrong with the Frogmonster world.")
    raise ValueError(f"Combat {name} not found in data.py. Something is wrong with the Frogmonster world.")

def can_burn(state: CollectionState, player: int) -> bool:
    return (state.has(i.fire_fruit_juicer, player) or 
            state.has_all([i.fireball, i.cicada], player) or 
            (state.has_all([i.gatling_gun, i.gatling_gun_myzand_upgrade], player) and state.has(i.metal_ore, player, 14))
    )       # 14 ore here since if we're testing this, you don't have fire fruit, and thus can't waste ore on it

def can_burn_underwater(state: CollectionState, player: int) -> bool:
    return (state.has_all([i.fireball, i.cicada], player) or
            (state.has(i.fire_fruit_juicer, player) and state.has(i.metal_ore, player, 14)) or
            (state.has_all([i.gatling_gun, i.gatling_gun_myzand_upgrade], player) and state.has(i.metal_ore, player, 14))
    )
    
def can_dash(tags: list[str], dif: Difficulty, state: CollectionState, player: int) -> bool:
    if "underwater" in tags and dif >= Difficulty.HARD:
        return state.has_any([i.bass, i.dash], player)
    else:
        return state.has(i.dash, player)


def has_level_2_gun(gun: str, state: CollectionState, player: int) -> bool:
    return state.has(gun, player) and state.has(get_gun_upgrade_from_gun(gun), player) and state.has(i.metal_ore, player, 16) and can_upgrade(state, player)

def matching_myzands(state: CollectionState, player: int) -> int:
    count = 0
    for gun in myzand_gun_library:
        if gun is not i.seedling:
            if state.has(gun, player) and state.has(myzand_gun_library[gun], player):
                count += 1
        elif gun is i.seedling:
            if state.has(i.seedling_myzand_upgrade, player):
                count += 1
    return count

def health_count(state: CollectionState, player: int) -> int:
    count = 0
    if state.has(i.health, player, 3):
        if state.has(i.health, player, 6):
            count += 1
        count += 1
    if state.has_any(tanky_bugs, player):
        count += 1
    return count

def can_upgrade(state: CollectionState, player: int) -> bool:
    return state.has(i.workshop_key, player)

def get_gun_upgrade_from_gun(gun: str) -> str:
    return myzand_gun_library[gun]
