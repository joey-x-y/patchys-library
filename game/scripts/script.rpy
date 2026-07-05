# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define initial_magician_name = "Magician"
define real_magician_name = "Patchouli"

define magician_name = initial_magician_name

define r = Character("Remilia", color="#4aa8ff")
define f = Character("Flandre", color="#ff786c")
define p = DynamicCharacter(magician_name, color="#ff67ff")


# The game starts here.

label start:

    call day1
    call day2
    call day3
    call day4
    call day5
    call day6
    call day7

    return
