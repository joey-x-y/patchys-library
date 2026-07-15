# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

default persistent.beat_game=False

define initial_magician_name = "Magician"
define real_magician_name = "Patchouli"

define magician_name = initial_magician_name

define r = Character("Remilia", color="#4aa8ff")
define f = Character("Flandre", color="#ff786c")
define p = DynamicCharacter("magician_name", color="#c767ff")


# The game starts here.

label start:
    stop music fadeout 2.0
    # call test

    call day1 from _call_day1
    call day2 from _call_day2
    call day3 from _call_day3
    call day4 from _call_day4
    call day5 from _call_day5
    call day6 from _call_day6
    call day7 from _call_day7

    return

label test:
    scene bg_library

    $ remi.show(expression="neutral", at=center)
    $ flan.show(expression="frown", at=far_left)
    $ pat.show(expression="neutral", at=right)


    r "We are testing, you scoundrel!"

    $ flan.move(flip)

    f "WHYYHU yo ma"