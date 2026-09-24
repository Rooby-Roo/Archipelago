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

@dataclass
class BabushkaOptions(PerGameCommonOptions):
    death_link: DeathLink
    music_rando: MusicRando