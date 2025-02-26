from BaseClasses import CollectionState
from .data import combat_data, Difficulty
from .names import item_names as i
from .names import combat_names as c

def get_custom_rules() -> None:

    def can_fight(name: str, difficulty: Difficulty, state: CollectionState, player: int) -> bool:

        # First, handle some fights that really can't rely on the default calculations.
        weird_fights = {
            c.barge: can_fight_barge
        }
        if name in weird_fights.keys():
            return weird_fights[name](difficulty, state, player)
        
        score, need, want, tags = get_combat_data(name, difficulty)

        for item in need:
            if item == "burn":
                if not can_burn(state, player):
                    return False
            elif not state.has(item, player):
                return False
            
        if state.has(i.dash, player):
            score -= 10

        if score <= 0:
            return True  # we check this multiple times through this formula, since each layer is more computationally expensive than the last.
        
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
                    for swarm_answer in [i.machine_gun, i.gatling_gun, i.fire_fruit_juicer, i.zap]:
                        if state.has(swarm_answer, player):
                            if first_one_best:
                                score -= 5
                                first_one_best = False
                            else:
                                score -= 2
                    for heavy_swarm_answer in [i.machine_gun, i.weepwood_bow, i.fire_fruit_juicer, i.gatling_gun]:
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
        
        if score <= 0:
            return True
        
        raise NotImplementedError("Robby isn't done with can_fight, go yell at him.")
    
    def can_fight_barge(difficulty: Difficulty, state: CollectionState, player: int):
        raise NotImplementedError

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
                (state.has(i.fire_fruit_juicer, player) and state.has(i.metal_ore, player, 16)) or
                (state.has_all([i.gatling_gun, i.gatling_gun_myzand_upgrade], player) and state.has(i.metal_ore, player, 16))
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