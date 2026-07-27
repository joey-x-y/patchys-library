label day7:

    call day7_morning from _call_day7_morning
    call epilogue from _call_epilogue

    $ persistent.beat_game = True

    return

label day7_morning:

    call day_transition_in from _call_day_transition_in_5

    $ remi.show([center_right, standheight, enterbottom(0.75)], flip=True)

    pause 0.75

    $ flan.show(expression="frown", at=[far_left, standheight, enterbottom()])
    $ remi.move(enterforcefinish)
    with None
    $ remi.flip(transition=dissolve_fast)

    r "Um... hello, Flandre. Are you doing alright?"

    f "Sure. Sorry for hitting you."

    play music bgm_library fadein 2.0

    $ remi.show(expression="smile", at=hop(10))

    "Remilia stands and puts her hands on her hips."

    r "Don't worry, I'm durable. I can bounce back from a few elbows."

    $ flan.expression("neutral")

    f "Heh, would that still be true if I hit you hard?"

    $ remi.expression("surprised")

    r "Uh... didn't you?"

    $ remi.expression("annoyed")
    $ flan.show(expression="frown", at=corner_right, transition=move_slow)
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

    f "Good enough."

    r "I could at least hold your hand."

    $ flan.show(expression="neutral", flip=True, transition=dissolve, zorder=3)

    f "...Fine."

    $ remi.show(expression="smile", at=center, transition=move_slow)
    $ flan.flip(transition=dissolve)

    pause 0.25

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_39

    $ pat.show([right, standheight], transition=dissolve)

    $ flan.show(expression="frown", at=[center_left, standheight, enterleft()], flip=True)
    $ remi.show(expression="neutral", at=[left, standheight, enterleft()], flip=True)

    "As they arrive, Patchouli looks up from her mountain of books and scrolls."

    $ pat.show(expression="curious")

    p "Ah, Flandre."

    f "Hi."

    $ pat.expression("confused")

    p "I'm, uh, sorry about your wings."

    f "Don't apologize for it. What's the plan now? Is there any hope?"

    $ pat.expression("neutral")

    p "I have been... thinking."

    p "I was trying to restore your wings, but now I have to think about how they could be replaced in their entirety."

    $ flan.expression("question")

    f "Huh. New wings? How's that work?"

    p "I don't know. Even though Remilia let me explore her wing anatomy, I'm unsure how I could replicate it."

    $ remi.expression("angry")

    r "Hey!"

    f "You what about anata what?"

    $ remi.expression("annoyed")
    $ pat.expression("curious")

    p "I got a feel of Remilia's wings, taking note of how the flaps and stem feel and connect with each other. I touched them as thoroughly as I could to try and fully understand them."

    $ remi.blush()
    $ flan.show(blush=True, at=enterforcefinish)
    with None
    $ flan.show(flip=True, at=center, transition=dissolve)

    "A shocked Flandre looks over to a tomato-faced Remilia."

    r "Shut up!"

    $ flan.show(expression="frown", blush=False)

    f "But I haven't made fun of you yet."

    $ flan.show(flip=True, at=center_left, transition=dissolve_fast)
    $ pat.show(at=center_right, transition=ease, zorder=7)

    "Patchouli's head snaps to the wings."

    p "I would like to touch them more. May I?"

    $ remi.show(expression="neutral", at=scoot_left)
    $ flan.show(expression="question", blush=True)

    r "I am not such an indecent vampire! I don't do such uncouth things on request!"

    $ remi.move(unscoot)
    $ flan.expression("frown")

    f "I shouldn't leave you two alone together."

    $ remi.expression("angry")

    r "I said shut up!"

    $ remi.show(expression="neutral", at=center_left)
    $ flan.show(expression="neutral", at=corner_left, transition=move_slow)

    "Remilia sighs as she walks over to Patchouli."

    r "Fine."

    $ pat.expression("smile")

    p "Thank you."

    show cg_wingtouch zorder 8 with dissolve

    "Patchouli grasps the wings. Flandre stares intently."

    p "I must say, it is rather nice."

    r "Are you doing this to me on purpose?"

    p "Forbidden knowledge has an appeal."

    r "That doesn't answer my question."

    p "I believe it does."

    $ flan.show(expression="surprised", at=closeup, zorder=9)

    f "Are you in love?"

    r "Be quiet!"

    p "I am satisfied."

    $ flan.show(expression="neutral", at=closeuprevert)
    hide cg_wingtouch with dissolve

    $ remi.move(left)
    $ pat.move(right, transition=move_slow)

    f "Were they nice, Patchy?"

    r "Ugh..."

    $ pat.expression("think", transition=dissolve_fast)

    "Patchouli stands with her eyes vacant and arms folded, unresponsive."

    f "Looks like a yes."

    $ flan.show(blush=False, zorder=2)
    $ remi.show(flip=True, transition=dissolve_fast)

    "Remilia walks in front of Flandre to flail her arms."

    $ remi.expression("angry")

    r "I showed her so she can understand wings more, to help with fixing yours. That is all. Understand?"

    f "Sure. Whatever you say."

    $ remi.expression("neutral")

    r "Oh... but—"

    $ pat.expression("surprised")
    $ remi.show(expression="surprised", blush=False, at=hop(10))
    $ flan.show(expression="surprised", at=hop(10))

    p "But that doesn't even matter!"

    $ pat.show(expression="smile", at=floatup, transition=move)
    $ flan.expression("question")
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
    $ flan.show(expression="smile", at=far_left, transition=move_slow)

    r "Hey, what's the plan exactly?"

    $ pat.expression("curious")

    p "I will imbue these crystals with the same magic I use to move objects, and embed it into her wing stems. If she applies magical energy to her stems, it will react with the crystals."

    r "Huh."

    f "That sounds super cool!"

    $ pat.expression("smile")

    p "Yes, I just need to think about how to implement that without them exploding on your back."

    $ flan.expression("frown")

    f "Oh."

    $ pat.expression("confused")

    p "Is trial and error acceptable? That would be fastest, and I believe your regeneration capabilities would be sufficient for survival."

    $ flan.show(expression="surprised", at=hop(10))

    f "No! Use Remi!"

    $ flan.expression("neutral")

    r "No. Regeneration doesn't prevent pain."

    $ pat.expression("neutral")

    p "I can numb your body."

    $ remi.show(expression="angry", at=scoot_right)

    r "No! You're insane!"

    $ remi.show(expression="neutral", at=unscoot)

    p "Fair enough."

    $ pat.move(hop(10))

    "Patchouli takes a long exhale."

    $ pat.expression("serious")

    p "Enough goofing off. Now, Flandre, I do believe you know how to use magical energy, right?"

    $ flan.expression("smile")

    f "Yeah! Like this!"

    play sound sfx_magic_cast
    call spear_summon from _call_spear_summon_3

    $ pat.expression("smile")

    "She summons her sword."

    $ remi.show(expression="annoyed", flip=True)

    r "Put that away!"

    $ flan.show(expression="frown", blush=True)

    f "Sorry."

    call spear_summon from _call_spear_summon_4

    $ remi.expression("neutral")
    $ flan.blush(False)

    "The sword disappears."

    $ remi.flip(transition=dissolve_fast)
    $ pat.move(hop(10))

    p "Perfect! This should work. Give me some time."

    $ flan.flip()
    $ flan.show(expression="smile", at=hop())

    f "Woohoo!"

    $ flan.expression("neutral")

    r "Would you like any help?"

    $ pat.show(blush=True, at=center, transition=move_fast, zorder=2)
    play sound sfx_rustle_2
    $ remi.move(small_shake)

    "Patchouli grabs Remilia by the shoulders."

    p "Yup! I'll work you to the bone."

    $ remi.show(expression="embarrassed", blush=True)

    r "Mm. Right."

    $ flan.show(expression="frown", flip=True)

    f "So touchy. Bleh."

    call scene_transition_fade("black") from _call_scene_transition_fade_40

    "Over the next few hours, Patchouli imbues various magical crystals as Remilia runs around gathering materials. Flandre lies on the ground reading about mercury."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_41

    $ remi.show(expression="neutral", blush=False, at=[center_left, standheight])
    $ pat.show(blush=False, at=[center_right, standheight])
    $ flan.show([corner_left, sitheight], flip=True)
    with dissolve

    p "Got it! This is stable! I think. Now for a test. Hold this, Remilia."

    $ pat.show(magic=False, transition=dissolve_fast)

    "She takes the crystal."

    $ pat.expression("serious")

    p "Now, put a little energy into it."

    play sound sfx_magic_summon
    call generic_spell from _call_generic_spell_11
    with None
    $ remi.move(floatup, transition=move_slow)
    
    "Remilia slowly floats into the air."

    $ pat.expression("smile")
    $ remi.expression("surprised")

    r "Whoa. Neat."

    $ remi.expression("smile")

    p "Perfect. Now we attach these to the wing stems."

    $ flan.flip()

    r "Incredible!"

    $ flan.show(expression="question", at=[far_left, standheight], transition=ease, zorder=7)

    f "What's going on?"

    p "I believe the problem has been solved."

    $ flan.show(expression="smile", at=hop(length=0.25))

    f "Yay! Yay!"

    $ pat.move(hop(10))
    with None
    $ remi.move(hopreset, transition=move_fast)

    "Patchouli swipes the crystal from Remilia's hand."

    r "That was truly incredible. You're brilliant."

    $ pat.blush()

    p "Ehem, yes, of course. Now lie down, Flandre. I will attach them."

    $ pat.blush(False)
    $ flan.move(hopreset)
    with None
    $ flan.show(right, transition=move_fast, zorder=1)
    play sound sfx_body_fall

    $ remi.expression("neutral")

    r "Don't damage the table with your dive-bombing."

    $ flan.expression("frown")

    f "This is my moment. Silence."

    $ remi.expression("smile")

    r "Fine, fine."

    call scene_transition_fade("black") from _call_scene_transition_fade_42

    stop music fadeout 2.0

    "Patchouli floats over Flandre. One by one, she places a crystal onto a wing stem, casts a spell, and it sticks. Eventually, she's done and floats away."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_43

    $ remi.show(expression="neutral", at=[corner_left, standheight])
    $ flan.show(wings="crystal", at=[right, sitheight], flip=True)
    $ pat.show(expression="serious", at=[left, standheight], flip=True, magic=False)
    with dissolve

    p "Listen to me closely. Stand up, slowly. Very carefully."

    f "Slowly. Got it."

    play sound sfx_crystals_clacking
    $ flan.move(standheight, transition=move_slow)

    "The crystals sway back and forth as she moves up."

    $ flan.expression("smile")

    f "Wow! Musical wings!"

    $ pat.expression("confused")

    p "Wait, no, hold on. Don't move."

    $ flan.expression("frown")

    $ pat.show(center, transition=move_fast)
    call generic_spell from _call_generic_spell_12
    $ pat.show(expression="neutral", at=left, transition=move_fast)

    p "Continue."

    $ flan.move(floatup, transition=move_slow)

    p "How is your balance?"

    $ flan.expression("neutral")

    f "Good! Kind of."

    p "Now, just apply the smallest amount of magical energy."

    $ flan.show(expression="smile", at=room_pacing(0.5, 0.7, 0.06, 0.15))

    "Flandre starts flipping in the air."

    p "How is it?"

    f "Awesome! Amazing! Absolutely astonishing!"

    $ remi.expression("smile")
    $ pat.expression("smile")

    p "Good."

    f "I can fly! I can fly! Fly! Fly! Bird!"

    $ flan.move(offscreenright, transition=move_fast)

    "She zooms around the room, faster than eyes can follow."

    $ pat.expression("serious")

    p "Hey!"

    r "Give up. She won't stop."

    play music bgm_title fadein 2.0

    $ remi.show(blush=True, at=center_left)
    $ pat.show(expression="annoyed", at=center_right, flip=True, transition=move_slow, zorder=2)

    p "I guess not. I trust you'll clean her messes? Fallen bookshelves are a pain."

    $ remi.expression("embarrassed", transition=dissolve)

    "Remilia's gaze flicks to the side and back to Patchouli a few times, her face steadily turning red."

    $ pat.blush(transition=dissolve)

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

    show f crystal frown onlayer screens at corner_right, closeup

    f "The moment I look away."

    call dismiss_cg from _call_dismiss_cg_3

    $ remi.show(expression="surprised", at=far_left)
    $ pat.move(right, transition=move_fast)

    "They jump apart."

    $ flan.show(expression="frown", at=corner_right, transition=dissolve)
    $ remi.expression("angry")

    r "She was just, checking something!"

    $ remi.expression("neutral")
    $ flan.expression("frown")

    f "Sure... sure. Give up, lovebirds. How many kisses was that?"

    $ pat.show(flip=True, expression="smile", at=center_right, transition=ease)

    p "Three."

    f "How many before today?"

    $ pat.expression("annoyed")

    p "Zero, sadly."

    $ remi.expression("annoyed")

    r "Patchy, don't tell her."

    $ pat.expression("smile")

    f "Patchy?"

    $ remi.expression("embarrassed")

    r "No, I meant... damn it."

    $ flan.expression("question")

    f "You two are stealing my spotlight. Stand there and watch my new moves! You can drown in each other's eyes later!"

    call scene_transition_fade("black") from _call_scene_transition_fade_44

    "The two lovebirds stand together as Flandre zips around at dangerous speeds."

    return

