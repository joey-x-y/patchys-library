define pp = "images/"

transform sprite_set:
    zoom 0.5
    # yoffset -100

layeredimage patchy:
    at sprite_set

    always:
        pp + "placeholder_patchy.png"

layeredimage flandre:
    at sprite_set

    always:
        pp + "placeholder_flandre.png"