# image spear_core = Solid("#ffffff")
image spear_glow = Solid("#ff2040")
image lazer_charge_sun = Solid("#f9ffa1")
image lazer_charge_water = Solid("#0003be")
image impact_flash = Solid("#ffffff")

init python:
    renpy.add_layer("effects", above="master")

    def spear_block_impact():
        renpy.sound.play(sfx_magic_clash_2)
        remi.move(shake(magnitude=2))
        renpy.show("impact_flash", at_list=[flash()], layer="effects")

screen spear_block_barrage_timer(interval=2):
    # Fire once almost immediately.
    timer 0.01 action Function(spear_block_impact)

    # Then continue at the chosen interval.
    timer interval repeat True action Function(spear_block_impact)

label spear_block_quick(pause_time=0.2, x=0.3, y=0.35):
    show impact_flash onlayer effects at flash()
    pause pause_time
    return

label spear_block_continuous(x=0.3, y=0.35):
    show screen spear_block_barrage_timer()
    return

label spear_block_barrage_end():
    hide screen spear_block_barrage_timer
    return

label spear_lazer_clash(defender=remi):
    play sound sfx_magic_thunderous
    $ defender.effect(shake)
    show spear_glow onlayer effects at flash(time=0.1, alpha=0.3)
    show lazer_charge_sun onlayer effects at flash(time=0.1, alpha=0.2)
    show lazer_charge_water onlayer effects at flash(time=0.1, alpha=0.2)
    pause 0.2
    return

label spear_summon(flash_time=0.3, pause_time=0.2):
    show spear_glow onlayer effects at flash(time=flash_time, alpha=0.4)
    pause pause_time
    return

label lazer_charge(flash_time=0.3, pause_time=0.2):
    show lazer_charge_sun onlayer effects at flash(time=flash_time, alpha=0.3)
    pause pause_time
    show lazer_charge_water onlayer effects at flash(time=flash_time, alpha=0.3)
    pause pause_time
    return

label clear_effects:
    hide spear_glow onlayer effects
    hide lazer_charge_sun onlayer effects
    hide lazer_charge_water onlayer effects
    hide impact_flash onlayer effects
    return

label generic_spell:
    play sound sfx_magic_summon
    show impact_flash onlayer effects at flash(0.2, 0.1)
    pause 0.2
    hide impact_flash onlayer effects
    return

transform flash(time=0.1, alpha=0.25):
    alpha 0.0
    linear time/2 alpha alpha
    linear time/2 alpha 0.0

transform flash_continuous(time=0.1, alpha=0.25, interval=2):
    block:
        alpha 0.0
        linear time/2 alpha alpha
        linear time/2 alpha 0.0
        pause interval
        repeat

transform point_flash(
    x=0.62,
    y=0.35,
    size=80,
    time=0.2
):
    xpos x
    ypos y

    xanchor 0.5
    yanchor 0.5

    xysize (size, size)

    alpha 0.0
    zoom 0.2

    parallel:
        linear 0.02 alpha 1.0
        linear time alpha 0.0

    parallel:
        easeout time zoom 1.8

# transform energy_spear(
#     x=0.33,
#     y=0.56,
#     width=360,
#     thickness=3,
#     angle=-25,
#     max_alpha=1.0
# ):
#     xpos x
#     ypos y

#     xanchor 0.0
#     yanchor 0.5

#     xysize (width, thickness)
#     rotate angle

#     alpha max_alpha
#     xzoom 0.0

#     easeout 0.04 xzoom 1.08
#     easein 0.02 xzoom 1.0

#     pause 0.04
#     linear 0.08 alpha 0.0

# label spear_block(x=0.33, y=0.56):

#     show spear_glow onlayer effects at energy_spear(
#         x=x,
#         y=y,
#         width=370,
#         thickness=14,
#         angle=-25,
#         max_alpha=0.22
#     )

#     show spear_core onlayer effects at energy_spear(
#         x=x,
#         y=y,
#         width=360,
#         thickness=3,
#         angle=-25,
#         max_alpha=0.95
#     )

#     pause 0.18

#     hide spear_core onlayer effects
#     hide spear_glow onlayer effects

#     return
