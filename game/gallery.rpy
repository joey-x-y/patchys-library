################################################################################
## GALLERY
##
## Background and CG entries contain a title, defined image name(s), and artist.
################################################################################

init python:

    GALLERY_CHARACTER_CONFIG = {
        "remilia": {
            "name": "Remilia",
            "sprite": "remi",
            "attributes": (
                ("expression", "Expression", REMI_EXPRESSIONS),
                ("dirty", "Dirty", (False, True)),
                ("accessories", "Accessories", (True, False)),
                ("hunt", "Hunt Outfit", (False, True)),
                ("blush", "Blushing", (False, True)),
            ),
        },
        "flandre": {
            "name": "Flandre",
            "sprite": "flan",
            "attributes": (
                ("expression", "Expression", FLAN_EXPRESSIONS),
                ("dirty", "Dirty", (False, True)),
                ("wings", "Wings", ("default", "mid", "gone", "crystal")),
                ("accessories", "Ribbon", (True, False)),
                ("blush", "Blush", (False, True)),
            ),
        },
        "patchouli": {
            "name": "Patchouli",
            "sprite": "pat",
            "attributes": (
                ("expression", "Expression", PAT_EXPRESSIONS),
                ("hat", "Hat", (True, False)),
                ("magic", "Magic Cast", (False, True)),
                ("blush", "Blushing", (False, True)),
            ),
        },
    }

    # Each entry is (title, image name, artist).
    # Image names reference images defined in custom_definitions.rpy.
    GALLERY_BACKGROUNDS = (
        ("Forest", "bg_forest", "Hiro Reverie"),
        ("Bedroom", "bg_bedroom", "camellia"),
        ("Patchouli's Study", "bg_study", "camellia"),
        ("Library Entrance", "bg_library", "camellia"),
    )

    # Each entry is (title, variants, artist). Add more image names to a
    # variants tuple to make them available with the arrows.
    GALLERY_CGS = (
        ("Vampire Kiss", ("cg_kiss_cry", "cg_kiss_gentle", "cg_hug", "cg_stare_cry", "cg_stare_gentle"), "Hiro Reverie"),
        ("Unsolicited Wing Touching", ("cg_wingtouch",), "numblr"),
        ("Title Screen", ("cg_title", "cg_title_completion"), "Hiro Reverie"),
    )

    def gallery_character_sprite(character):
        sprite_name = GALLERY_CHARACTER_CONFIG[character]["sprite"]
        return getattr(renpy.store, sprite_name)

    def gallery_reset_character(character):
        sprite = gallery_character_sprite(character)
        gallery_character_states[character] = sprite.defaults.copy()

    def gallery_cycle_character_attribute(character, attribute, direction):
        config = GALLERY_CHARACTER_CONFIG[character]
        values = next(
            item[2] for item in config["attributes"] if item[0] == attribute
        )
        current = gallery_character_states[character][attribute]
        index = values.index(current)
        gallery_character_states[character][attribute] = (
            values[(index + direction) % len(values)]
        )

    def gallery_character_image(character):
        sprite = gallery_character_sprite(character)
        return sprite._image_name(gallery_character_states[character])

    def gallery_value_label(value):
        if value is True:
            return "On"
        if value is False:
            return "Off"
        return str(value).replace("_", " ").title()

    def gallery_placeholder(text, size, color="#352842"):
        return Fixed(
            Solid(color, xysize=size),
            Text(
                text,
                color=gui.idle_small_color,
                size=30,
                xalign=0.5,
                yalign=0.5,
            ),
            xysize=size,
        )

    def gallery_asset(path, placeholder_text, size, color="#352842"):
        if path:
            return Transform(path, fit="cover", xysize=size)
        return gallery_placeholder(placeholder_text, size, color)


default gallery_character_states = {
    "remilia": {
        "expression": "neutral",
        "dirty": False,
        "accessories": True,
        "hunt": False,
        "blush": False,
    },
    "flandre": {
        "expression": "neutral",
        "dirty": False,
        "wings": "default",
        "accessories": True,
        "blush": False,
    },
    "patchouli": {
        "expression": "neutral",
        "hat": True,
        "magic": False,
    },
}


transform gallery_character_preview:
    xcenter 570
    yalign 1.0


transform gallery_thumbnail_hover:
    xalign 0.5
    yalign 0.5

    on hover:
        easein 0.15 zoom 1.05
    on idle:
        easein 0.15 zoom 1.0


