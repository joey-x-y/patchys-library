label day7:

    call day7_morning from _call_day7_morning

    call epilogue from _call_epilogue

    $ persistent.beat_game = True

    return

label day7_morning:

    call day_transition_in from _call_day_transition_in_5

    $ remi.show([center_right, standheight, enterbottom(0.5)], flip=True)

    pause 0.5

    $ flan.show([far_left, standheight, enterbottom()])
    $ remi.move(enterforcefinish)
    with None
    $ remi.flip(transition=dissolve_fast)

    r "Um... hello, Flandre. Are you doing alright?"

    f "Sure. Sorry for hitting you."

    play music bgm_library fadein 2.0

    $ remi.show(expression="smile", at=hop(10))

    "Remilia stands and puts her hands on her hips."

    r "Don't worry, I'm durable. I can bounce back from a few elbows."

    f "Heh, would that still be true if I hit you hard?"

    $ remi.expression("surprised")

    r "Uh... didn't you?"

    $ flan.move(corner_right, transition=move_slow)
    $ remi.flip(transition=dissolve_fast)

    r "You going already?"

    f "Yes."

    $ flan.move(offscreenright)
    $ remi.show(expression="neutral", at=offscreenright, transition=move_slow)

    call scene_transition_fade("bg_library_stairs") from _call_scene_transition_fade_38

    $ flan.show([center_left, standheight], flip=True)
    $ remi.show([right, standheight], flip=True, transition=dissolve)

    "She leaves, and Remilia follows her up the stairs."

    r "How's your balance?"

    f "Manageable enough."

    r "I could at least hold your hand."

    $ flan.show(flip=True, transition=dissolve, zorder=3)

    f "...Fine."

    $ remi.show(expression="smile", at=center, transition=move_slow)
    $ flan.flip(transition=dissolve)

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_39

    $ pat.show([right, standheight], transition=dissolve)

    $ flan.show([center_left, standheight, enterleft()], flip=True)
    $ remi.show(expression="neutral", at=[left, standheight, enterleft()], flip=True)

    "As they arrive, Patchouli looks up from her mountain of books and scrolls."

    p "Ah, Flandre."

    f "Hi."

    p "I'm, uh, sorry about your wings."

    f "Don't apologize for it. What's the plan now? Is there any hope?"

    p "I have been... thinking."

    f "About what?"

    p "I was trying to restore your wings, but now I have to think about how they could be replaced in their entirety."

    f "Huh. New wings? How's that work?"

    p "I don't know. Even though Remilia let me explore her wing anatomy, I'm unsure how I could replicate it."

    $ remi.expression("angry")

    r "Hey!"

    f "You what about anata what?"

    p "I got a feel of Remilia's wings, taking note of how the flaps and stem feel and connect with each other. I touched them as thoroughly as I could to try and fully understand them."

    $ remi.blush()
    $ flan.move(enterforcefinish)
    with None
    $ flan.flip(transition=dissolve)

    "A shocked Flandre looks over to a tomato-faced Remilia."

    r "Shut up!"

    f "But I haven't made fun of you yet."

    $ pat.move(center, transition=ease)
    $ flan.flip(transition=dissolve_fast)

    "Patchouli's head snaps to the wings."

    p "I would like to touch them more. May I?"

    $ remi.show(expression="neutral", at=scoot_left)

    r "I am not such an indecent vampire! I don't do such uncouth things on request!"

    $ remi.move(unscoot)

    f "I shouldn't leave you two alone together."

    $ remi.expression("angry")

    r "I said shut up!"

    $ remi.show(expression="neutral", at=center_left)
    $ flan.move(corner_left, transition=move_slow)

    "Remilia sighs as she walks over to Patchouli."

    r "Fine."

    p "Thank you."

    show cg_wingtouch zorder 8 with dissolve

    "Patchouli grasps the wings. Flandre stares intently."

    p "I must say, it is rather nice."

    r "Are you doing this to me on purpose?"

    p "Forbidden knowledge has an appeal."

    r "That doesn't answer my question."

    p "I believe it does."

    $ flan.show(closeup, zorder=9, transition=dissolve)

    f "Are you in love?"

    r "Be quiet!"

    p "I am satisfied."

    $ flan.move(closeuprevert)
    hide cg_wingtouch with dissolve

    $ remi.show(left)
    $ pat.move(right, transition=move_slow)

    f "Were they nice, Patchy?"

    r "Ugh..."

    "Patchouli stands with her eyes closed and arms folded, unresponsive."

    f "Looks like a yes."

    $ flan.show(zorder=2)
    $ remi.show(flip=True, transition=dissolve_fast)

    "Remilia walks in front of Flandre to flail her arms."

    $ remi.expression("angry")

    r "I showed her so she can understand wings more, to help with fixing yours. That is all. Understand?"

    f "Sure. Whatever you say."

    $ remi.expression("neutral")

    r "Oh... but—"

    $ remi.show(expression="surprised", blush=False, at=hop(10))
    $ flan.move(hop(10))

    p "But that doesn't even matter!"

    $ pat.move(floatup, transition=move)
    $ remi.show(expression="neutral", flip=True, transition=dissolve_fast)

    "Patchouli suddenly hovers into the air with a smile."

    f "Huh?"

    p "I don't have to make vampire wings!"

    $ pat.flip(transition=dissolve_fast)
    $ pat.move(offscreenright, transition=move_slow)

    $ flan.move(scoot_right)

    f "Patchy, wait! But I want wings!"

    "Flandre reaches out her arm in Patchouli's direction."

    $ pat.show(magic=True, at=[hopreset, right, enterright()], flip=True)
    $ flan.move(unscoot)

    "She returns with multiple crystals in hand."

    p "I can just attach magic crystals!"

    f "Whoa, magic crystals?"

    p "Yes! This shouldn't take very long."

    $ remi.move(center_left)
    $ flan.move(far_left, transition=move_slow)

    r "Hey, what's the plan exactly?"

    p "I will imbue these crystals with the same magic I use to move objects, and embed it into her wing stems. If she applies magical energy to her stems, it will react with the crystals."

    r "Huh."

    f "That sounds super cool!"

    p "Yes, I just need to think about how to implement that without them exploding on your back."

    f "Oh."

    p "Is trial and error acceptable? That would be fastest, and I believe your regeneration capabilities would be sufficient for survival."

    $ flan.move(hop(10))

    f "No! Use Remi!"

    r "No. Regeneration doesn't prevent pain."

    p "I can numb your body."

    $ remi.show(expression="angry", at=scoot_right)

    r "No! You're insane!"

    $ remi.show(expression="neutral", at=unscoot)

    p "Fair enough."

    "Patchouli takes a long exhale."

    p "Enough goofing off. Now, Flandre, I do believe you know how to use magical energy, right?"

    f "Yeah! Like this!"

    play sound sfx_magic_cast
    call spear_summon from _call_spear_summon_3

    "She summons her sword."

    $ remi.show(expression="serious", flip=True)

    r "Put that away!"

    f "Sorry."

    call spear_summon from _call_spear_summon_4

    $ remi.expression("neutral")

    "The sword disappears."

    $ remi.flip(transition=dissolve_fast)

    p "Perfect! This should work. Give me some time."

    $ flan.flip()
    $ flan.move(hop())

    f "Woohoo!"

    r "Would you like any help?"

    $ pat.move(center, transition=move_fast)
    play sound sfx_rustle_2
    $ remi.move(small_shake)

    "Patchouli grabs Remilia by the shoulders."

    p "Yup! I'll work you to the bone."

    $ remi.show(expresssion="embarrased", blush=True)

    r "Mm. Right."

    $ flan.flip()

    f "So touchy. Bleh."

    call scene_transition_fade("black") from _call_scene_transition_fade_40

    "Over the next few hours, Patchouli imbues various magical crystals as Remilia runs around gathering materials. Flandre lies on the ground reading about mercury."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_41

    $ remi.show(expression="neutral", blush=False, at=[center_left, standheight])
    $ pat.show([center_right, standheight])
    $ flan.show([corner_left, sitheight], flip=True)
    with dissolve

    p "Got it! This is stable! I think. Now for a test. Hold this, Remilia."

    $ pat.show(magic=True, transition=dissolve_fast)

    "She takes the crystal."

    p "Now, put a little energy into it."

    play sound sfx_magic_summon
    $ remi.move(floatup)
    call generic_spell from _call_generic_spell_11

    "Remilia slowly floats into the air."

    $ remi.expression("surprised")

    r "Whoa. Neat."

    p "Perfect. Now we attach these to the wing stems."

    $ remi.expression("smile")
    $ flan.flip()

    r "That's incredible!"

    $ flan.show([far_left, standheight], transition=ease, zorder=7)

    f "What's going on?"

    p "I believe the problem has been solved."

    $ flan.move(hop(length=0.25))

    f "Yay! Yay!"

    $ pat.move(hop(10))
    with None
    $ remi.move(hopreset, transition=move_fast)

    "Patchouli swipes the crystal from Remilia's hand."

    r "That was truly incredible. You're brilliant."

    p "Ehem, yes, of course. Now lie down, Flandre. I will attach them."

    $ flan.move(hopreset)
    $ flan.show(right, transition=move_fast, zorder=1)
    play sound sfx_body_fall

    $ remi.expression("neutral")

    r "Don't damage the table with your dive-bombing."

    f "This is my moment. Silence."

    $ remi.expression("smile")

    r "Fine, fine."

    call scene_transition_fade("black") from _call_scene_transition_fade_42

    stop music fadeout 2.0

    "Patchouli floats over Flandre. One by one, she places a crystal onto a wing stem, casts a spell, and it sticks. Eventually, she's done and floats away."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_43

    $ remi.show(expression="neutral", at=[corner_left, standheight])
    $ flan.show(wings="crystal", at=[right, sitheight], flip=True)
    $ pat.show(at=[left, standheight], flip=True, magic=False)
    with dissolve

    p "Listen to me closely. Stand up, slowly. Very carefully."

    f "Slowly. Got it."

    play sound sfx_crystals_clacking
    $ flan.move(standheight, transition=move_slow)

    "The crystals sway back and forth as she moves up."

    f "Wow! Musical wings!"

    p "Wait, no, hold on. Don't move."

    $ pat.show(center, transition=move_fast)
    call generic_spell from _call_generic_spell_12
    $ pat.show(left, transition=move_fast)

    p "Continue."

    $ flan.move(floatup, transition=move_slow)

    p "How is your balance?"

    f "Good! Kind of."

    p "Now, just apply the smallest amount of magical energy."

    # "Flandre shoots to the ceiling."

    # p "Gently!"

    # "She slowly floats down."

    "Flandre starts flipping in the air."

    p "How is it?"

    f "Awesome! Amazing! Absolutely astonishing!"

    $ remi.expression("smile")

    p "Good."

    f "I can fly! I can fly! Fly! Fly! Bird!"

    $ flan.move(offscreenright, transition=move_fast)

    "She zooms around the room, faster than their eyes can follow."

    p "Hey!"

    r "Give up. She won't stop."

    play music bgm_title fadein 2.0

    $ remi.show(blush=True, at=center_left)
    $ pat.show(center_right, flip=True, transition=move_slow, zorder=2)

    "Remilia walks up to Patchouli."

    p "I guess not. I trust you'll clean her messes? Fallen bookshelves are a pain."

    $ remi.expression("embarrassed", transition=dissolve)

    "Remilia's gaze flicks to the side and back to Patchouli a few times, her face steadily turning red."

    p "Uh, wha—"

    stop music fadeout 2.0
    
    call summon_cg("cg_kiss_surprise") from _call_summon_cg_3
    play music bgm_ending fadein 2.0

    "Remilia lunges into Patchouli, grabbing and kissing her."

    p "Mmm?"

    "Remilia pulls back after a few moments, looking into Patchouli's eyes. Her eyes are teary."

    r "Thank you Patchy! I... uh... oh. What did I just...?"

    "Patchouli looks back into her eyes."

    p "You just kissed me?"

    r "Yes, sorry. I don't know why I did that. Sorry."

    call summon_cg("cg_kiss_gentle") from _call_summon_cg_4

    "Remilia starts to let go, but Patchouli pulls her in for another kiss."

    "They hold it for ten seconds before separating again."

    scene black onlayer screens with dissolve

    call summon_cg("cg_stare") from _call_summon_cg_5

    r "Uh, uh..."

    p "This is nice."

    r "Uh, yes."

    "They stand silently."

    r "Hey, um... can we... more?"

    p "Mm."

    call summon_cg("cg_kiss_gentle") from _call_summon_cg_6

    "They go back in for another."

    show f crystal onlayer screens at corner_right, closeup

    f "The moment I look away."

    call dismiss_cg from _call_dismiss_cg_3

    $ remi.show(expression="surprised", at=far_left)
    $ pat.move(right, transition=move_fast)

    "They jump apart."

    $ flan.move(corner_right, transition=dissolve)
    $ remi.expression("angry")

    r "She was just, checking something!"

    $ remi.expression("neutral")

    f "Sure... sure. Give up, lovebirds. How many kisses was that?"

    p "Three."

    f "How many before today?"

    p "Zero, sadly."

    r "Patchy, don't tell her."

    f "Patchy?"

    $ remi.expression("embarrassed")

    r "No, I meant... damn it."

    f "You two are stealing my spotlight. Stand there and watch my new moves! You can drown in each other's eyes later!"

    call scene_transition_fade("black") from _call_scene_transition_fade_44

    "The two lovebirds stand together as Flandre zips around at dangerous speeds."

    return

