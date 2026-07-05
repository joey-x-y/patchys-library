define pp = "images/"

transform sprite_set:
    zoom 0.22
    # yoffset -100

transform sprite_set_placeholder:
    zoom 0.5

layeredimage pat:
    at sprite_set

    always:
        pp + "patchy.png"

layeredimage flan:
    at sprite_set_placeholder

    always:
        pp + "placeholder_flandre.png"

layeredimage rem:
    at sprite_set_placeholder

    always:
        pp + "placeholder_patchy.png"