label epilogue:

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_45

    $ remi.show(expression="neutral", blush=False, at=[far_left, standheight])
    $ pat.show(expression="neutral", blush=False, at=[center, standheight])
    $ flan.show(expression="frown", at=[far_right, standheight])
    with dissolve

    "Finally, Flandre crashes into a chair."

    f "I'm tired."

    call generic_spell

    $ flan.expression("neutral")

    "Patchouli summons a dead chicken on Flandre's lap. She instantly dives into the new meal."

    call generic_spell

    "Then, a couch appears."

    $ pat.flip(transition=dissolve)

    p "I believe you wanted a sofa?"

    $ remi.expression("smile")

    r "Yes!"

    $ remi.move(sitheight, transition=move_fast)

    "Remilia dives headfirst into the couch, letting her wings spread across the whole thing. Then finally, she sits up."

    $ pat.expression("smile")

    p "You sure do like it."

    "Remilia pats the spot next to her."

    $ remi.show(expression="neutral", blush=True)

    r "Come here. But don't you dare sit on my wing."

    $ pat.show(at=center_left, transition=move_slow)
    $ pat.show(flip=True, blush=True, at=sitheight, transition=move_slow)
    $ remi.move(scoot_right(50))
    $ flan.expression("frown")

    "Patchouli sits next to Remilia, and the vampire leans into her with no hesitation."

    $ remi.expression("smile")

    r "Thank you. I can't thank you enough."

    p "It was my pleasure. An intriguing puzzle, and a good story besides."

    r "Mhm."

    $ flan.expression("question")

    "Remilia looks over to a fascinated Flandre."

    $ remi.show(expression="neutral", blush=False)

    r "Stop staring."

    f "Sorry."

    r "No you're not."

    $ flan.expression("smile")

    f "Hehe. You're married now."

    $ remi.expression("angry")

    r "No we are not!"

    $ flan.move(dropdowninstant, transition=move_slow)
    $ flan.hide(transition=dissolve_fast)

    "Flandre leans back, then immediately falls asleep. The chicken remains fall to the floor."

    call left_zoom_l

    $ remi.expression("neutral")

    r "Geez, such a handful."

    $ pat.show(expression="neutral", blush=False, transition=dissolve_fast)

    p "She makes for quality entertainment."

    $ remi.expression("smile")

    r "I guess so."

    $ pat.show(expression="smile", blush=True)

    p "You are rather bold, stealing my lips like a prince from a fairytale."

    $ remi.expression("embarrassed")

    r "I uh, yeah. Sorry."

    p "You do not need to apologize. I thoroughly enjoyed it."

    $ remi.blush()

    r "Then, are we, um, you know? I guess... a thing?"

    $ pat.expression("confused")

    p "I don't know."

    $ remi.expression("neutral")

    r "Then... I wanna be. So we are."

    $ pat.expression("smile")

    p "I have no opposition to that."

    $ remi.show(expression="smile", at=scoot_right(100))

    "Remilia pulls herself into Patchouli."

    $ remi.move(hop(10, 0.3))

    "Then, Remilia's wings envelop her."

    r "Good. You're mine."

    $ pat.expression("neutral")

    "They stick together silently for a few minutes."

    p "I want to show you something. I believe it will be to your liking."

    $ remi.show(expression="embarrassed", at=unscoot)

    r "W-what do you mean?"

    $ pat.expression("smile")

    "Patchouli grins widely."

    $ pat.show(expression="curious", at=[scoot_right, left], blush=False, flip=True, transition=dissolve_fast)

    p "I brought something very special when I set out to build this mansion. I've been storing it in the basement, waiting for the perfect occasion."

    r "U-um, what is it?"

    call generic_spell

    "A crate appears on the table."

    $ pat.expression("smile")

    p "An ancient wine."

    $ remi.show(expression="surprised", blush=False, at=[center_right, standheight], transition=move_fast)
    $ pat.expression("annoyed")

    r "How ancient?!"

    $ pat.show(expression="serious", at=[center_left], flip=True)

    p "Come back here, you animal! I will serve us in a civil manner."

    $ remi.expression("neutral")

    r "Hmph, fine."

    $ pat.expression("neutral")
    $ remi.move(at=[far_left, sitheight], transition=move_slow)
    $ remi.move(at=scoot_right(100), transition=move_slow)

    "Remilia sits back down, then Patchouli pulls her in."

    $ pat.show(expression="smile", blush=True)

    p "I'll serve it once you wrap me in your wings again."

    $ remi.expression("smile")

    r "Gladly."

    $ remi.move(hop(10, 0.3))

    "As the wings wrap around Patchouli, the crate lid flies off to the floor. Large wine bottles float up and out, lining the table."

    p "Now, shall we discuss the future over some wine?"

    $ remi.blush()

    r "Yes!"

    call scene_transition_fade("black") from _call_scene_transition_fade_46

    "As Flandre sleeps after her wing celebration, the new couple drink wine together throughout the night."

    return
