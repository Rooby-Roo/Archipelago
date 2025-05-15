from dataclasses import dataclass
from Options import OptionSet, Toggle, Range, Choice, PerGameCommonOptions, TextChoice,random,ItemDict,OptionDict, DefaultOnToggle
from .names import item_names as iname

# class Goal(Choice):
#     """Choose your goal for the multiworld
#     - Pelly Hunt: Exctract each of the Pelly Statues from all level types
#     - Level Quota: Complete a certain number of levels in a single run"""
#     display_name: str = "Goal"
#     option_pelly_hunt = 0
#     option_level_quota = 1
#     default = 0

class PellyHunt(OptionSet):
    """Choose which Pellys will be required for victory"""
    display_name: str = "Pellys Required"
    valid_keys = {
        "Standard Pelly",
        "Glass Pelly",
        "Gold Pelly"
    }
    default = valid_keys

class PellySpawning(DefaultOnToggle):
    """Determines how Pellys are spawned
    True: Spawns all Pellys. All Pellys are loctions.
    False: Only spawns Pellys chosen in 'Pellys Required'. Only spawned Pellys are Locations."""
    display_name: str = "Pelly Spawning"

class LevelQuota(Range):
    """Choose how many levels must be completed for your goal. This is in addition to gathering all Pellys."""
    display_name: str = "Level Quota"
    range_start = 1
    range_end = 20
    default = 8

class ShopPackCount(Range):
    """Choose how many Archipelago Shop Items are unlocked with each Progressive Shop Stock."""
    display_name: str = "Progressive Shop Stock Amount"
    range_start = 5
    range_end = 50
    default = 10

class ShopUpgradeLocationsTotal(Range):
    """Choose how many Archipelago Items show up in the Upgrades section of the Shop"""
    display_name: str = "Total Shop Upgrade Locations"
    range_start = 20
    range_end = 100
    default = 80

class ShopUpgradeLocationsInLogic(Range):
    """Choose how many shop how many shop upgrades will be potentially logically relevant.
    Items past this number will not have progression items.
    This number gets set to the Total Shop Upgrade Locations if its greater.\n"""
    display_name: str = "Shop Upgrade Locations in Logic"
    range_start = 20
    range_end = 100
    default = 60

class StartingLevelType(TextChoice):
    """Choose which level type to start with"""
    display_name: str = "Starting Level Type"
    option_swiftbroom_academy = 0
    option_headman_manor = 1
    option_mcjannek_station = 2
    default = "random"

class UpgradeItemWeights(OptionDict):
    """Choose the Weights for adding Upgrades to the Item Pool"""
    display_name: str = "Upgrade Item Weights"
    default = {
        iname.health_up : 5,
        iname.strength_up : 3,
        iname.range_up : 2,
        iname.sprint_up: 3,
        iname.stamina_up : 5, 
        iname.player_count_up : 1, 
        iname.double_jump_up : 2, 
        iname.tumble_up : 2
    }
    


@dataclass
class REPOGameOptions(PerGameCommonOptions):
    #goal: Goal
    pellys_required: PellyHunt
    pelly_spawning : PellySpawning
    level_quota: LevelQuota 
    shop_stock: ShopPackCount
    shop_upgrade_total: ShopUpgradeLocationsTotal
    shop_upgrade_logical: ShopUpgradeLocationsInLogic
    starting_level_type: StartingLevelType
    upgrade_item_weights: UpgradeItemWeights

    
