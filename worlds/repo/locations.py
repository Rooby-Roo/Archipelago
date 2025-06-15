from typing import Dict, List, NamedTuple, Set, Optional
from BaseClasses import Location

from .names import location_names as lname, region_names as rname
from .options import REPOGameOptions

class REPOLocation(Location):
    game: str = "R.E.P.O"

location_base_id: int = 75912022

class REPOLocationData(NamedTuple):
    region: str
    location_id_offset: int
    location_group: Optional[str] = None


level_types = ["Swiftbroom Academy ","Headman Manor ","McJannek Station ","Museum of Human Art "]
pelly_types = [lname.standard_pelly,lname.glass_pelly,lname.gold_pelly]

v = 200 # Valuable Base ID
e = 500 # Monster Base ID
location_table: Dict[str, REPOLocationData] = { 
    # ---- Shop Upgrade Purchases ----
    # Reserved 1 - 100 for shop
    # lname.upgrade_pur + " 1": REPOLocationData(rname.shop,1,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 2": REPOLocationData(rname.shop,2,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 3": REPOLocationData(rname.shop,3,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 4": REPOLocationData(rname.shop,4,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 5": REPOLocationData(rname.shop,5,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 6": REPOLocationData(rname.shop,6,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 7": REPOLocationData(rname.shop,7,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 8": REPOLocationData(rname.shop,8,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 9": REPOLocationData(rname.shop,9,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 10": REPOLocationData(rname.shop,10,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 11": REPOLocationData(rname.shop,11,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 12": REPOLocationData(rname.shop,12,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 13": REPOLocationData(rname.shop,13,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 14": REPOLocationData(rname.shop,14,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 15": REPOLocationData(rname.shop,15,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 16": REPOLocationData(rname.shop,16,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 17": REPOLocationData(rname.shop,17,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 18": REPOLocationData(rname.shop,18,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 19": REPOLocationData(rname.shop,19,"Shop Upgrade Purchase"),
    # lname.upgrade_pur + " 20": REPOLocationData(rname.shop,20,"Shop Upgrade Purchase"),

    # ---- Pellys ----
    # -- Swiftbroom --
    level_types[0] + lname.standard_pelly: REPOLocationData(rname.swiftbroom,101,"Standard Pelly"),
    level_types[0] + lname.glass_pelly:    REPOLocationData(rname.swiftbroom,102,"Glass Pelly"),
    level_types[0] + lname.gold_pelly:     REPOLocationData(rname.swiftbroom,103,"Gold Pelly"),

    # -- Headman --
    level_types[1] + lname.standard_pelly: REPOLocationData(rname.headman,104,"Standard Pelly"),
    level_types[1] + lname.glass_pelly:    REPOLocationData(rname.headman,105,"Glass Pelly"),
    level_types[1] + lname.gold_pelly:     REPOLocationData(rname.headman,106,"Gold Pelly"),

    # -- McJannek --
    level_types[2] + lname.standard_pelly: REPOLocationData(rname.mcjannek,107,"Standard Pelly"),
    level_types[2] + lname.glass_pelly:    REPOLocationData(rname.mcjannek,108,"Glass Pelly"),
    level_types[2] + lname.gold_pelly:     REPOLocationData(rname.mcjannek,109,"Gold Pelly"),

    # -- Museum --
    level_types[3] + lname.standard_pelly: REPOLocationData(rname.museum,110,"Standard Pelly"),
    level_types[3] + lname.glass_pelly:    REPOLocationData(rname.museum,111,"Glass Pelly"),
    level_types[3] + lname.gold_pelly:     REPOLocationData(rname.museum,112,"Gold Pelly"),

    # ---- Valuables ----
    # -- All --
    lname.diamond:       REPOLocationData(rname.menu,v,       "Light Valuable"),
    lname.ring:          REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.goblet:        REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.ocarina:       REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.pocket_watch:  REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.uranium_mug:   REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.crown:         REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.doll:          REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.frog_toy:      REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.gem_box:       REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.globe:         REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.money:         REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.monkey:        REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.uranium_plate: REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.small_vase:    REPOLocationData(rname.menu,(v:=v+1),"Light Valuable"),
    lname.champagne:     REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.clown_doll:    REPOLocationData(rname.menu,(v:=v+1),"Medium+ Valuable"),
    lname.trophy:        REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.vase:          REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),
    lname.large_vase:    REPOLocationData(rname.menu,(v:=v+1),"Heavy Valuable"),
    lname.animal_crate:  REPOLocationData(rname.menu,(v:=v+1),"Heavy Valuable"),
    lname.bonsai:        REPOLocationData(rname.menu,(v:=v+1),"Medium Valuable"),

    # -- Headman Manor --
    lname.music_box:         REPOLocationData(rname.headman,(v:=v+1),"Medium Valuable"),
    lname.gramophone:        REPOLocationData(rname.headman,(v:=v+1),"Medium+ Valuable"),
    lname.rhino:             REPOLocationData(rname.headman,(v:=v+1),"Medium++ Valuable"),
    lname.scream_doll:       REPOLocationData(rname.headman,(v:=v+1),"Medium+ Valuable"),
    lname.grand_piano:       REPOLocationData(rname.headman,(v:=v+1),"VeryHeavy Valuable"),
    lname.harp:              REPOLocationData(rname.headman,(v:=v+1),"Heavy Valuable"),
    lname.painting:          REPOLocationData(rname.headman,(v:=v+1),"Heavy Valuable"),
    lname.grandfather_clock: REPOLocationData(rname.headman,(v:=v+1),"Heavy+ Valuable"),
    lname.dinosaur_skeleton: REPOLocationData(rname.headman,(v:=v+1),"Heavy Valuable"),
    lname.golden_statue:     REPOLocationData(rname.headman,(v:=v+1),"Heavy Valuable"),
    lname.tv:                REPOLocationData(rname.headman,(v:=v+1),"Heavy Valuable"),
    lname.radio:             REPOLocationData(rname.headman,(v:=v+1),"Medium++ Valuable"),
    lname.ship_in_a_bottle:  REPOLocationData(rname.headman,(v:=v+1),"Medium Valuable"),

    # -- McJannek Station --
    lname.desktop_computer:  REPOLocationData(rname.mcjannek,(v:=v+1),"Medium+ Valuable"),
    lname.fan:               REPOLocationData(rname.mcjannek,(v:=v+1),"Medium Valuable"),
    lname.explosive_barrel:  REPOLocationData(rname.mcjannek,(v:=v+1),"Heavy Valuable"),
    lname.sample:            REPOLocationData(rname.mcjannek,(v:=v+1),"Medium Valuable"),
    lname.big_sample:        REPOLocationData(rname.mcjannek,(v:=v+1),"Medium Valuable"),
    lname.flamethrower:      REPOLocationData(rname.mcjannek,(v:=v+1),"Heavy Valuable"),
    lname.science_station:   REPOLocationData(rname.mcjannek,(v:=v+1),"Heavy+ Valuable"),
    lname.server:            REPOLocationData(rname.mcjannek,(v:=v+1),"Heavy+ Valuable"),
    lname.printer:           REPOLocationData(rname.mcjannek,(v:=v+1),"Medium++ Valuable"),
    lname.hdd:               REPOLocationData(rname.mcjannek,(v:=v+1),"Medium+ Valuable"),
    lname.ice_saw:           REPOLocationData(rname.mcjannek,(v:=v+1),"Medium Valuable"),
    lname.laptop:            REPOLocationData(rname.mcjannek,(v:=v+1),"Medium Valuable"),
    lname.propane:           REPOLocationData(rname.mcjannek,(v:=v+1),"Medium+ Valuable"),
    lname.sample_pack:       REPOLocationData(rname.mcjannek,(v:=v+1),"Medium+ Valuable"),
    lname.guitar:            REPOLocationData(rname.mcjannek,(v:=v+1),"Medium++ Valuable"),
    lname.sample_cooler:     REPOLocationData(rname.mcjannek,(v:=v+1),"Medium++ Valuable"),
    lname.leg_ice:           REPOLocationData(rname.mcjannek,(v:=v+1),"Heavy+ Valuable"),
    lname.skeleton_ice:      REPOLocationData(rname.mcjannek,(v:=v+1),"Heavy+ Valuable"),

    # -- Swiftbroom Academy --
    lname.chomp_book:        REPOLocationData(rname.swiftbroom,(v:=v+1),"Light Valuable"),
    lname.love_potion:       REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium Valuable"),
    lname.cube_of_knowledge: REPOLocationData(rname.swiftbroom,(v:=v+1),"Heavy++ Valuable"),
    lname.staff:             REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium+++ Valuable"),
    lname.large_sword:       REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium++ Valuable"),
    lname.broom:             REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium+++ Valuable"),
    lname.hourglass:         REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium Valuable"),
    lname.master_potion:     REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium++ Valuable"),
    lname.goblin_head:       REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium++ Valuable"),
    lname.griffin:           REPOLocationData(rname.swiftbroom,(v:=v+1),"VeryHeavy Valuable"),
    lname.power_crystal:     REPOLocationData(rname.swiftbroom,(v:=v+1),"Medium Valuable"),

    # -- Museum of Human Art --
    lname.egg:           REPOLocationData(rname.museum,(v:=v+1),"Medium+++ Valuable"),
    lname.car:           REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.banana_bow:    REPOLocationData(rname.museum,(v:=v+1),"Light++ Valuable"),
    lname.boombox:       REPOLocationData(rname.museum,(v:=v+1),"Medium Valuable"),
    lname.cool_brain:    REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.cubic_tower:   REPOLocationData(rname.museum,(v:=v+1),"Light+ Valuable"),
    lname.fish:          REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.silverfish:    REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.goldfish:      REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.golden_swirl:  REPOLocationData(rname.museum,(v:=v+1),"VeryHeavy Valuable"),
    lname.pacifier:      REPOLocationData(rname.museum,(v:=v+1),"Medium+++ Valuable"),
    lname.baby_head:     REPOLocationData(rname.museum,(v:=v+1),"Medium+++ Valuable"),
    lname.monkeybox:     REPOLocationData(rname.museum,(v:=v+1),"Medium++ Valuable"),
    lname.flesh_blob:    REPOLocationData(rname.museum,(v:=v+1),"Medium Valuable"),
    lname.tooth:         REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.goldtooth:     REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.toast:         REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.horse:         REPOLocationData(rname.museum,(v:=v+1),"VeryHeavy Valuable"),
    lname.blender:       REPOLocationData(rname.museum,(v:=v+1),"Medium+++ Valuable"),
    lname.mug_deluxe:    REPOLocationData(rname.museum,(v:=v+1),"Medium++++ Valuable"),
    lname.gumball:       REPOLocationData(rname.museum,(v:=v+1),"Medium++ Valuable"),
    lname.traffic_light: REPOLocationData(rname.museum,(v:=v+1),"Heavy+ Valuable"),
    lname.milk:          REPOLocationData(rname.museum,(v:=v+1),"Heavy Valuable"),
    lname.handface:      REPOLocationData(rname.museum,(v:=v+1),"Medium+++ Valuable"),
    lname.gem_burger:    REPOLocationData(rname.museum,(v:=v+1),"Medium++++ Valuable"),
    lname.wire_figure:   REPOLocationData(rname.museum,(v:=v+1),"Light+ Valuable"),
    lname.rubendoll:     REPOLocationData(rname.museum,(v:=v+1),"Medium Valuable"),
    lname.duck_man:        REPOLocationData(rname.museum,(v:=v+1),"Light+ Valuable"),
    lname.cocktail:        REPOLocationData(rname.museum,(v:=v+1),"Light Valuable"),
    lname.cube_ball:       REPOLocationData(rname.museum,(v:=v+1),"Light+ Valuable"),
    lname.ladybug:         REPOLocationData(rname.museum,(v:=v+1),"Medium++ Valuable"),
    lname.cubic_sculpture: REPOLocationData(rname.museum,(v:=v+1),"Medium+++ Valuable"),

    # ---- Enemy Souls ----
    lname.animal_soul       : REPOLocationData(rname.menu,e,       "Monster Soul"),
    lname.duck_soul         : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.bowtie_soul       : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.chef_soul         : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.clown_soul        : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.headman_soul      : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.hidden_soul       : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.huntsman_soul     : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.mentalist_soul    : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.reaper_soul       : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.robe_soul         : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.rugrat_soul       : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.shadow_child_soul : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.spewer_soul       : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.trudge_soul       : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),
    lname.upscream_soul     : REPOLocationData(rname.menu,(e:=e+1),"Monster Soul"),

    # ---- Event Locations ----
    "Victory": REPOLocationData(rname.menu,None,"Event")

}

for i in range(100):
    location_table[lname.upgrade_pur + " " + str(i+1)] = REPOLocationData(rname.shop,i+1,"Shop Upgrade Purchase")

location_name_to_id: Dict[str, int] = {}

for name, data in location_table.items():
    if data.location_id_offset != None:
        location_name_to_id.update({name:data.location_id_offset + location_base_id})
    else:
        location_name_to_id.update({name:None})

def get_location_group(location_name: str) -> str:
    return location_table[location_name].location_group

event_locations: List[str] = [name for name, data in location_table.items() if data.location_group == "Event"]

temp_loc_total: int = 0

location_name_groups: Dict[str, Set[str]] = {}
pelly_list: list[REPOLocationData] = []

for loc_name, loc_data in location_table.items():
    if loc_data.location_id_offset != None:
        temp_loc_total += 1

    if loc_data.location_group:
        location_name_groups.setdefault(loc_data.location_group, set()).add(loc_name)

    if loc_name.__contains__("Pelly"):
        pelly_list.append(loc_name)

location_total: int = temp_loc_total