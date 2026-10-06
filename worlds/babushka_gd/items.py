from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

from names import ItemNames as i

if TYPE_CHECKING:
    from .__init__ import BabushkaWorld

ITEM_NAME_TO_ID = {
    # Spells
    i.feather_fall: 100,
    i.air_walk: 101,
    i.ladder: 102,
    i.ghost: 103,

    # Memories
    i.fish_memory: 200,
    i.cricket_memory: 201,
    i.spore_memory: 202,
    i.love: 203,

    # Collectibles
    i.angel_egg: 300,
    i.fishing_rod: 301,
    i.flower_pot: 302,
    i.cute_pet: 303,

    # Equipment
    i.broomerang: 400,
    i.map_item: 401,
    i.warp: 402,
    i.time_keeper: 403,

    # Elders
    i.elder_0: 500,
    i.elder_1: 501,
    i.elder_2: 502,
    i.elder_3: 503,

    # Hats
    i.outfit_0: 600,
    i.outfit_1: 601,
    i.outfit_2: 602,
    i.outfit_3: 603,
    i.outfit_4: 604,
    i.outfit_5: 605,
    i.outfit_6: 606,
    i.outfit_7: 607,
    i.outfit_8: 608,
    i.outfit_9: 609,
    i.outfit_10: 610,
    i.outfit_11: 611,

    # Other filler items
    i.forget_trap: 700,
    i.shard_bundle: 701
}

DEFAULT_ITEM_CLASSIFICATIONS = {
    i.feather_fall: ItemClassification.progression | ItemClassification.useful,
    i.air_walk: ItemClassification.progression | ItemClassification.useful,
    i.ladder: ItemClassification.progression | ItemClassification.useful,
    i.ghost: ItemClassification.progression | ItemClassification.useful,
    i.fish_memory: ItemClassification.progression | ItemClassification.useful,
    i.cricket_memory: ItemClassification.progression | ItemClassification.useful,
    i.spore_memory: ItemClassification.progression | ItemClassification.useful,
    i.love: ItemClassification.useful,
    i.angel_egg: ItemClassification.filler,
    i.fishing_rod: ItemClassification.progression,
    i.flower_pot: ItemClassification.progression,
    i.cute_pet: ItemClassification.progression,
    i.broomerang: ItemClassification.useful,
    i.map_item: ItemClassification.filler,
    i.warp: ItemClassification.progression,
    i.time_keeper: ItemClassification.useful,
    i.elder_0: ItemClassification.progression,
    i.elder_1: ItemClassification.progression,
    i.elder_2: ItemClassification.progression,
    i.elder_3: ItemClassification.progression,
    i.outfit_0: ItemClassification.filler,
    i.outfit_1: ItemClassification.filler,
    i.outfit_2: ItemClassification.filler,
    i.outfit_3: ItemClassification.filler,
    i.outfit_4: ItemClassification.filler,
    i.outfit_5: ItemClassification.filler,
    i.outfit_6: ItemClassification.filler,
    i.outfit_7: ItemClassification.filler,
    i.outfit_8: ItemClassification.filler,
    i.outfit_9: ItemClassification.filler,
    i.outfit_10: ItemClassification.filler,
    i.outfit_11: ItemClassification.filler,
    i.forget_trap: ItemClassification.trap,
    i.shard_bundle: ItemClassification.filler


}

TRAPS = [name for (name, itemclass) in DEFAULT_ITEM_CLASSIFICATIONS.items() if itemclass == ItemClassification.trap]

OBTAINABLE_OUTFITS = [
    i.outfit_1, i.outfit_2, i.outfit_3, i.outfit_4, i.outfit_5, i.outfit_6,
    i.outfit_7, i.outfit_8, i.outfit_9, i.outfit_10, i.outfit_11
]

ALWAYS_CREATED_ITEMS = [
    i.feather_fall,
    i.air_walk,
    i.ladder,
    i.ghost,
    i.fish_memory,
    i.cricket_memory,
    i.spore_memory,
    i.love,
    i.love,
    i.love,
#   i.love, # TODO: Verify that there are in fact 4 of these? I never found a fourth but code suggests yes!
    i.fishing_rod,
    i.flower_pot,
    i.cute_pet,
    i.broomerang,
    i.broomerang,
    i.time_keeper,
    i.elder_0,
    i.elder_1,
    i.elder_2,
    i.elder_3,
]

class BabushkaItem(Item):
    game = "Babushka's Glitch Dungeon"

def create_item_with_class(world: BabushkaWorld, name: str, itemclass: ItemClassification|None = None) -> BabushkaItem: 

    classification = itemclass if itemclass else DEFAULT_ITEM_CLASSIFICATIONS[name]
    if world.options.angel_egg_hunt and name == i.angel_egg:
        classification = ItemClassification.progression

    return BabushkaItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: BabushkaWorld) -> None:

    itempool: list[Item] = []

    for name in ALWAYS_CREATED_ITEMS:
        itempool.append(world.create_item(name))

    if world.options.naked_grandma:
        for _ in range(11):
            itempool.append(world.create_item(world.random.choice(TRAPS)))
    else:
        for name in OBTAINABLE_OUTFITS:
            itempool.append(world.create_item(name))

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += itempool

