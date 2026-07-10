define cp = "images/characters/"

transform sprite_set:
    zoom 0.22
    # yoffset -100

layeredimage pat:
    at sprite_set

    always:
        cp + "patchy.png"

layeredimage flan:
    at sprite_set

    always:
        cp + "placeholder_flandre.png"

layeredimage rem:
    at sprite_set

    always:
        cp + "placeholder_patchy.png"