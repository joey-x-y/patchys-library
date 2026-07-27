define cpp = cp + "patchy/"
define cppe = cpp + "expression/"
define cppa = cpp + "acc/"

layeredimage p:
    at sprite_set(scale=0.6, yoffset=60)

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
        attribute angry:
            cppe + "nose.png"
        attribute annoyed:
            cppe + "eye 1.png"
        attribute annoyed:
            cppe + "mouth 6.png"
        attribute serious:
            cppe + "serious.png"
        attribute smile:
            cppe + "smile.png"
        attribute surprised:
            cppe + "shock.png"
        attribute think:
            cppe + "thinking.png"
        attribute curious:
            cppe + "eye 1.png"
        attribute curious:
            cppe + "mouth 5.png"
        attribute confused:
            cppe + "eye 1.png"
        attribute confused:
            cppe + "mouth 6.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cppe + "blushing.png"