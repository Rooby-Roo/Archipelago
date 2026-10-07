from enum import StrEnum

class ItemNames(StrEnum):
    # spells
    feather_fall = "Feather Fall"
    air_walk = "Air Walk"
    ladder = "Ladder"
    ghost = "Ghost"

    # memories
    cricket_memory = "Cricket Memory"
    fish_memory = "Fish Memory"
    spore_memory = "Spore Memory"
    love = "Love"

    # key items
    angel_egg = "Angel Egg"
    flower_pot = "Flower Pot"
    fishing_rod = "Fishing Rod"
    cute_pet = "Cute Pet"

    # equip items
    map_item = "Map"
    warp = "????"
    broomerang = "Progressive Broomerang"
    time_keeper = "Time Keeper"

    elder = "Crystal Elder"
    elder_0 = "First Elder"
    elder_1 = "Cricket Elder"
    elder_2 = "Fish Elder"
    elder_3 = "Spore Elder"

    # outfits
    # this list is pulled from Steam discussion. TODO: Verify
    outfit_0 = "Babushka Head Scarf"
    outfit_1 = "Fish Hat"
    outfit_2 = "Locust Wings"
    outfit_3 = "Toadstool"
    outfit_4 = "Chicken Suit"
    outfit_5 = "Grub Face"
    outfit_6 = "Elder Mask"
    outfit_7 = "Witch Hat"
    outfit_8 = "Skull"
    outfit_9 = "Crone Hat"
    outfit_10 = "No Scarf"
    outfit_11 = "Cozy Winter Scarf"

    # Doors & Keys
    key = "Key"
    door_tutorial = "Tutorial Area Door"
    door_tadpole = "Tadpole Bog Question Block Room Door"
    door_tadpole_eye = "Tadpole Bog Eye Door"
    door_moldy_1 = "Moldy Spore Forest First Flip Spore Room Door"
    door_moldy_2 = "Moldy Spore Forest Glitched Slammer Room Door"
    door_moldy_eye = "Moldy Spore Forest Eye Door"
    door_cricket = "Cricket Caves Air Walk & Ladder Room Door"
    door_cricket_eye = "Cricket Caves Eye Door"
    door_tower_exterior = "Elder Tower Exterior Door"  # this is just the 4 elders door. idk if it's worth locking or not
    door_tower_inside = "Elder Tower Interior Door"

    # fillers
    forget_trap = "Forget Trap"
    shard_bundle = "50 Shards"

