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

    # group eyes:
    #     attribute eye1 default:
    #         cpre + "eye 1.png"
    #     attribute eye2:
    #         cpre + "eye 2.png"
    #     attribute eye3:
    #         cpre + "eye 3.png"
    #     attribute eye4:
    #         cpre + "eye 4.png"
    #     attribute eye5:
    #         cpre + "eye 5.png"
    #     attribute eye6:
    #         cpre + "eye 6.png"
    #     attribute eye7:
    #         cpre + "eye 7.png"
    #     attribute eye8:
    #         cpre + "eye 8.png"
    #     attribute eye9:
    #         cpre + "eye 9.png"

    # group mouth:
    #     attribute mouth1 default:
    #         cpre + "mouth 1.png"
    #     attribute mouth2:
    #         cpre + "mouth 2.png"
    #     attribute mouth3:
    #         cpre + "mouth 3.png"
    #     attribute mouth4:
    #         cpre + "mouth 4.png"
    #     attribute mouth5:
    #         cpre + "mouth 5.png"
    #     attribute mouth6:
    #         cpre + "mouth 6.png"
    #     attribute mouth7:
    #         cpre + "mouth 7.png"
    #     attribute mouth8:
    #         cpre + "mouth 8.png"

    # expression combos: 
    # embarrassed = eye9 mouth8
    # smile = eye1 mouth2
    # surprise = eye8 mouth1
    # serious = eye7 mouth5

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
            cpre + "eye 9.png"
        attribute embarrassed:
            cpre + "mouth 8.png"
        attribute serious:
            cpre + "eye 7.png"
        attribute serious:
            cpre + "mouth 5.png"
        attribute smile:
            cpre + "eye 1.png"
        attribute smile:
            cpre + "mouth 2.png"
        attribute surprised:
            cpre + "eye 8.png"
        attribute surprised:
            cpre + "mouth 1.png"
        attribute surprised:
            cprf + "sweat emote.png"
        attribute annoyed:
            cpre + "eye 1.png"
        attribute annoyed:
            cpre + "mouth 7.png"
        attribute annoyed:
            cprf + "sweat emote.png"

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