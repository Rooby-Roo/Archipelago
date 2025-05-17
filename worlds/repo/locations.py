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


level_types = ["Swiftbroom Academy ","Headman Manor ","McJannek Station "]
pelly_types = [lname.standard_pelly,lname.glass_pelly,lname.gold_pelly]

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
    level_types[0] + lname.glass_pelly: REPOLocationData(rname.swiftbroom,102,"Glass Pelly"),
    level_types[0] + lname.gold_pelly: REPOLocationData(rname.swiftbroom,103,"Gold Pelly"),

    # -- Headman --
    level_types[1] + lname.standard_pelly: REPOLocationData(rname.headman,104,"Standard Pelly"),
    level_types[1] + lname.glass_pelly: REPOLocationData(rname.headman,105,"Glass Pelly"),
    level_types[1] + lname.gold_pelly: REPOLocationData(rname.headman,106,"Gold Pelly"),

    # -- McJannek --
    level_types[2] + lname.standard_pelly: REPOLocationData(rname.mcjannek,107,"Standard Pelly"),
    level_types[2] + lname.glass_pelly: REPOLocationData(rname.mcjannek,108,"Glass Pelly"),
    level_types[2] + lname.gold_pelly: REPOLocationData(rname.mcjannek,109,"Gold Pelly"),

    # ---- Valuables ----
    # -- All --
    lname.diamond: REPOLocationData(rname.menu,200,"Light Valuable"),
    lname.ring: REPOLocationData(rname.menu,201,"Light Valuable"),
    lname.goblet: REPOLocationData(rname.menu,202,"Light Valuable"),
    lname.ocarina: REPOLocationData(rname.menu,203,"Light Valuable"),
    lname.pocket_watch: REPOLocationData(rname.menu,204,"Light Valuable"),
    lname.uranium_mug: REPOLocationData(rname.menu,205,"Light Valuable"),
    lname.crown: REPOLocationData(rname.menu,206,"Light Valuable"),
    lname.doll: REPOLocationData(rname.menu,207,"Medium Valuable"),
    #lname.diamond: REPOLocationData(rname.menu,208,"Light Valuable"),
    lname.frog_toy: REPOLocationData(rname.menu,209,"Light Valuable"),
    lname.gem_box: REPOLocationData(rname.menu,210,"Medium Valuable"),
    lname.globe: REPOLocationData(rname.menu,211,"Medium Valuable"),
    lname.money: REPOLocationData(rname.menu,212,"Medium Valuable"),
    lname.monkey: REPOLocationData(rname.menu,213,"Medium Valuable"),
    lname.uranium_plate: REPOLocationData(rname.menu,214,"Light Valuable"),
    lname.small_vase: REPOLocationData(rname.menu,215,"Light Valuable"),
    lname.champagne: REPOLocationData(rname.menu,216,"Medium Valuable"),
    lname.clown_doll: REPOLocationData(rname.menu,217,"Medium+ Valuable"),
    lname.radio: REPOLocationData(rname.menu,218,"Medium++ Valuable"),
    lname.ship_in_a_bottle: REPOLocationData(rname.menu,219,"Medium Valuable"),
    lname.trophy: REPOLocationData(rname.menu,220,"Medium Valuable"),
    lname.vase: REPOLocationData(rname.menu,221,"Medium Valuable"),
    lname.tv: REPOLocationData(rname.menu,222,"Heavy Valuable"),
    lname.large_vase: REPOLocationData(rname.menu,223,"Heavy Valuable"),
    lname.animal_crate: REPOLocationData(rname.menu,224,"Heavy Valuable"),
    lname.bonsai: REPOLocationData(rname.menu,225,"Medium Valuable"),

    # -- Headman Manor --
    lname.music_box: REPOLocationData(rname.headman,226,"Medium Valuable"),
    lname.gramophone: REPOLocationData(rname.headman,227,"Medium+ Valuable"),
    lname.rhino: REPOLocationData(rname.headman,228,"Medium++ Valuable"),
    lname.scream_doll: REPOLocationData(rname.headman,229,"Medium+ Valuable"),
    lname.grand_piano: REPOLocationData(rname.headman,230,"VeryHeavy Valuable"),
    lname.harp: REPOLocationData(rname.headman,231,"Heavy Valuable"),
    lname.painting: REPOLocationData(rname.headman,232,"Heavy Valuable"),
    lname.grandfather_clock: REPOLocationData(rname.headman,233,"Heavy+ Valuable"),
    lname.dinosaur_skeleton: REPOLocationData(rname.headman,234,"Heavy Valuable"),
    lname.golden_statue: REPOLocationData(rname.headman,235,"Heavy Valuable"),

    # -- McJannek Station --
    lname.desktop_computer: REPOLocationData(rname.mcjannek,236,"Medium+ Valuable"),
    lname.fan: REPOLocationData(rname.mcjannek,237,"Medium Valuable"),
    lname.explosive_barrel: REPOLocationData(rname.mcjannek,208,"Heavy Valuable"),
    lname.sample: REPOLocationData(rname.mcjannek,238,"Medium Valuable"),
    lname.big_sample: REPOLocationData(rname.mcjannek,239,"Medium Valuable"),
    lname.flamethrower: REPOLocationData(rname.mcjannek,240,"Heavy Valuable"),
    lname.science_station: REPOLocationData(rname.mcjannek,241,"Heavy+ Valuable"),
    lname.server: REPOLocationData(rname.mcjannek,242,"Heavy+ Valuable"),
    lname.printer: REPOLocationData(rname.mcjannek,243,"Medium++ Valuable"),
    lname.hdd: REPOLocationData(rname.mcjannek,244,"Medium+ Valuable"),
    lname.ice_saw: REPOLocationData(rname.mcjannek,245,"Medium Valuable"),
    lname.laptop: REPOLocationData(rname.mcjannek,246,"Medium Valuable"),
    lname.propane: REPOLocationData(rname.mcjannek,247,"Medium+ Valuable"),
    lname.sample_pack: REPOLocationData(rname.mcjannek,248,"Medium+ Valuable"),
    lname.guitar: REPOLocationData(rname.mcjannek,249,"Medium++ Valuable"),
    lname.sample_cooler: REPOLocationData(rname.mcjannek,250,"Medium++ Valuable"),
    lname.leg_ice: REPOLocationData(rname.mcjannek,251,"Heavy+ Valuable"),
    lname.skeleton_ice: REPOLocationData(rname.mcjannek,252,"Heavy+ Valuable"),

    # -- Swiftbroom Academy --
    lname.chomp_book: REPOLocationData(rname.swiftbroom,253,"Light Valuable"),
    lname.love_potion: REPOLocationData(rname.swiftbroom,254,"Medium Valuable"),
    lname.cube_of_knowledge: REPOLocationData(rname.swiftbroom,255,"Heavy++ Valuable"),
    lname.staff: REPOLocationData(rname.swiftbroom,256,"Medium+++ Valuable"),
    lname.large_sword: REPOLocationData(rname.swiftbroom,257,"Medium++ Valuable"),
    lname.broom: REPOLocationData(rname.swiftbroom,258,"Medium+++ Valuable"),
    lname.hourglass: REPOLocationData(rname.swiftbroom,259,"Medium Valuable"),
    lname.master_potion: REPOLocationData(rname.swiftbroom,260,"Medium++ Valuable"),
    lname.goblin_head: REPOLocationData(rname.swiftbroom,261,"Medium++ Valuable"),
    lname.griffin: REPOLocationData(rname.swiftbroom,262,"VeryHeavy Valuable"),
    lname.power_crystal: REPOLocationData(rname.swiftbroom,263,"Medium Valuable"),

    # ---- Enemy Souls ----
    lname.animal_soul : REPOLocationData(rname.menu,300,"Monster Soul"),
    lname.duck_soul : REPOLocationData(rname.menu,301,"Monster Soul"),
    lname.bowtie_soul : REPOLocationData(rname.menu,302,"Monster Soul"),
    lname.chef_soul : REPOLocationData(rname.menu,303,"Monster Soul"),
    lname.clown_soul : REPOLocationData(rname.menu,304,"Monster Soul"),
    lname.headman_soul : REPOLocationData(rname.menu,305,"Monster Soul"),
    lname.hidden_soul : REPOLocationData(rname.menu,306,"Monster Soul"),
    lname.huntsman_soul : REPOLocationData(rname.menu,307,"Monster Soul"),
    lname.mentalist_soul : REPOLocationData(rname.menu,308,"Monster Soul"),
    lname.reaper_soul : REPOLocationData(rname.menu,309,"Monster Soul"),
    lname.robe_soul : REPOLocationData(rname.menu,310,"Monster Soul"),
    lname.rugrat_soul : REPOLocationData(rname.menu,311,"Monster Soul"),
    lname.shadow_child_soul : REPOLocationData(rname.menu,312,"Monster Soul"),
    lname.spewer_soul : REPOLocationData(rname.menu,313,"Monster Soul"),
    lname.trudge_soul : REPOLocationData(rname.menu,314,"Monster Soul"),
    lname.upscream_soul : REPOLocationData(rname.menu,315,"Monster Soul"),
    #Last Used 264

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