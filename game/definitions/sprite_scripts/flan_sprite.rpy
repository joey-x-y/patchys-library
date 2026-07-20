define cpf = cp + "flandre/"
define cpfe = cpf + "expression/"
define cpfw = cpf + "wing/"
define cpfa = cpf + "acc/"

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

    group face:
        attribute neutral default:
            cpfe + "normal face.png"
        attribute frown:
            cpfe + "eye 1.png"

        attribute frown:
            cpfe + "mouth 2.png"
            # cpfe + "beginging frown.png"
        attribute angry:
            cpfe + "hostile.png"
        attribute crying:
            cpfe + "crying.png"
        attribute holding_tear:
            cpfe + "holding back tear.png"
        attribute serious:
            cpfe + "serious.png"
        attribute smile:
            cpfe + "smile.png"
        attribute surprised:
            cpfe + "suprise.png"

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