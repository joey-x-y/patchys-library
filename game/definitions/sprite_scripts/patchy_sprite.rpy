define cpp = cp + "patchy/"

transform sprite_set_patchy:
    zoom 0.24
    xanchor 0.5
    yanchor 1.0
    yoffset 60

## Default

image p neutral = At(cpp + "default/default_patchy default .png", sprite_set_patchy)
image p smile = At(cpp + "default/smile_patchy default .png", sprite_set_patchy)
image p angry = At(cpp + "default/angry_patchy default .png", sprite_set_patchy)

## Magic

image p neutral magic = At(cpp + "magic/patchy magic.png", sprite_set_patchy)
image p smile magic = At(cpp + "magic/smile_patchy magic default .png", sprite_set_patchy)
image p angry magic = At(cpp + "magic/Angry_patchy magic default .png", sprite_set_patchy)

## No hat

image p neutral nohat = At(cpp + "no hat/default no hat/default_patchy default no hat.png", sprite_set_patchy)
image p smile nohat = At(cpp + "no hat/default no hat/smile_patchy default no hat.png", sprite_set_patchy)
image p angry nohat = At(cpp + "no hat/default no hat/angry_patchy default no hat.png", sprite_set_patchy)

## No hat + magic

image p neutral nohat magic = At(cpp + "no hat/magic no hat/patchy magic no hat.png", sprite_set_patchy)
image p smile nohat magic = At(cpp + "no hat/magic no hat/smile_patchy magic no hat.png", sprite_set_patchy)
image p angry nohat magic = At(cpp + "no hat/magic no hat/angry_patchy magic no hat.png", sprite_set_patchy)


