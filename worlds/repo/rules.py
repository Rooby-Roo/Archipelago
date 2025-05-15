import math
from typing import TYPE_CHECKING, Dict, List
from worlds.generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from BaseClasses import CollectionState

from .options import REPOGameOptions
from .names import location_names as lname
from .names import item_names as iname
from .names import region_names as rname
from .locations import level_types, location_table, pelly_list
from . import logic
#import logic

if TYPE_CHECKING:
    from . import REPOWorld

#forkless_easy_skills: List[str] = {

#}

#forkless_hard_skills: List[str] = {
  
#}



def set_region_rules(world: "REPOWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options
    
    # ---- Levels are locked behind Level Items ----
    multiworld.get_entrance(f"{rname.menu} -> {rname.headman}", player).access_rule = \
lambda state: state.has(iname.headman_lvl, player)
    
    multiworld.get_entrance(f"{rname.menu} -> {rname.mcjannek}", player).access_rule = \
lambda state: state.has(iname.mcjannek_lvl, player)
    
    multiworld.get_entrance(f"{rname.menu} -> {rname.swiftbroom}", player).access_rule = \
lambda state: state.has(iname.swiftbroom_lvl, player)
    
    

def set_location_rules(world: "REPOWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    #Set Completion Condition to Victory Event
    multiworld.completion_condition[player] = lambda state: state.has("Victory", player)

    #Set Logic for Victory Location
    #if options.goal == "pelly_hunt":
        #Player Should have access to all levels
    add_rule(multiworld.get_location("Victory",player),
        lambda state: state.has_all({iname.headman_lvl,iname.mcjannek_lvl,iname.swiftbroom_lvl},player))
    
    #Player Should be able to reach all Pellys
    for pelly in pelly_list:
        #Rules for Pelly by Location
        if (options.pelly_spawning == True or any(map(pelly.__contains__,options.pellys_required))):
            if (pelly.__contains__("Swiftbroom Academy")):
                print("SBA Pelly Added")
                set_rule(multiworld.get_location(pelly,player),
                    lambda state: state.can_reach(multiworld.get_region(rname.swiftbroom,player),player))
            if (pelly.__contains__("Headman Manor")):
                print("HM Pelly added")
                set_rule(multiworld.get_location(pelly,player),
                    lambda state: state.can_reach(multiworld.get_region(rname.headman,player),player))
            if (pelly.__contains__("McJannek Station")):
                print("McJ Pelly added")
                set_rule(multiworld.get_location(pelly,player),
                    lambda state: state.can_reach(multiworld.get_region(rname.mcjannek,player),player))
            
            #Rules for Pelly by Type
            if pelly.__contains__("Gold"):
                set_rule(multiworld.get_location(pelly,player),
                    lambda state: state.has(iname.strength_up,player,3))

        #Rules for Victory
        if (options.pelly_spawning == False and any(map(pelly.__contains__,options.pellys_required))):
            print(f"adding {pelly} rule to list")
            add_rule(multiworld.get_location("Victory",player),
                lambda state: state.can_reach(multiworld.get_location(pelly,player)))
        elif(options.pelly_spawning == True):
            print(f"adding {pelly} rule to list")
            add_rule(multiworld.get_location("Victory",player),
                lambda state: state.can_reach(multiworld.get_location(pelly,player)))
        
    # elif options.goal == "level_quota":
    #     set_rule(multiworld.get_location("Victory",player),
    #         lambda state: state.has(iname.strength_up,player,3))
        

    for loc_name in location_table:
        print(f"Shop Upgrade total: {int(options.shop_upgrade_total.value)}\n Location id: {location_table[loc_name].location_id_offset}")
        if location_table[loc_name].location_id_offset != None and location_table[loc_name].location_id_offset > int(options.shop_upgrade_total.value):
            continue

        if loc_name.__contains__(lname.upgrade_pur):
            stockItemsRequired = math.ceil( (location_table[loc_name].location_id_offset - options.shop_stock) / options.shop_stock)
            print(f"Adding rule for {loc_name} requiring {stockItemsRequired} stock")
            if stockItemsRequired > 0:
                set_rule(multiworld.get_location(loc_name,player),
                    lambda state: state.has(iname.shop_stock,player,stockItemsRequired))

    #set_rule(multiworld.get_location())


#logic.set_options(world.options)




  
