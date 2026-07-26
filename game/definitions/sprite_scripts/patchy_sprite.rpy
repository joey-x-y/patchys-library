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
        attribute angry:
            cppe + "nose.png"
        attribute annoyed:
            cppe + "eye 4.png"
        attribute annoyed:
            cppe + "mouth 4.png"
        attribute serious:
            cppe + "eye 4.png"
        attribute serious:
            cppe + "mouth 5.png"
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

    # group eyes:
    #     attribute eye1 default:
    #         cppe + "eye 1.png"
    #     attribute eye2:
    #         cppe + "eye 2.png"
    #     attribute eye3:
    #         cppe + "eye 3.png"
    #     attribute eye4:
    #         cppe + "eye 4.png"
    #     attribute eye5:
    #         cppe + "eye 5.png"
    #     attribute eye6:
    #         cppe + "eye 6.png"
        
    # group mouth:
    #     attribute mouth1 default:
    #         cppe + "mouth 1.png"
    #     attribute mouth2:
    #         cppe + "mouth 2.png"
    #     attribute mouth3:
    #         cppe + "mouth 3.png"
    #     attribute mouth4:
    #         cppe + "mouth 4.png"
    #     attribute mouth5:
    #         cppe + "mouth 5.png"
    #     attribute mouth6:
    #         cppe + "mouth 6.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cppe + "blushing.png"