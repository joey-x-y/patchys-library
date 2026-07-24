define cpp = cp + "patchy/"
define cppe = cpp + "expression/"
define cppa = cpp + "acc/"

# TODO consider changing neutral mouth, build annoyed face. build curious face, probably just neutral mouth with wide eyes. Confused similar to curious

layeredimage p:
    at sprite_set(scale=0.62, yoffset=60)

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
        attribute annoyed:
            cppe + "angry.png"
        attribute serious:
            cppe + "serious.png"
        attribute smile:
            cppe + "smile.png"
        attribute surprised:
            cppe + "shock.png"
        attribute think:
            cppe + "thinking.png"
        attribute curious:
            cppe + "normal face.png"
        attribute confused:
            cppe + "normal face.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cppe + "blushing.png"