from dataclasses import dataclass
from Options import Toggle, Range, Choice, PerGameCommonOptions, DeathLinkMixin, StartInventoryPool

class GameDifficulty(Choice):
    """Determines expected player skill. A harder difficulty means you will be expected to go further in the game with less resources."""
    display_name = "Game Difficulty"
#    option_easy = 0
    option_normal = 1
    option_hard = 2
#    option_very_hard = 3
    default = 1

class GoalCondition(Choice):
    """Determines the win condition for the game. Myzand 2: Traverse Myzand's Forest, defeat him, and lock him away. Eye Chest: Open the 6-Eye Door and collect the Eye Fragment."""
    display_name = "Goal"
    option_myzand_2 = 0
    option_eye_chest = 1
    default = 0

class ShufflePuzzles(Toggle):
    """When enabled, slide puzzles and their rewards will be shuffled into the pool."""
    display_name = "Shuffle Slide Puzzles"

class StartWithGear(Toggle):
    """When enabled, Blue in Lost Swamp will always give you a gun, and you will always find a spell at the Fireball location. (This may break gun/spell plando, so be warned.)"""
    display_name = "I Hate Seedling"

class ShuffleBugEffects(Toggle):
    """Randomizes the temporary effect gained when eating any bug other than Mushroom."""
    display_name = "Shuffle Bug-Eating Effects"

class ShopMultiplier(Range):
    """Decreases the total cost of items in shops by a percentage. 100 = no discount, 0 = free shops."""
    display_name = "Shop Multiplier"
    range_start = 0
    range_end = 100
    default = 100

class OpenCity(Toggle):
    """When enabled, the Lost Swamp portal vine will be enabled from the beginning, allowing quick travel to City without needing Sticky Hands."""
    display_name = "Open City"

class AdvancedParkour(Toggle):
    """When enabled, the player will be expected to do more advanced or unituitive platform movement to get to some locations."""
    display_name = "Hardcore Parkour"

@dataclass
class FrogmonsterOptions(PerGameCommonOptions, DeathLinkMixin):
    start_inventory_from_pool: StartInventoryPool
    game_difficulty: GameDifficulty
    goal: GoalCondition
    shuffle_puzzles: ShufflePuzzles
    i_hate_seedling: StartWithGear
    shuffle_bug_effects: ShuffleBugEffects
    shop_multiplier: ShopMultiplier
    open_city: OpenCity
#    hardcore_parkour: AdvancedParkour

