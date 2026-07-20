define cpp = cp + "patchy/"
define cppe = cpp + "expression/"
define cppa = cpp + "acc/"

transform sprite_set_patchy:
    zoom 0.62
    xanchor 0.5
    yanchor 1.0
    yoffset 60

layeredimage p:
    at sprite_set_patchy

    group base:
        attribute base default:
            cpp + "no ac base/base.png"
        attribute magic:
            cpp + "no ac base/base magic.png"

    group hat:
        attribute hat default:
            cppa + "hat.png"
        attribute nohat:
            Null()

    group face:
        attribute neutral default:
            cppe + "normal face.png"
        attribute angry:
            cppe + "angry.png"
        attribute serious:
            cppe + "serious.png"
        attribute smile:
            cppe + "smile.png"
        attribute surprised:
            cppe + "shock.png"
        attribute think:
            cppe + "thinking.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cppe + "blushing.png"