class LocationNames(StrEnum):
    # Timestamps from this video: https://www.youtube.com/watch?v=9I0yvxbZnnA
    # TODO: I've only listed things shown in the above video thus far. I also know I missed an angel egg somewhere.
    tutorial_left_key = "Basement: Feather Fall Key"  # Key (freestanding) # 3:12
    tutorial_right_key = "Basement: Air Walk Chest"  # Key (in chest) # 5:24
    tutorial_left_key_chest = "Basement: Chest by Feather Fall Key"  # ???? (in chest) # 3:14
    tutorial_cat_chest = "Basement: Cat Room Chest" # Grimoire (in chest) # 8:30
    tutorial_cat_egg = "Basement: Cat Room Angel Egg"  # Egg # 2:16:38
    tutorial_ghost_egg = "Basement: Ghost Angel Egg"  # Egg # 10:54
    tutorial_outside_chest = "Above Basement: Chest"  # Chest, but was already open in video? May be outfit? # 2:14:02
    tutorial_snowman_chest = "Above Farm: Chest"  # cozy winter scarf # 2:15:22

    haven_purchase_1 = "Haven: Buy Broomerang"  # Broomerang (from purchase) # 15:12
    haven_purchase_2 = "Haven: Buy Broomerang 2"  # Broomerang (from purchase)
    haven_chest = "Haven: Chest"  # Map (in chest) # 14:04
    anywhere_time_keeper = "Outside Boss Room: Buy Time Keeper"  # Time Keeper (from purchase)  # Can be anywhere???

    moldy_entrance_egg = "Moldy Spore Forest First Room: Egg"  # Egg # 14:43
    moldy_big_guy_egg = "Moldy Spore Forest Big Guy Room: Egg"  # Egg # 39:40
    moldy_first_flip_spore_key = "Moldy Spore Forest First Flip Spore Room: Key"  # Key (freestanding) # 39:56
    moldy_second_flip_spore_egg = "Moldy Spore Forest Second Flip Spore Room: Egg"  # Egg # 2:20:01
    moldy_door_maze_egg = "Moldy Spore Forest Door Maze: Egg"  # Egg # 2:21:25
    moldy_mimic_purchase = "Moldy Spore Forest Door Maze: Buy Cute Pet"  # Cute Pet (from purchase) # 41:55
    moldy_ghost_egg_bottom = "Moldy Spore Forest Ghost Alley: Egg under glitches"  # Egg # 51:43
    moldy_ghost_egg_left = "Moldy Spore Forest Ghost Alley: Egg in wraparound"  # Egg # 56:34
    moldy_glitched_slammer_key_1 = "Moldy Spore Forest Glitched Slammer Room: Top Left Key"  # Key (freestanding)  # 45:44
    moldy_glitched_slammer_key_2 = "Moldy Spore Forest Glitched Slammer Room: Top Right Key"  # Key (freestanding)  # 46:15
    moldy_glitched_slammer_key_3 = "Moldy Spore Forest Glitched Slammer Room: Bottom Left Key"  # Key (freestanding)  # 46:00
    moldy_glitched_slammer_key_4 = "Moldy Spore Forest Glitched Slammer Room: Bottom Right Key"  # Key (freestanding)  # 46:20
    moldy_slammer_corridor_egg = "Moldy Spore Forest Slammer Corridor: Egg"  # Egg # 2:23:27
    moldy_mushroom_stair_egg = "Moldy Spore Forest Mushroom Stairs: Egg"  # Egg # 48:21
    moldy_blind_room = "Moldy Spore Forest Blind Triplets Room: Chest"  # Toadstool Outfit (in chest)
    moldy_eye_door = "Moldy Spore Forest Boss Lobby: Eye Door"  # Eye Doors?
    moldy_boss_elder = "Moldy Spore Forest Boss Room: Baba Yaga's House's Crystal Elder"  # Elder # 1:00:37
    moldy_boss_love = "Moldy Spore Forest Boss Room: Baba Yaga's House's Love"  # Elder # 1:00:46
    moldy_boss_memory = "Moldy Spore Forest Boss Room: Trade Cute Pet"  # Spore Memory 1:02:43

    tadpole_entrance_egg = "Tadpole Bog First Room: Egg"  # Egg # 36:27
    tadpole_secret_egg = 'Tadpole Bog "Secret to Everybody" Room: Egg' # Egg # 35:50 
    tadpole_big_guy_chest = "Tadpole Bog Big Guy Room: Chest"  # Fish Hat Outfit (in chest) # 16:44
    tadpole_big_guy_egg = "Tadpole Bog Big Guy Room: Egg"  # Egg # 1:48:15
    tadpole_question_egg_left = "Tadpole Bog Question Block Room: Egg at top of waterfall"  # Egg # 37:06
    tadpole_question_egg_right = "Tadpole Bog Question Block Room: Egg underground"  # Egg # 1:51:00
    tadpole_question_key = "Tadpole Bog Question Block Room: Key"  # Key (freestanding) # 20:13
    tadpole_mimic_purchase = "Tadpole Bog Mimic Room: Buy Fishing Rod"  # Fishing Rod (from purchase) # 21:08 # Mimic room diverts from question block room. above the waterfall.
    tadpole_air_walk_frog_egg = "Tadpole Bog Air Walk Frog Room: Egg"  # Egg # 24:52
    # TODO: There's a door off of Air Walk Frog Room! Left and then up 
    tadpole_bubble_column_egg = "Tadpole Bog Bubble Column Room: Egg"  # Egg # 1:51:59
    tadpole_catfishing_egg = "Tadpole Catfishing Room: Egg"  # Egg # 1:55:07
    tadpole_eye_door = "Tadpole Bog Boss Lobby: Eye Door"  # Eye Doors? Will we shuffle this?
    tadpole_boss_elder = "Tadpole Bog Boss Room: The Warty Seadevil's Crystal Elder"  # Elder # 34:06
    tadpole_boss_love = "Tadpole Bog Boss Room: The Warty Seadevil's Love"  # Love # 34:14
    tadpole_boss_memory = "Tadpole Bog Boss Room: Trade Fishing Pole"  # Fish Memory # 34:49

    cricket_entrance_egg = "Cricket Caves First Room: Egg"  # Egg # 1:55:59
    cricket_square_stair_egg_lower = "Cricket Caves Square Stair Room: Egg above"  # Egg # 2:06:47
    cricket_square_stair_egg_upper = "Cricket Caves Square Stair Room: Egg in sandpit"  # Egg # 2:04:26
    cricket_mimic_purchase = "Cricket Caves Mimic Room: Buy Flower Pot"  # Flower Pot (from purchase) # 1:59:45
    cricket_mimic_egg = "Cricket Caves Mimic Room: Egg"  # Egg # 2:10:16
    cricket_airwalk_and_ladder_chest = "Cricket Caves Air Walk & Ladder Room: Chest"  # locust wings outfit # 2:02:09
    cricket_airwalk_and_ladder_egg = "Cricket Caves Air Walk & Ladder Room: Egg"  # Egg # 2:08:48
    cricket_key_hole_egg = "Cricket Caves Key Hole: Egg"  # Egg # Room name shared with room on the right # 2:02:25
    cricket_key_hole_key = "Cricket Caves Key Hole: Key"  # Key (freestanding) # 1:08:05
    cricket_worms_egg = "Cricket Caves 4 Worms Room: Egg"  # Egg # 2:03:46
    cricket_worms_key = "Cricket Caves 4 Worms Room: Key"  # Key (freestanding)  # 1:10:18
    cricket_boulderfall_egg = "Cricket Caves Boulderfall Room: Egg"
    cricket_eye_door = "Cricket Caves Boss Lobby: Eye Door"  # Eye Doors?
    cricket_boss_elder = "Cricket Caves Boss Room: The Vessel of Souls' Crystal Elder"  # Elder # 1:18:05
    cricket_boss_love = "Cricket Caves Boss Room: The Vessel of Souls' Love"  # Love # 1:18:10
    cricket_boss_memory = "Cricket Caves Boss Room: Trade Flower Pot"  # cricket memory # 2:00:48

    tower_elder = "Elder Tower Exterior: Crystal Elder"  # Elder # 12:35
    tower_climb_chest = "Elder Tower Climb: Chest"  # Grimoire upgrade # 1:21:00
    tower_key_door_chest = "Elder Tower Key Door Room: Chest"  # Grub face outfit # 1:23:47
    tower_key_door_egg_bottom = "Elder Tower Key Door Room: Egg underground"  # Egg # 1:42:08
    tower_key_door_egg_bottom = "Elder Tower Key Door Room: Egg above"  # Egg # 2:24:30
    tower_horse_key = "Elder Tower Horse Room: Key"  # Key (freestanding) # 1:25:52
    tower_clones_key = "Elder Tower Clone Alley: Key"  # Key (freestanding) # 1:27:44

    ooze_exit_chest = "Primordial Ooze Escape: Chest"  # elder mask outfit # 1:34:26
    ooze_credits_chest_1 = "Primordial Ooze Credits Room: Lower Chest"  # witch hat outfit # 1:35:10
    ooze_credits_chest_2 = "Primordial Ooze Credits Room: Upper Chest"  # skull outfit # 1:39:49