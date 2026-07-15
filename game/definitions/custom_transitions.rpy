define forest_walk_fade = Fade(0.75, 0.6, 0.75)

label scene_transition_fade(bg):
    scene expression bg
    with fade
    return

label day_transition_in:
    scene black
    pause 1.0
    scene bg_bedroom with fade
    return

transform table_zoom:
    ease 1.0 zoom 1.3 pos (-0.3, -0.2)

transform table_unzoom:
    zoom 1.3 pos (-0.3, -0.2)
    ease 1.0 zoom 1.0 pos (0.0, 0.0)

transform camera_revert:
    zoom 1.0 pos (0.0, 0.0)


