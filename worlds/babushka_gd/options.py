from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Range, Toggle, FreeText

class DeathLink(FreeText):
    """This game supports Death Link entirely in-client. This option does nothing except tell you that
    you can turn it on in the game's options menu."""
    display_name = "Death Link"
    default = "wow, thanks gramma"

class MusicRando(Choice):
    """Shuffles all the game's music tracks. Multiple music tracks that aren't used anywhere in the base
    game are included, so you'll get to listen to all sorts of new stuff!
    Shuffled = Shuffles the music once.
    Chaos = Shuffles the music every time music plays."""
    option_false = 0
    option_shuffled = 1
    option_chaos = 2
    option_alias_true = 1
    default = 0

class AngelEggHunt(Toggle):
    """Turns Angel Eggs into MacGuffins! In addition to anything else, you will need to collect Angel
    Eggs to unlock the endgame."""
    default = False

class AngelEggHuntCountNeeded(Range):
    """How many Angel Eggs are needed in order to fullfill the Angel Egg Hunt? This option does nothing
    if Angel Egg Hunt is not enabled."""
    range_start = 1
    range_end = 28
    default = 14

class AngelEggsInPool(Range):
    """How many Angel Eggs are in the item pool? If this number is lower than Angel Eggs Needed and 
    Angel Egg Hunt is on, this number will be brought up to match it automatically. Angel Eggs do 
    nothing if Angel Egg Hunt is not enabled, but you can still add them to the pool if you want."""
    range_start = 0
    range_end = 28
    default = 28

class NakedGrandma(Toggle):
    """Removes all costumes from the pool and replaces them with traps."""

@dataclass
class BabushkaOptions(PerGameCommonOptions):
    death_link: DeathLink
    music_rando: MusicRando
    angel_egg_hunt: AngelEggHunt
    angel_eggs_needed: AngelEggHuntCountNeeded
    angel_eggs_in_pool: AngelEggsInPool
    naked_grandma: NakedGrandma