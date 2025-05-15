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