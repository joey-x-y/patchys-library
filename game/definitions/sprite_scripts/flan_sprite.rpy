define cpf = cp + "flandre/"
define cpfe = cpf + "expression/"
define cpfw = cpf + "wing/"
define cpfa = cpf + "acc/"

image right_wing = Composite(
    (1804, 1733),
    (902, 0),
    Transform(
        cpfw + "wing beginning.png",
        crop=(902, 0, 902, 1733) # x, y, width, height
    )
)

layeredimage f:
    at sprite_set

    group wings:
        attribute begin default:
            cpfw + "wing beginning.png"
        attribute mid:
            cpfw + "wing mid.png"
        attribute gone:
            cpfw + "wing stem.png"
        attribute crystal:
            cpfw + "wing crystal.png"
        attribute rightwing:
            "right_wing"

    group hair:
        attribute long default:
            cpfw + "back hair.png"
        attribute short:
            Null()

    always:
        cpf + "no ac base/base.png"

    group hat:
        attribute ribbon default:
            cpfa + "bow.png"
        attribute nohat:
            Null()

    group face:
        attribute neutral default:
            cpfe + "eye 2.png"
        attribute neutral default:
            cpfe + "mouth 1.png"
        attribute frown:
            cpfe + "eye 1.png"
        attribute frown:
            cpfe + "mouth 2.png"
        attribute angry:
            cpfe + "hostile.png"
        attribute crying:
            cpfe + "crying.png"
        attribute holding_tear:
            cpfe + "eye 4.png"
        attribute holding_tear:
            cpfe + "mouth 2.png"
        attribute serious:
            cpfe + "serious.png"
        attribute smile:
            cpfe + "eye 2.png"
        attribute smile:
            cpfe + "mouth 3.png"
        attribute surprised:
            cpfe + "eye 5.png"
        attribute surprised:
            cpfe + "mouth 5.png"
        attribute question:
            cpfe + "eye 2.png"
        attribute question:
            cpfe + "mouth 6.png"

    group tired:
        attribute awake default:
            Null()
        attribute tired:
            cpfa + "bag.png"

    group dirt:
        attribute none default:
            Null()
        attribute dirty:
            cpfa + "dirty.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cpfe + "blush.png"