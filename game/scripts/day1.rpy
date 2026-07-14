label day1:

    call day1_forest
    call day1_library
    call day1_end

    return
    
label day1_forest:
    scene bg_forest

    play music bgm_forest fadein 2.0

    $ remi.show(dirty=True, at=[left, standheight])
    $ flan.show(dirty=True, at=[right, standheight])

    f "Remi! Look out!"

    "Remilia swerves upwards, narrowly avoiding a tree."

    r "That was close."

    f "Just land already! You've been flying for hours!"

    r "No, no, I can still..."

    "They slowly drift downward, back into the treeline."

    f "Remi!"

    r "Wh—"

    "They blast through a wall of thin branches."

    f "See! You're going to kill yourself like this!"

    r "Fine."

    play sound sfx_forest_land

    "Remilia drops down from the air and catches her breath. Flandre steps down from her back."

    f "Geez, Remi."

    "Remilia takes Flandre's hand."

    r "We need to keep moving, trees aren't good enough shelter from the sun. It will cut through the leaves."

    f "But you're pushing yourself to death. Slow down."

    r "I'm just trying to..."

    "She takes a deep breath."

    r "I'll be careful. Can you walk?"

    f "I'll try."

    play sound sfx_forest_footsteps
    with forest_walk_fade

    f "Hey... I'm getting really tired. I need a break."

    r "There's no time. Please push for a little longer."

    play sound sfx_forest_land 

    "Flandre's legs buckle, and she falls back hard."

    f "I can't."

    "Remilia kneels down and places her hand on Flandre's hat."

    r "Alright. We'll spare a few minutes."

    "Remilia begins to get up, but gets pulled back down."

    f "You need rest too."

    r "It will be just a moment."

    "Flandre sighs and lets go."

    "Remilia leaves, and quickly returns with a rabbit in hand."

    r "A feast, just for you."

    f "Thanks."

    "Flandre devours half of it."

    f "Here's the rest."

    r "I'll be alright."

    f "No you won't. You're hungry too."

    r "Keep the rest. You need it more."

    f "Fine."

    "Flandre finishes and tosses the bones aside."

    r "How are your wings feeling?"

    f "They hurt."

    r "Has the pain lessened at all?"

    f "No."

    r "I see."

    "Remilia looks off to the sky. The purple foreglow of sunrise begins to show itself."

    r "We cannot wait any longer. Let's go, Flandre. Take my hand."

    f "Okay..."

    "Flandre grabs Remilia's hand and pulls herself up."

    r "There must be some kind of shelter. Hunters build cabins out here."

    f "Vampire hunters?"

    r "No, the animal kind. Don't worry."

    "Flandre grabs Remilia's hand as they begin walking."

    play sound sfx_forest_footsteps
    with forest_walk_fade

    r "Oh?"

    "Among the trees, they find a large, old-looking building."

    r "Odd. But it is shelter."

    f "What if someone scary is in there?"

    play sound sfx_forest_land

    "Remilia steps to the door and grabs the handle."

    r "We have no choice. Come, I'll keep you safe."

    "The edge of the sun begins to rise, stinging their vampiric skin."

    "Then, they enter the mysterious building together."

    return

label day1_library:
    stop music fadeout 2.0

    call scene_transition_fade("bg_library")

    "They step into a large library. Bookshelves line the walls, and a large staircase lies straight ahead."

    $ remi.show(at=[standheight, far_left, enterleft], zorder=1)
    $ flan.face(flipped=True)
    $ flan.show(at=[standheight, corner_left, enterleft])

    "Flandre leans into her sister's ear."

    f "Do you think anyone is here?"

    "Remilia takes Flandre's hand."

    r "Let's take a look. Try to keep quiet."

    $ remi.move(enterforcefinish)
    $ flan.move(enterforcefinish)
    with None

    $ remi.move(left)
    $ flan.move(far_left)
    with ease

    pause 0.3

    
    $ remi.move(far_left)
    $ flan.move(corner_left)
    with move_fast

    call spear_summon()

    play sound sfx_magic_clash_2

    $ remi.effect(shake)

    call spear_block_quick()

    "Something fires at Remilia's neck, but she summons her spear to block at the last moment."

    call spear_block_continuous()

    r "This trap won't on us, fool."

    $ flan.effect(scoot_right)

    f "What is that?!"

    r "Stay close. I have it handled."

    call spear_block_barrage_end()

    play music bgm_duel fadein 2.0

    $ pat.face(flipped=True)
    $ pat.show(magic=True, at=[standheight, floatup, corner_right, enterright(speed=1.5)])

    pause 1.5

    # call lazer_charge(flash_time=2, pause_time=0.5)

    "The attacks stop as a purple figure appears in the air. A mass of crystals appear around her and begin to glow. Yellow on her left, blue on the right."

    "Remilia lifts her spear, charging it up in response."

    call spear_lazer_clash()

    "The crystals fire beams of light and water, Remilia meets them with a flash of energy from her spear. The attacks cancel each other out."

    "Remilia's knees buckle for a moment. Flandre holds Remilia from behind, stabilizing her. The magician watches intently."

    p "Leave, monsters."

    r "We can't! We just need shelter for the day."

    "The crystals begin charging again."

    p "A shame."

    call spear_lazer_clash()

    "Remilia charges her spear again, and the beams collide. Remilia nearly goes limp in Flandre's arms, heavily breathing."

    f "Sis..."

    call spear_lazer_clash()

    "Again, the lasers fire. They collide yet again."

    play sound sfx_body_fall
    $ remi.move(dropdown)
    $ flan.move(unscoot)

    "As the crystals charge again, Remilia drops."

    f "Remi, no!"

    play sound sfx_magic_cast
    $ flan.move(left, transition=move_fast)

    call spear_summon()

    "Flandre steps in front of Remilia's body and summons her sword. The magician charges her crystals."

    f "Hah!"

    call spear_lazer_clash(defender=flan)

    "The red slash collides with the lasers, splitting them in half. They crash into the ground next to the sisters."

    play sound sfx_body_fall
    $ flan.move(drophalf)

    "Flandre drops to her knees, breathing frantically."

    $ pat.move([floatdowntocenter])
    call clear_effects

    "The magician slowly floats down in front of them."

    p "It appears neither of you can fight anymore."

    f "We never wanted to! We just want to rest!"

    p "This is a magician's domain. A poor choice."

    f "We had to! The sun will kill us!"

    p "Hmm..."

    stop music fadeout 2.0

    p "I've never seen vampires before. I want to study you. On that condition, you may stay."

    f "Fine!"

    play sound sfx_door_open

    p "Your room is over there. Go on."

    play sound sfx_rustle_2
    $ flan.move(standup)
    pause 0.5
    $ flan.move(shake(magnitude=4))
    pause 0.3
    play sound sfx_body_fall
    $ flan.move(drophalf)

    p "Hm. I suppose you are rather exhausted."

    play sound sfx_magic_summon

    $ remi.move(offscreenright)
    $ flan.move(offscreenright)
    with ease

    f "Whoa!"

    "The magician sends them off to their room."

    return

