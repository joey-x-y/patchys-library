define cpr = "remi/"
define cpre = cpr + "expression/"
define cpra = cpr + "accessary/"

image r_wings = At(cpr + "wing.png", sprite_set)

layeredimage r:
    at sprite_set

    always:
        cpr + "no acc/remilia default no head band.png"

    group hat:
        attribute hat default:
            cpra + "headdress.png"
        attribute nohat:
            Null()
            
    group glove:
        attribute glove default:
            cpra + "glove.png"
        attribute noglove:
            Null()
        attribute bloody:
            cpra + "hunt_hand.png"

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

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cpre + "plusing.png"

    group dirt:
        attribute none default:
            Null()
        attribute dirty:
            Fixed(
                cpr + "eyebag.png",
                cpr + "dirty/remilia dirty.png"
            )