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

#Last used number - 59
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

    # ---- SHOP UNLOCKS ----
    iname.small_health: REPOItemData(ItemClassification.filler,1,21,"Health Pack"),
    iname.medium_health: REPOItemData(ItemClassification.filler,1,22,"Health Pack"),
    iname.large_health: REPOItemData(ItemClassification.filler,1,23,"Health Pack"),
    iname.progressive_health: REPOItemData(ItemClassification.filler,1,24,"Shop Unlock"),
    iname.baseball_bat: REPOItemData(ItemClassification.filler,1,25,"Melee Shop Unlock"),
    iname.frying_pan: REPOItemData(ItemClassification.filler,1,26,"Melee Shop Unlock"),
    iname.sledge_hammer: REPOItemData(ItemClassification.filler,1,27,"Melee Shop Unlock"),
    iname.sword: REPOItemData(ItemClassification.filler,1,28,"Melee Shop Unlock"),
    iname.inflatable_hammer: REPOItemData(ItemClassification.filler,1,29,"Melee Shop Unlock"),
    iname.prodzap: REPOItemData(ItemClassification.filler,1,30,"Melee Shop Unlock"),
    iname.gun: REPOItemData(ItemClassification.filler,1,31,"Ranged Shop Unlock"),
    iname.shotgun: REPOItemData(ItemClassification.filler,1,32,"Ranged Shop Unlock"),
    iname.tranq_gun: REPOItemData(ItemClassification.filler,1,33,"Ranged Shop Unlock"),
    iname.pulse_pistol: REPOItemData(ItemClassification.filler,1,34,"Ranged Shop Unlock"),
    iname.photon_blaster: REPOItemData(ItemClassification.filler,1,35,"Ranged Shop Unlock"),
    iname.boltzap: REPOItemData(ItemClassification.filler,1,36,"Ranged Shop Unlock"),
    iname.cart_cannon: REPOItemData(ItemClassification.filler,1,37,"Ranged Shop Unlock"),
    iname.cart_laser: REPOItemData(ItemClassification.filler,1,38,"Ranged Shop Unlock"),
    iname.grenade: REPOItemData(ItemClassification.filler,1,39,"Explosive Shop Unlock"),
    iname.shock_grenade: REPOItemData(ItemClassification.filler,1,40,"Explosive Shop Unlock"),
    iname.stun_grenade: REPOItemData(ItemClassification.filler,1,41,"Explosive Shop Unlock"),
    iname.duct_taped_grenade: REPOItemData(ItemClassification.filler,1,42,"Explosive Shop Unlock"),
    iname.shockwave_mine: REPOItemData(ItemClassification.filler,1,43,"Explosive Shop Unlock"),
    iname.stun_mine: REPOItemData(ItemClassification.filler,1,44,"Explosive Shop Unlock"),
    iname.explosive_mine: REPOItemData(ItemClassification.filler,1,45,"Explosive Shop Unlock"),
    iname.rubber_duck: REPOItemData(ItemClassification.filler,1,46,"Explosive Shop Unlock"),
    iname.recharge_drone: REPOItemData(ItemClassification.filler,1,47,"Drone Shop Unlock"),
    iname.indestructible_drone: REPOItemData(ItemClassification.filler,1,48,"Drone Shop Unlock"),
    iname.roll_drone: REPOItemData(ItemClassification.filler,1,49,"Drone Shop Unlock"),
    iname.feather_drone: REPOItemData(ItemClassification.filler,1,50,"Drone Shop Unlock"),
    iname.zero_grav_drone: REPOItemData(ItemClassification.filler,1,51,"Drone Shop Unlock"),
    iname.pocket_cart: REPOItemData(ItemClassification.filler,1,52,"Shop Unlock"),
    iname.cart: REPOItemData(ItemClassification.filler,1,53,"Shop Unlock"),
    iname.valuable_detector: REPOItemData(ItemClassification.filler,1,54,"Shop Unlock"),
    iname.extraction_detector: REPOItemData(ItemClassification.filler,1,55,"Shop Unlock"),
    iname.energy_crystal: REPOItemData(ItemClassification.filler,1,56,"Shop Unlock"),
    iname.zero_grav_orb: REPOItemData(ItemClassification.filler,1,57,"Shop Unlock"),
    iname.duck_bucket: REPOItemData(ItemClassification.filler,1,58,"Shop Unlock"),
    iname.phase_bridge: REPOItemData(ItemClassification.filler,1,59,"Shop Unlock"),

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