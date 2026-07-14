# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define initial_magician_name = "Magician"
define real_magician_name = "Patchouli"

define magician_name = initial_magician_name

define r = Character("Remilia", color="#4aa8ff")
define f = Character("Flandre", color="#ff786c")
define p = DynamicCharacter("magician_name", color="#c767ff")


# The game starts here.

label start:

    # call test

    call day1
    call day2
    call day3
    call day4
    call day5
    call day6
    call day7

    return

label test:
    scene bg_library

    $ remi.show(expression="neutral", at=center)
    $ flan.show(expression="frown", at=far_left)
    $ pat.show(expression="neutral", at=right)


    r "We are testing, you scoundrel!"

    $ flan.move(flip)

    f "WHYYHU yo ma"