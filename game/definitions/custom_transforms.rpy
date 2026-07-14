transform sprite_facing(flipped=False):
    xzoom (-1.0 if flipped else 1.0)

transform standheight:
    ypos 1.0

transform left:
    xpos 0.3

transform far_left:
    xpos 0.2

transform corner_left:
    xpos 0.1

transform right:
    xpos 0.7

transform far_right:
    xpos 0.8

transform corner_right:
    xpos 0.9

transform center:
    xpos 0.5

transform center_left:
    xpos 0.4

transform center_right:
    xpos 0.6

transform scoot_left:
    ease 0.4 xoffset -30

transform scoot_right:
    ease 0.4 xoffset 30

transform unscoot:
    ease 0.4 xoffset 0

transform enterleft(speed=1):
    xoffset -800
    alpha 0

    ease speed xoffset 0 alpha 1

transform enterright(speed=1):
    xoffset 800
    alpha 0
    ease speed xoffset 0 alpha 1

transform enterbottom(speed=1):
    yoffset 800
    alpha 0
    ease speed yoffset 0 alpha 1

transform enterforcefinish():
    yoffset 0
    xoffset 0
    alpha 1

transform drophalf:
    ease 0.3 ypos 1.2

transform standup:
    ease 0.3 ypos 1.0

transform dropdown:
    ease 0.5 ypos 1.65

transform dropdowninstant:
    ypos 1.65

transform floatup:
    yoffset -50

transform floatdowntocenter:
    yoffset -50
    parallel:
        ease 1.0 yoffset 0
    parallel:
        ease 1.0 xpos 0.6

transform hop(height=60, length=0.15):
    ease length yoffset -height
    ease length yoffset 0

transform hopdown(height=60, length=0.15):
    ease length yoffset height
    ease length yoffset 0

transform hopreset():
    yoffset 0

define move_fast = MoveTransition(0.1)

define move_slow = MoveTransition(0.7, time_warp=_warper.ease)

define dissolve_fast = Dissolve(0.1)

transform small_shake(magnitude=3.0, length=0.5):
    ease length/4.0 xoffset -magnitude 
    ease length/2.0 xoffset magnitude
    ease length/4.0 xoffset 0

transform shake(magnitude=8, length=0.15):
    linear length/5.0 xoffset -magnitude yoffset -magnitude/1.5
    linear length/5.0 xoffset magnitude yoffset magnitude/1.5
    linear length/5.0 xoffset -magnitude/1.5 yoffset magnitude/2.0
    linear length/5.0 xoffset magnitude/1.5 yoffset -magnitude/2.0
    linear length/5.0 xoffset 0 yoffset 0