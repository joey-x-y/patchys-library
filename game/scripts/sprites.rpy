define pp = "images/"

transform sprite_set:
    zoom 0.22
    # yoffset -100

transform sprite_set_placeholder:
    zoom 0.5

layeredimage patchy:
    at sprite_set

    always:
        pp + "patchy.png"

layeredimage flandre:
    at sprite_set_placeholder

    always:
        pp + "placeholder_flandre.png"