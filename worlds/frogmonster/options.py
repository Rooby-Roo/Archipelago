from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions, StartInventoryPool

class GameDifficulty(Choice):
    """Determines expected player skill. A harder difficulty means you will be expected to go further in the game with less resources."""
    display_name = "Game Difficulty"
    option_easy = 1
    option_normal = 2
    option_hard = 3
    option_very_hard = 4
    default = 2

class ExcludePuzzles(Toggle):
    """When enabled, puzzles and their rewards will be excluded. This includes the chest in the Estate pool."""
    display_name = "Exclude Puzzles"

class StartWithGear(Toggle):
    """When enabled, Blue in Lost Swamp will always give you a gun, and you will always find a spell at the Fireball location."""
    display_name = "Start With Gear"
    # does nothing at the moment, to be implemented later

class ShuffleBugEffects(Toggle):
    """Randomizes the temporary effect gained when eating any bug other than Mushroom.
    CURRENTLY NOT IMPLEMENTED IN THE CLIENT."""
    display_name = "Shuffle Bug-Eating Effects"

class ShopMultiplier(Range):
    """Decreases the total cost of items in shops by a percentage. 100 = no discount, 0 = free shops.
    CURRENTLY NOT IMPLEMENTED IN THE CLIENT."""
    display_name = "Shop Multiplier"
    range_start = 0
    range_end = 100
    default = 100

@dataclass
class FrogmonsterOptions(PerGameCommonOptions):
    start_inventory_from_pool: StartInventoryPool
    game_difficulty: GameDifficulty
#    exclude_puzzles: ExcludePuzzles
#    start_with_gear: StartWithGear
    shuffle_bug_effects: ShuffleBugEffects
    shop_multiplier: ShopMultiplier

