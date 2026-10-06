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

    number_of_items = len(itempool)
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
    if world.options.start_with_one_confetti_cannon:
        # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        starting_confetti_cannon = world.create_item("Confetti Cannon")
        world.push_precollected(starting_confetti_cannon)
