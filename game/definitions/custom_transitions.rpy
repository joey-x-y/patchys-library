define config.layers = [
    "background",
    "rear_sprites",
    "master",
    "effects",
    "transient",
    "screens",
    "overlay",
]

define forest_walk_fade = Fade(0.75, 0.6, 0.75)

label show_transition_fade(bg):
    show expression bg onlayer background
    with fade
    return

label scene_transition_fade(bg):
    # Clear scene-specific layers
    scene onlayer rear_sprites
    scene onlayer master

    # Show the new background
    scene expression bg onlayer background

    with fade
    return

label day_transition_in:
    scene black onlayer background
    pause 1.0
    scene bg_bedroom onlayer background with fade
    hide black onlayer background
    return

label table_zoom_l:
    show layer master at table_zoom
    show layer rear_sprites at table_zoom
    show layer backgrounds at table_zoom
    return

label table_unzoom_l:
    show layer master at table_unzoom
    show layer rear_sprites at table_unzoom
    show layer backgrounds at table_unzoom
    return

transform table_zoom:
    ease 1.0 zoom 1.3 pos (-0.3, -0.2)

transform table_unzoom:
    zoom 1.3 pos (-0.3, -0.2)
    ease 1.0 zoom 1.0 pos (0.0, 0.0)

transform camera_revert:
    zoom 1.0 pos (0.0, 0.0)

label dim_screen:
    show black_2 onlayer background:
        alpha 0.5

    show black:
        alpha 0.2

    with dissolve
    return

label dim_screen_half:
    show black_2 onlayer background:
        alpha 0.25

    show black:
        alpha 0.1

    with dissolve
    return
    
label dim_screen_revert:
    hide black onlayer background
    hide black_2
    with dissolve
    return