define cpf = "flandre/"
define cpfe = cpf + "expression/"
define cpfw = cpf + "Wing layer/"

layeredimage f:
    at sprite_set

    group wings:
        attribute begin default:
            cpfw + "wing begining.png"
        attribute mid:
            cpfw + "wing mid.png"
        attribute gone:
            cpfw + "wing end.png"
        attribute crystal:
            cpfw + "wing crystal.png"

    group base:
        attribute clean default:
            cpf + "default/flandre normal default.png"
        attribute noacc:
            cpf + "no acc/base.png"

    group face:
        attribute neutral default:
            cpfe + "default.png"
        attribute frown:
            cpfe + "beginging frown.png"
        attribute angry:
            cpfe + "angry.png"
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

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cpfe + "blusing.png"

    group dirt:
        attribute none default:
            Null()
        attribute dirty:
            Fixed(
                cpf + "dirty/base.png",
                cpfe + "bag eye.png"
            )
