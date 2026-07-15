define cpr = "remi/"
define cpre = cpr + "expression/"

image r_wings = At(cpr + "wing.png", sprite_set)

layeredimage r:
    at sprite_set

    group base:
        attribute clean default:
            cpr + "default/remilia.png"
        attribute hunt:
            cpr + "dirty/remilia dirty hunt rabbit.png"
        attribute noacc:
            cpr + "no acc/remilia default no head band.png"

    group face:
        attribute neutral default:
            cpre + "default.png"
        attribute angry:
            cpre + "angry.png"
        attribute crying:
            cpre + "crying 1.png"
        attribute crying2:
            cpre + "crying 2.png"
        attribute embarrassed:
            cpre + "embarssed.png"
        attribute holding_tear:
            cpre + "hodlign tear.png"
        attribute serious:
            cpre + "serious.png"
        attribute smile:
            cpre + "smile.png"
        attribute surprised:
            cpre + "suprised.png"

    group dirt:
        attribute none default:
            Null()
        attribute dirty:
            Fixed(
                cpr + "dirty/remilia dirty.png",
                cpr + "eyebag.png"
            )