screen gallery():
    tag menu

    add gui.main_menu_background
    add Solid("#09070dcc")

    text _("Gallery"):
        style "gallery_title"

    vbox:
        style "gallery_main_buttons"

        textbutton _("Remilia"):
            action [
                Function(gallery_reset_character, "remilia"),
                ShowMenu("character_gallery", character="remilia"),
            ]

        textbutton _("Flandre"):
            action [
                Function(gallery_reset_character, "flandre"),
                ShowMenu("character_gallery", character="flandre"),
            ]

        textbutton _("Patchouli"):
            action [
                Function(gallery_reset_character, "patchouli"),
                ShowMenu("character_gallery", character="patchouli"),
            ]

        textbutton _("Backgrounds") action ShowMenu("background_gallery")
        textbutton _("CGs") action ShowMenu("cg_gallery")

    textbutton _("Return"):
        style "gallery_back_button"
        action ShowMenu("main_menu")

    key "game_menu" action ShowMenu("main_menu")


screen character_gallery(character):
    tag menu

    $ config = GALLERY_CHARACTER_CONFIG[character]
    $ character_name = config["name"]
    $ state = gallery_character_states[character]
    $ sprite_image = gallery_character_image(character)

    add gui.main_menu_background
    add Solid("#09070dcc")

    text _("[character_name]"):
        style "gallery_title"

    if character == "flandre":
        add sprite_image:
            at gallery_character_preview
            xzoom -1
            yoffset -80

    elif character == "patchouli":
        add sprite_image:
            at gallery_character_preview
            yoffset -60

    elif character == "remilia":
        add "r_wings":
            at gallery_character_preview
            yoffset -80
        add sprite_image:
            at gallery_character_preview
            yoffset -80

    frame:
        style "gallery_controls_frame"

        vbox:
            spacing 16

            for attribute, label, values in config["attributes"]:
                vbox:
                    spacing 3

                    text _(label):
                        style "gallery_attribute_label"

                    hbox:
                        spacing 12

                        textbutton _("←"):
                            style "gallery_arrow_button"
                            action Function(
                                gallery_cycle_character_attribute,
                                character,
                                attribute,
                                -1,
                            )

                        text gallery_value_label(state[attribute]):
                            style "gallery_value_text"

                        textbutton _("→"):
                            style "gallery_arrow_button"
                            action Function(
                                gallery_cycle_character_attribute,
                                character,
                                attribute,
                                1,
                            )

    text _("Artist: camellia"):
        style "gallery_artist_credit"
        xalign 0.77

    textbutton _("Back"):
        style "gallery_back_button"
        action ShowMenu("gallery")

    key "game_menu" action ShowMenu("gallery")


screen background_gallery():
    tag menu

    add gui.main_menu_background
    add Solid("#09070de6")

    text _("Backgrounds"):
        style "gallery_title"

    viewport:
        style "gallery_grid_viewport"
        mousewheel True
        draggable True

        vpgrid:
            cols 2
            spacing 60

            for background_index, background in enumerate(GALLERY_BACKGROUNDS):
                $ background_title, background_image, background_artist = background

                vbox:
                    spacing 8

                    button:
                        xysize (420, 236)
                        action ShowMenu(
                            "background_gallery_view",
                            background_index=background_index,
                        )

                        add gallery_asset(
                            background_image,
                            background_title,
                            (420, 236),
                        ):
                            at gallery_thumbnail_hover

                    text background_title:
                        xalign 0.5

                    if background_artist:
                        text _("Artist: [background_artist]"):
                            xalign 0.5
                            color gui.idle_small_color

    textbutton _("Back"):
        style "gallery_back_button"
        action ShowMenu("gallery")

    key "game_menu" action ShowMenu("gallery")


screen background_gallery_view(background_index):
    tag menu

    $ background_title, background_image, background_artist = GALLERY_BACKGROUNDS[background_index]

    add gallery_asset(
        background_image,
        background_title + "\nPlaceholder",
        (1920, 1080),
        "#17121d",
    )

    if background_artist:
        text _("Artist: [background_artist]"):
            style "gallery_artist_credit"

    textbutton _("Back"):
        style "gallery_back_button"
        action ShowMenu("background_gallery")

    key "game_menu" action ShowMenu("background_gallery")


