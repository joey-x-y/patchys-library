define cpp = "patchy/"
define cppe = cpp + "expression/"

transform sprite_set_patchy:
    zoom 0.24
    xanchor 0.5
    yanchor 1.0
    yoffset 60

layeredimage p:
    at sprite_set_patchy

    group base:
        attribute base default:
            cpp + "default/patchy default.png"
        attribute magic:
            cpp + "magic/patchy magic.png"
        attribute nohat:
            cpp + "no acc/patchy no hat default.png"
        attribute magicnohat:
            cpp + "no acc/patchy no hat magic .png"

    group face:
        attribute neutral default:
            cppe + "default.png"
        attribute angry:
            cppe + "angry.png"
        attribute serious:
            cppe + "serious.png"
        attribute smile:
            cppe + "smile.png"
        attribute surprised:
            cppe + "shock.png"
        attribute think:
            cppe + "Thinking.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cppe + "blusing.png"