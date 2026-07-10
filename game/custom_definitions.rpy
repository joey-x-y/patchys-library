define sp = "audio/sfx/"
define ap = "audio/bgm/"
define bp = "images/backgrounds/"

# BGM __________

define bgm_duel = ap + "duel.ogg"
define bgm_ending = ap + "ending.ogg"
define bgm_forest = "<volume 0.5>" + ap + "forest.ogg"
define bgm_emotional = ap + "library_emotional.ogg"
define bgm_library = ap + "library.ogg"
define bgm_title = ap + "title.ogg"

# SFX __________

# define sfx_footstep_metal = "<from 0 to 1.7>" + sp + "Footsteps Metal 2.ogg"
define sfx_body_fall = sp + "body_fall.ogg"
define sfx_coffin_close = sp + "coffin_close.ogg"
define sfx_coffin_open = sp + "coffin_open.ogg"
define sfx_crystals_clacking = sp + "crystals_clacking.ogg"
define sfx_door_close = sp + "door_close.ogg"
define sfx_door_open = sp + "door_open.ogg"
define sfx_forest_land = "<from 0 to 0.5>" + sp + "forest_footsteps.ogg"
define sfx_forest_footsteps = "<volume 0.5>" + sp + "forest_footsteps.ogg"
define sfx_magic_cast = sp + "magic_cast.ogg" # summon gungnir or lavaiten
define sfx_magic_clash_1 = sp + "magic_clash_1.ogg"
define sfx_magic_clash_2 = sp + "magic_clash_2.ogg" # sneak attack collision
define sfx_magic_summon = sp + "magic_summon.ogg" # patchy generic magic
define sfx_magic_thunderous = sp + "magic_thunderous.ogg" # lazer gungnir collisions
define sfx_rustle_1 = sp + "rustle_1.ogg"
define sfx_rustle_2 = sp + "rustle_2.ogg"
define sfx_rustle_3 = sp + "rustle_3.ogg"
define sfx_stomach_growling = sp + "stomach_growling.ogg"
define sfx_woosh = sp + "woosh.ogg"

# BGs __________

transform bg_scale:
    fit "contain"
    xysize (1920, 1080)

image bg_study = At(bp + "library.png", bg_scale)
image bg_library = At(bp + "entrance.png", bg_scale)