screen cg_gallery():
    tag menu

    add gui.main_menu_background
    add Solid("#09070de6")

    text _("CGs"):
        style "gallery_title"

    hbox:
        style "gallery_cg_entries"

        for cg_index, cg in enumerate(GALLERY_CGS):
            $ cg_title, cg_variants, cg_artist = cg
            $ variant_count = len(cg_variants)

            vbox:
                spacing 12

                button:
                    xysize (620, 349)
                    action ShowMenu(
                        "cg_gallery_view",
                        cg_index=cg_index,
                        variant_index=0,
                    )

                    add gallery_asset(
                        cg_variants[0],
                        cg_title,
                        (620, 349),
                    ):
                        at gallery_thumbnail_hover

                text cg_title:
                    xalign 0.5
                    size 38

                if cg_artist:
                    text _("Artist: [cg_artist]"):
                        xalign 0.5
                        color gui.idle_small_color

                text _("[variant_count] Variants"):
                    xalign 0.5
                    color gui.idle_small_color

    textbutton _("Back"):
        style "gallery_back_button"
        action ShowMenu("gallery")

    key "game_menu" action ShowMenu("gallery")


screen cg_gallery_view(cg_index, variant_index=0):
    tag menu

    # Screen parameters reset on every screen update, so copy the starting
    # variant into a default variable that SetScreenVariable can change.
    default current_variant = variant_index

    $ cg_title, cg_variants, cg_artist = GALLERY_CGS[cg_index]
    $ variant_count = len(cg_variants)
    $ variant_number = current_variant + 1
    $ variant_path = cg_variants[current_variant]

    add gallery_asset(
        variant_path,
        cg_title + "\nVariant {}".format(current_variant + 1),
        (1920, 1080),
        "#17121d",
    )

    textbutton _("←"):
        style "gallery_fullscreen_arrow_button"
        xpos 40
        yalign 0.5
        action SetScreenVariable(
            "current_variant",
            (current_variant - 1) % variant_count,
        )

    textbutton _("→"):
        style "gallery_fullscreen_arrow_button"
        xalign 1.0
        xoffset -40
        yalign 0.5
        action SetScreenVariable(
            "current_variant",
            (current_variant + 1) % variant_count,
        )

    text "[variant_number] / [variant_count]":
        xalign 0.5
        yalign 0.95
        outlines [(2, "#000000", 0, 0)]

    if cg_artist:
        text _("Artist: [cg_artist]"):
            style "gallery_artist_credit"

    textbutton _("Back"):
        style "gallery_back_button"
        action ShowMenu("cg_gallery")

    key "game_menu" action ShowMenu("cg_gallery")


style gallery_title is gui_label_text
style gallery_title:
    xalign 0.5
    ypos 45
    size 64
    color gui.accent_color

style gallery_main_buttons is vbox
style gallery_main_buttons:
    xalign 0.5
    yalign 0.5
    spacing 20

style gallery_main_buttons_button is gui_button
style gallery_main_buttons_button:
    xsize 420
    ysize 70

style gallery_main_buttons_button_text is gui_button_text
style gallery_main_buttons_button_text:
    xalign 0.5
    size 40

style gallery_back_button is navigation_button
style gallery_back_button:
    xpos 40
    yalign 1.0
    yoffset -35
    padding (25, 12)
    background Solid("#00000099")

style gallery_controls_frame is gui_frame
style gallery_controls_frame:
    xpos 1080
    xsize 700
    yalign 0.5
    padding (45, 35)
    background Solid("#17121de6")

style gallery_attribute_label is gui_text
style gallery_attribute_label:
    size 33
    color gui.accent_color

style gallery_value_text is gui_text
style gallery_value_text:
    min_width 320
    yalign 0.5
    text_align 0.5
    size 31

style gallery_arrow_button is gui_button
style gallery_arrow_button:
    xysize (70, 48)

style gallery_arrow_button_text is gui_button_text
style gallery_arrow_button_text:
    xalign 0.5
    size 34

style gallery_grid_viewport is gui_viewport
style gallery_grid_viewport:
    xpos 500
    ypos 160
    xsize 1420
    ysize 800

style gallery_cg_entries is hbox
style gallery_cg_entries:
    xalign 0.5
    yalign 0.5
    spacing 20

style gallery_fullscreen_arrow_button is gui_button
style gallery_fullscreen_arrow_button:
    xysize (90, 90)
    background Solid("#00000099")
    hover_background Solid("#9933ffcc")

style gallery_fullscreen_arrow_button_text is gui_button_text
style gallery_fullscreen_arrow_button_text:
    xalign 0.5
    size 52

style gallery_artist_credit is gui_text
style gallery_artist_credit:
    xalign 1.0
    xoffset -40
    yalign 1.0
    yoffset -35
    outlines [(2, "#000000", 0, 0)]