label epilogue:

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_45

    $ remi.show(expression="neutral", blush=False, at=[far_left, standheight])
    $ pat.show(at=[center, standheight], flip=True)
    $ flan.show(at=[far_right, standheight])
    with dissolve

    "Finally, Flandre crashes into a chair."

    f "I'm tired."

    "Patchouli summons a dead chicken on Flandre's lap."

    f "Yay!"

    "She instantly dives into her new meal."

    call generic_spell

    "Then, a couch appears."

    $ pat.flip(transition=dissolve)

    p "I believe you wanted a couch?"

    $ remi.expression("smile")

    r "Yes!"

    "Remilia dives into the couch, letting her wings spread across the whole thing. Then she sits up."

    p "Glad you like it."

    "Remilia pats the spot next to her."

    $ remi.show(expression="neutral", blush=True)

    r "Come here. But don't you dare sit on my wing."

    $ remi.move(corner_left)
    $ pat.move(left, transition=move_slow)
    $ pat.flip(transition=dissolve)
    $ remi.move(scoot_right, transition=move_slow)

    "Patchouli joins her. Remilia immediately leans into her."

    $ remi.expression("smile")

    r "Thank you. I can't thank you enough."

    p "It was my pleasure. It made for a good story."

    r "Mhm."

    "Remilia looks over to a fascinated Flandre."

    $ remi.show(expression="neutral", blush=False)

    r "Stop staring."

    f "Sorry."

    r "No you're not."

    f "Hehe. You're married now."

    $ remi.expression("angry")

    r "No we are not!"

    $ flan.move(dropdowninstant, transition=move_slow)
    $ flan.hide(transition=dissolve_fast)

    "Flandre leans back, then immediately falls asleep. The chicken remains fall to the floor."

    $ remi.show(expression="neutral", at=center_left)
    $ pat.move(center, transition=move_slow)

    r "Geez, such a handful."

    p "It makes for good entertainment."

    $ remi.expression("smile")

    r "Yeah. It is."

    p "You are rather bold, stealing my lips like a prince from a fairytale."

    $ remi.expression("embarrassed")

    r "I uh, yeah. Sorry."

    p "You do not need to apologize. I thoroughly enjoyed it."

    $ remi.blush()

    r "Then, are we, um, you know? I guess... a thing?"

    p "I don't know."

    $ remi.expression("neutral")

    r "Then... I wanna be. So we are."

    p "I have no opposition to that."

    $ remi.show(expression="smile", at=scoot_right)

    "Remilia pulls herself into Patchouli."

    $ remi.move(hop(10))

    "Then, Remilia's wings envelop her."

    r "Good. You're mine."

    "They stick together silently for a few minutes."

    p "I want to show you something. I believe it will be to your liking."

    $ remi.show(expression="embarrassed", at=unscoot)

    r "W-what do you mean?"

    "Patchouli grins widely."

    p "I brought something very special when I set out to build this mansion. I've been storing it in the basement, waiting for the perfect occasion."

    r "U-um, what is it?"

    "A crate appears on the table."

    p "An ancient wine."

    $ remi.show(expression="surprised", blush=False, at=right, transition=move_fast)

    "Remilia leaps from the couch to the table."

    r "How ancient?!"

    p "Hey, come back here! I will serve us in a civil manner."

    $ remi.expression("neutral")

    r "Hmph, fine."

    $ remi.move(center_left, transition=move_slow)

    "Remilia sits back down, then Patchouli pulls her in."

    p "I'll serve it once you wrap me in your wings again."

    $ remi.expression("smile")

    r "Gladly."

    $ remi.move(scoot_right)

    "As the wings wrap around Patchouli, the crate lid flies off to the floor. Large wine bottles float up and out, lining the table."

    p "Now, shall we discuss the future over some wine?"

    $ remi.blush()

    r "Yes!"

    call scene_transition_fade("black") from _call_scene_transition_fade_46

    "As Flandre sleeps after her wing celebration, the new couple drink wine together throughout the night."

    return
