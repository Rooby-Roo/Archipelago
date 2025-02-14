from dataclasses import dataclass
from Options import Toggle, PerGameCommonOptions, StartInventoryPool

class ShuffleBugEffects(Toggle):
    """Randomizes the temporary effect gained when eating any bug other than Mushroom."""
    display_name = "Shuffle Bug-Eating Effects"

@dataclass
class FrogmonsterOptions(PerGameCommonOptions):
    shuffle_bug_effects: ShuffleBugEffects
    start_inventory_from_pool: StartInventoryPool
    pass