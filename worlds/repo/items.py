from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification, Item

from .names import item_names as iname

class REPOItem(Item):
    game: str = "R.E.P.O"

item_base_id: int = 75912022

class REPOItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


# a lot of quantities here will need to be adjusted later
item_table: Dict[str, REPOItemData] = {
    
    # ---- LEVELS ----
    #0-9 Reserved for Levels
    iname.swiftbroom_lvl: REPOItemData(ItemClassification.progression,1,0,"Level"),
    iname.headman_lvl: REPOItemData(ItemClassification.progression,1,1,"Level"),
    iname.mcjannek_lvl: REPOItemData(ItemClassification.progression,1,2,"Level"),
    iname.museum_lvl: REPOItemData(ItemClassification.progression,1,3,"Level"),

    # ---- UPGRADES ----
    iname.health_up: REPOItemData(ItemClassification.filler,1,10,"Upgrades"),
    iname.strength_up: REPOItemData(ItemClassification.progression,3,11,"Upgrades"),
    iname.range_up: REPOItemData(ItemClassification.filler,1,12,"Upgrades"),
    iname.sprint_up: REPOItemData(ItemClassification.filler,1,13,"Upgrades"),
    iname.stamina_up: REPOItemData(ItemClassification.filler,1,14,"Upgrades"),
    iname.player_count_up: REPOItemData(ItemClassification.filler,1,15,"Upgrades"),
    iname.double_jump_up: REPOItemData(ItemClassification.filler,1,16,"Upgrades"),
    iname.tumble_up: REPOItemData(ItemClassification.filler,1,17,"Upgrades"),
    iname.crouch_rest: REPOItemData(ItemClassification.filler,1,18,"Upgrades"),
    iname.tumble_wings: REPOItemData(ItemClassification.filler,1,19,"Upgrades"),

    # ---- AP Function Items ----
    iname.shop_stock: REPOItemData(ItemClassification.progression,0,20,"Progressive Shop"),

    # ---- Event Items ----
    "Victory": REPOItemData(ItemClassification.progression,0,None,"Event"),
}

item_name_to_id: Dict[str, int] ={}#= {name: combine_item_id(data) for name, data in item_table.items()}

for name, data in item_table.items():
    if data.item_id_offset != None:
        item_name_to_id.update({name:data.item_id_offset + item_base_id})
    else:
        item_name_to_id.update({name:None})
        

def get_item_group(item_name: str) -> str:
    return item_table[item_name].item_group

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]

trap_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.trap]
event_items: List[str] = [name for name, data in item_table.items() if data.item_group == "Event"]

item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

#item_limited_group = [iname.umami_training1,iname.umami_training2,iname.umami_training3,iname.googly_eye,iname.used_bandage]