define cpr = cp + "remi/"
define cpre = cpr + "expression/"
define cpra = cpr + "acc/"
define cprf = cpr + "effects/"

image r_wings = At(cpr + "wing/remilia.png", sprite_set)

# TODO consider removing blushes from embarrased and other main faces

layeredimage r:
    at sprite_set
    
    always:
        cpr + "no ac base/remilia.png"

    group hat:
        attribute hat default:
            cpra + "hat.png"
        attribute nohat:
            Null()
            
    group glove:
        attribute glove default:
            cpra + "glove.png"
        attribute noglove:
            Null()
        attribute bloody:
            cpra + "bloody hand.png"

    group face:
        attribute neutral default:
            cpre + "default.png"
        attribute angry:
            cpre + "angry.png"
        attribute crying:
            cpre + "holding back tear.png"
        attribute crying2:
            cpre + "crying ver 2.png"
        attribute embarrassed:
            cpre + "embarssed.png"
        attribute serious:
            cpre + "serious.png"
        attribute smile:
            cpre + "smile.png"
        attribute surprised:
            cpre + "suprised.png"

    group tired:
        attribute awake default:
            Null()
        attribute tired:
            cpra + "bag.png"

    group dirt:
        attribute none default:
            Null()
        attribute dirty:
            cpra + "dirt.png"

    group effects:
        attribute noeffect default:
            Null()
        attribute blushing:
            cprf + "blush.png"