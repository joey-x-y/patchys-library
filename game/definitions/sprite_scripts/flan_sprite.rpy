define cpf = cp + "flandre/"
define cpfe = cpf + "expression/"
define cpfw = cpf + "wing/"
define cpfa = cpf + "acc/"

# TODO consider removing blushes from surprised face, or add questioning face



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

    # group eyes:
    #     attribute eye1 default:
    #         cpfe + "eye 1.png"
    #     attribute eye2:
    #         cpfe + "eye 2.png"
    #     attribute eye3:
    #         cpfe + "eye 3.png"
    #     attribute eye4:
    #         cpfe + "eye 4.png"
    #     attribute eye5:
    #         cpfe + "eye 5.png"
    #     attribute eye6:
    #         cpfe + "eye 6.png"

    # group mouth:
    #     attribute mouth1 default:
    #         cpfe + "mouth 1.png"
    #     attribute mouth2:
    #         cpfe + "mouth 2.png"
    #     attribute mouth3:
    #         cpfe + "mouth 3.png"
    #     attribute mouth4:
    #         cpfe + "mouth 4.png"
    #     attribute mouth5:
    #         cpfe + "mouth 5.png"
    #     attribute mouth6:
    #         cpfe + "mouth 6.png"
    #     attribute mouth7:
    #         cpfe + "mouth 7.png"

    # smile = eye2 mouth3
    # angry = eye3 mouth5
    # surprised = eye5 mouth5

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
        attribute holding_tear:
            cpfe + "tear 1.png"
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