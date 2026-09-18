from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, FreeText

class DeathLink(FreeText):
    """This game supports Death Link entirely in-client. This option does nothing except tell you that
    you can turn it on in the game's options menu."""
    display_name = "Death Link"
    default = "wow, thanks gramma"

@dataclass
class BabushkaOptions(PerGameCommonOptions):
    death_link: DeathLink


# If we want to group our options by similar type, we can do so as well. This looks nice on the website.
option_groups = [
    OptionGroup(
        "Gameplay Options",
        [HardMode, Hammer, ExtraStartingChest, StartWithOneConfettiCannon, TrapChance],
    ),
    OptionGroup(
        "Aesthetic Options",
        [ConfettiExplosiveness, PlayerSprite],
    ),
]

# Finally, we can define some option presets if we want the player to be able to quickly choose a specific "mode".
option_presets = {
    "boring": {
        "hard_mode": False,
        "hammer": False,
        "extra_starting_chest": False,
        "start_with_one_confetti_cannon": False,
        "trap_chance": 0,
        "confetti_explosiveness": ConfettiExplosiveness.range_start,
        "player_sprite": PlayerSprite.option_human,
    },
    "the true way to play": {
        "hard_mode": True,
        "hammer": True,
        "extra_starting_chest": True,
        "start_with_one_confetti_cannon": True,
        "trap_chance": 50,
        "confetti_explosiveness": ConfettiExplosiveness.range_end,
        "player_sprite": PlayerSprite.option_duck,
    },
}
