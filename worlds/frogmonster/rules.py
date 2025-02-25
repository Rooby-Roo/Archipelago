from BaseClasses import CollectionState
from .data import combat_data, Difficulty
from .names import item_names as i

def get_custom_rules() -> None:

    def can_fight(name: str, difficulty: Difficulty, player: int) -> bool:
        score, need, want, tags = get_combat_data(name, difficulty)

    def get_combat_data(name: str, difficulty: Difficulty) -> tuple[int, list[str] | None, list[str] | None, list[str] | None]:
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
    
    def has_level_2_gun(gun: str, state: CollectionState, player: int) -> bool:
        return state.has(gun, player) and state.has(get_gun_upgrade_from_gun(gun), player) and state.has(i.metal_ore, player, 16)

    def get_gun_upgrade_from_gun(gun: str) -> str:
        return {
            i.seedling: i.seedling_myzand_ugrade,
            i.reeder: i.reeder_myzand_upgrade,
            i.machine_gun: i.machine_gun_myzand_upgrade,
            i.weepwood_bow: i.weepwood_bow_myzand_upgrade,
            i.finisher: i.finisher_myzand_upgrade,
            i.fire_fruit_juicer: i.fire_fruit_juicer_myzand_upgrade,
            i.gatling_gun: i.gatling_gun_myzand_upgrade,
            i.wooden_cannon: i.wooden_cannon_myzand_upgrade
        }[gun]