label day1_end:

    call scene_transition_fade("bg_bedroom_nocoffin")
    $ pat.face(flipped=False)
    $ flan.face(flipped=False)
    $ remi.face(flipped=True)

    $ flan.show(at=[standheight, right, enterleft(speed=1.5)], zorder=1)
    $ remi.show(at=[dropdowninstant, corner_right, enterleft(speed=1.5)])
    
    pause 0.7
    $ pat.show(magic=False, at=[standheight, left, enterleft(speed=1.5)])

    p "This will be your room. It should be good enough for two."

    p "That is all for today. Rest well, I need healthy subjects."

    f "Um... I can't sleep. My wings... they burn."

    p "Fine. Bring them here."

    $ flan.move(enterforcefinish)
    $ remi.move(enterforcefinish)
    $ pat.move(enterforcefinish)
    with None

    $ flan.move(center_left, transition=move_slow)
    $ flan.face(flipped=True, transition=dissolve_fast)

    "Flandre stumbles over, presenting her back."

    $ remi.move(drophalf)

    r "What do you intend to do with them?"

    $ flan.show(expression="smile")

    f "Remi, you're awake!"

    r "Yes, I was the whole time. I just couldn't move."

    p "Then you should understand your situation. I am studying a vampire, as agreed. Be silent."

    $ remi.move(standup)

    "Remilia stands and stares her down."

    "The magician leans in close to the wings for a few moments."

    $ pat.show(magic=True, transition=dissolve_fast)
    call generic_spell()
    
    p "I numbed them."

    $ flan.move(hop)

    f "Yay! Thank you!"

    $ pat.show(magic=False, transition=dissolve_fast)

    $ flan.move(hopreset)
    $ flan.move(right, transition=ease)
    
    $ flan.face(flipped=False)

    p "Is that all?"

    f "Um... can we have coffins?"

    p "...Why?"

    f "Sorry, never mind."

    p "Then I belie—"

    r "No, it's important. Vampires recover far quicker inside one. If you want your test subjects to be at full health, you should bring some."

    p "Ugh..."

    $ pat.flip()
    $ pat.show(magic=True, transition=dissolve_fast)
    call generic_spell()

    show bg_bedroom behind f, r, p with dissolve

    "She summons two coffins onto the bed."

    $ pat.flip()
    $ pat.show(magic=False, transition=dissolve_fast)

    p "No more."

    play sound sfx_stomach_growling
    $ remi.move(shake(1, 0.3))

    r "..."

    f "Um, we're hungry. Sorry."

    p "I'll warp something later."

    $ pat.move(corner_left, transition=move_slow)

    p "A word of caution. Try anything, you'll explode. So don't."

    $ pat.move(offscreenleft)
    with move_slow
    $ flan.move(left)
    $ remi.move(right)
    with move_slow
    $ flan.face(flipped=True, transition=dissolve_fast)

    "Remilia lets out a massive sigh."

    r "What a ridiculous situation."

    f "But we have shelter."

    r "Indeed. How are your wings doing? Did she do anything strange?"

    f "Nope! I can't feel them! It's great! I can finally—"

    play sound sfx_body_fall

    $ remi.show(dropdown, zorder=1)

    f "Ah, Remi!"

    $ flan.move([center_right, drophalf], transition=ease)

    "She runs over and kneels down beside her."

    f "You seriously passed out? Ugh, I told you to eat."

    play sound sfx_coffin_close

    $ flan.move(standup)
    $ remi.hide(transition=dissolve)
    $ flan.face(flipped=False, transition=dissolve_fast)

    "Flandre picks her up and drops her into a coffin. She sits on the edge of the bed."

    f "We really need food..."

    call generic_spell()

    "After a few moments, a dead chicken appears on the table."

    f "Oh!"

    "She feeds Remilia its blood."

    f "Take care of yourself too. Stupid sis."

    play sound sfx_coffin_close
    $ flan.hide(transition=dissolve_fast)

    scene black with fade
    

    "Flandre finishes the meal, then jumps into the other coffin."

    f "Finally... I can..."

    return
