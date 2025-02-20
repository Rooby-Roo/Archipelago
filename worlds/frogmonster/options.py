from dataclasses import dataclass
from Options import Toggle, Range, PerGameCommonOptions, StartInventoryPool

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
    shuffle_bug_effects: ShuffleBugEffects
    shop_multiplier: ShopMultiplier

