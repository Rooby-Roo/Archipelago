from typing import Iterable

from BaseClasses import CollectionState
from .combat import combat_data, Difficulty, secret_synergies, tanky_bugs
from .names import item_names as i
from .names import combat_names as c

def can_fight(name: str, player: int, difficulty: Difficulty, state: CollectionState) -> bool:

    # First, handle some fights that really can't rely on the default calculations.
    weird_fights = {
        c.barge: can_fight_barge
    }
    if name in weird_fights.keys():
        return weird_fights[name](difficulty, state, player)
    
    score, need, want, tags = get_combat_data(name, difficulty)

    for item in need:
        if not state.has(item, player):
            return False
    return True

    # Yes this is unreachable but I need to completely rework this, so we're basically ignoring combat difficulty for now
    if state.has(i.dash, player):
        score -= 15

    if score <= 0:
        return True  # we check this here to offer an early eject, since dash is so powerful and will simplify a lot of combats.
    
    # Handling: Fight-specific utilities
    for item in want:
        if state.has(item, player):
            score -= 5
    for item in tags:
        match item:
            case "underwater":  # fight takes place primarily or exclusively underwater.
                if state.has(i.bass, player):
                    score -= 5
            case "swarm":  # fight is primarily large quantities of small monsters. Weapons that spray are preferred.
                first_one_best = True
                swarm_answers = [i.machine_gun, i.gatling_gun, i.zap]
                if "underwater" not in tags:
                    swarm_answers.append(i.fire_fruit_juicer)  # standalone ffj cannot work underwater. Only gun with this property. 
                for swarm_answer in swarm_answers:
                    if state.has(swarm_answer, player):
                        if first_one_best:
                            score -= 5
                            first_one_best = False
                        else:
                            score -= 2
                for heavy_swarm_answer in [item for item in [i.machine_gun, i.weepwood_bow, i.fire_fruit_juicer, i.gatling_gun] if state.has(item, player)]:  # comprehension to pre-check the level 1 gun types before getting into the slightly costly has_2 function
                    if has_level_2_gun(heavy_swarm_answer, state, player):
                        if first_one_best:
                            score -= 5
                            first_one_best = False
                        else:
                            score -= 2
            case "stationary":  # fight against a single target (or two) that doesn't really move. Weapons that benefit that are calculated here.
                first_one_best = True
                for stationary_answer in [i.weepwood_bow, i.wooden_cannon, i.puff]:
                    if state.has(stationary_answer, player):
                        if first_one_best:
                            score -= 5
                            first_one_best = False
                        else:
                            score -= 2
            case _:
                raise ValueError(f"Tag {item} is not handled for in the fight logic. Something is wrong with the Frogmonster world.")
    
    # Handling: Guns
    guns = state.count_group_unique("Guns", player)
    # is this something I should make hashable? It feels small enough that this might be faster than setting up a dict.
    gun_scores = {
        0: 0,
        1: 8,   # 8
        2: 15,  # 7
        3: 20,  # 5
        4: 23,  # 3
        5: 26,  # 3
        6: 28,  # 2
        7: 30,  # 2
    }
    score -= gun_scores.get(guns, 0)

    if can_upgrade(state, player):
        ores = state.count(i.metal_ore, player)
        max_ores = max(ores, guns)
        score -= (4 * max_ores)  # technically this is operating on the assumption that you're not going to go down both upgrade paths on most guns. It's all skill estimations so idc

    # Handling: Spells
    spells = state.count_group_unique("Spells", player)
    good_heal_spells = [i.fireball, i.beans, i.puff]
    if "swarm" in tags:
        good_heal_spells.append(i.zap)
    for spell in good_heal_spells:
        if state.has(spell, player):
            score -= 4
            break
    spell_scores = {
        0: 0,
        1: 7,
        2: 10,
        3: 12,
        4: 13,
        5: 14,
        6: 15,
        7: 15,
        8: 15
    }
    score -= spell_scores.get(spells, 0)

    # Handling: Spell Synergies
    for spell, bug in secret_synergies.items():
        if state.has_all([spell, bug], player):
            score -= 3
    
    # Handling: Health and Mana
    hp = state.count(i.health, player)
    mp = state.count(i.mana, player)
    if hp >= 3:
        if hp >= 6:
            score -= 10
        score -= 5
    if mp >= 3 and state.has_group("Spells", player, 1):
        if mp >= 6:
            score -= 6
        score -= 3
    
    if score <= 0:
        return True
    else:
        return False

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
            (state.has_any(tanky_bugs, player) or state.has(i.health, 3))
        )
    elif difficulty == Difficulty.NORMAL:
        return (
            state.has_all([i.dash, i.fire_fruit_juicer], player) and 
            state.has_group_unique("Guns", player, 2) and
            (state.has_any(tanky_bugs, player) or state.has(i.health, 3))
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
        raise ValueError(f"Difficutly {difficulty} is not a valid type. Something is wrong with the Frogmonster world.")
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

def has_level_2_gun(gun: str, state: CollectionState, player: int) -> bool:
    return state.has(gun, player) and state.has(get_gun_upgrade_from_gun(gun), player) and state.has(i.metal_ore, player, 16) and can_upgrade(state, player)

def can_upgrade(state: CollectionState, player: int) -> bool:
    return state.has(i.workshop_key, player)

def get_gun_upgrade_from_gun(gun: str) -> str:
    return {
        i.seedling: i.seedling_myzand_upgrade,
        i.reeder: i.reeder_myzand_upgrade,
        i.machine_gun: i.machine_gun_myzand_upgrade,
        i.weepwood_bow: i.weepwood_bow_myzand_upgrade,
        i.finisher: i.finisher_myzand_upgrade,
        i.fire_fruit_juicer: i.fire_fruit_juicer_myzand_upgrade,
        i.gatling_gun: i.gatling_gun_myzand_upgrade,
        i.wooden_cannon: i.wooden_cannon_myzand_upgrade
    }[gun]