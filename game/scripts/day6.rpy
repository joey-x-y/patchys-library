label day6:
    call day6_morning from _call_day6_morning


    return


label day6_morning:

    call day_transition_in from _call_day_transition_in_4

    $ flan.show(wings="gone", at=[center_right, standheight], flip=True, transition=dissolve, zorder=5)

    "Flandre jumps out from her coffin."

    f "I'm starving..."

    $ flan.show(far_left, transition=move_slow, flip=True)

    "She goes straight to the stash of food, crunching away."

    $ remi.show([center_right, standheight], transition=dissolve, zorder=1)

    "Remilia slowly rises."

    $ remi.flip(transition=dissolve_fast)

    r "Eating so loudly so—"

    r "..."

    f "I am absolutely starving. Want one?"

    "Flandre continues eating for a few moments."

    $ flan.flip(transition=dissolve_fast)

    f "Uh, do you?"

    stop music fadeout 2.0

    r "..."

    f "What? What's wrong?!"

    $ remi.flip(transition=dissolve_fast)

    "Remilia averts her eyes."

    f "Remi?!"

    $ remi.flip(transition=dissolve_fast)

    r "..."

    $ flan.move(hop(10))

    "Flandre reaches behind to her wings and grabs them."

    f "Uh, Remi, something is..."

    r "Your wings are gone."

    f "Gone. Oh."

    $ flan.move(hopreset)
    $ flan.move(hop(10))

    "Flandre rubs her hand along the empty wing stem."

    "Remilia takes a deep breath, then slowly approaches Flandre."

    r "Hey, Flan—."

    play sound sfx_magic_cast
    call spear_summon() from _call_spear_summon_2

    "A large red sword appears in Flandre's hand and begins to glow."

    r "No, stop!"

    $ remi.move(left, transition=move_fast)
    $ remi.move(room_pacing(start_pos=0.3, distance=0.003, move_speed=0.15, pivot_pause_time=0.175))
    $ flan.move(room_pacing(start_pos=0.2, distance=0.003, move_speed=0.15, pivot_pause_time=0.175))

    "Remilia flies over and grabs Flandre. Flandre swings her sword around as Remilia holds her in place."

    r "Stop!"

    f "No! No! No! Shut up!"

    "Flandre throws elbows at Remilia's stomach."

    r "Calm down! Please!"

    f "I want my wings back!"

    r "Then please, calm down. We can have Patchouli figure something out."

    f "But, but, they're... already gone."

    $ remi.move(left)
    $ flan.move(far_left)
    $ flan.flip(transition=dissolve_fast)

    "Flandre goes limp, and puts her face in her hands, crying."

    f "They're gone! I'll never fly again!"

    $ flan.flip(transition=dissolve_fast)
    $ remi.move(at=[center_right, sitheight], transition=move_fast)
    $ remi.move(drophalf)
    with None

    $ flan.move(at=floatup, transition=move_fast)

    "Flandre shoves Remilia onto the ground, then jumps into her coffin."

    "Remilia coughs hard on the floor, holding her stomach. After her breath stabilizes, she sits up and stares at Flandre silently."

    $ remi.move(sitheight, move_slow)

    r "Flandre?"

    f "..."

    r "I'll... find Patchouli."

    f "..."

    r "Um, I'll be right back, alright?"

    $ remi.move(standheight, transition=move_slow)
    $ remi.flip(transition=dissolve_fast)
    $ remi.move(offscreenright, transition=move_slow)

    call scene_transition_fade("bg_library") from _call_scene_transition_fade_29

    $ remi.show([offscreenright, standheight], flip=True)
    with None
    $ remi.move(center_right, transition=move_slow)

    $ remi.move(drophalf, transition=move_slow)

    r "Ow... she's so strong. My stomache..."
    
    r "Ah, I don't have time to be hurt right now!"

    $ remi.move(standheight, transition=move_slow)

    call scene_transition_fade("black") from _call_scene_transition_fade_30

    "She finally stands up and flies her way to the study."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_31

    $ pat.show([right, standheight], transition=dissolve)

    $ remi.show(at=[left, standheight, enterleft(0.3)], flip=True)

    r "Patchouli! Come!"

    p "Is something amiss?"

    r "Hurry!"

    $ remi.show(enterforcefinish, flip=True)
    with None

    $ remi.move(offscreenleft, transition=ease)

    p "Hmm."

    call scene_transition_fade("bg_bedroom") from _call_scene_transition_fade_32

    $ flan.show([far_left, standheight, floatup])
    $ remi.show([center_right, standheight], transition=dissolve)

    $ pat.show([far_right, standheight, enterright()])

    "Patchouli flies behind Remilia into the bedroom. Flandre is leaning back in her coffin, blankly staring at the ceiling. Her gaze snaps to them as they enter."

    f "Go away! Leave me alone!"

    p "Um..."

    r "Flandre... she wants to help you."

    f "Leave me alone!"

    $ flan.flip(transition=dissolve_fast)
    $ flan.move(hopreset, transition=move_fast)

    "Flandre turns and curls herself into a ball, revealing her decayed wings."

    p "...What?"

    r "Mhm... She's not taking it well."

    p "Damn it! They're already gone?"

    $ remi.flip(transition=dissolve_fast)

    r "Uh, hey, Patchouli?"

    p "What can I—"

    $ pat.move(enterforcefinish)
    $ pat.flip()
    with None
    $ pat.move(offscreenright, transition=ease)

    r "Hey!"

    $ remi.flip(transition=dissolve_fast)
    pause 0.2
    $ remi.flip(transition=dissolve_fast)
    pause 0.2
    $ remi.flip(transition=dissolve_fast)

    "She looks back and forth between the door and Flandre's deadly glare."
    
    $ remi.flip(transition=dissolve_fast)
    $ remi.move(offscreenright, transition=move_fast)

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_33

    $ pat.show([center_left, sitheight], transition=dissolve, zorder=5)
    $ remi.show([corner_left, standheight, enterleft()])
    pause 0.2
    $ pat.move(drophalf)

    r "What are you doing?"

    p "I want... to do... something."

    r "Slow down, would you? Aren't you weak?"

    $ pat.move(standup)

    p "I'm fine."

    $ pat.move(center, transition=MoveTransition(0.5, time_warp=_warper.ease))
    $ pat.move(drophalf)

    r "Stop! Just sit down!"

    $ remi.move(enterforcefinish)
    with None
    $ remi.move(center_left, transition=ease)
    $ remi.move(floatup)
    with None
    $ pat.move(standheight, transition=ease)

    $ remi.move(center_right)
    $ pat.move(right, transition=ease)

    $ pat.show(sitheight, flip=True)
    $ remi.move(center_left, transition=ease)

    play music bgm_emotional fadein 2.0
    call table_zoom_l from _call_table_zoom_l_5

    $ remi.move(hopreset)
    with None
    $ remi.move(sitheight, transition=move_slow)

    "She drops Patchouli onto her chair, then sits across from her. Patchouli breathes hard for a full minute before recovering."

    p "Sorry."

    $ remi.flip(transition=dissolve)
    $ remi.flip(transition=dissolve)

    "Remilia looks to the door and back, lets out a deep breath as she drops her head in tears."

    call show_transition_fade("bg_study") from _call_show_transition_fade_6

    "Nobody speaks for a few minutes."

    r "Hey. Patchouli?"

    p "What?"

    r "What now?"

    p "I do not know."

    r "Can't you do something?"

    p "Do what?!"

    r "Never mind. Sorry."

    "Patchouli crosses her arms and looks down."

    p "I screwed it up. Working so slow."

    $ remi.move(drophalf)

    "Remilia curls into a ball and buries her face."

    r "It was never even your problem to begin with. This is all my fault."

    p "I made it my problem."

    "Patchouli looks over to Remilia, then looks back down."

    call table_unzoom_l from _call_table_unzoom_l_2
    stop music fadeout 2.0

    $ pat.move([center_right, standheight], transition=move_slow)

    "She takes a deep breath, then slowly floats over."

    p "Um... Remilia?"

    $ remi.move(sitheight, transition=move_slow)
    $ remi.move([center, standheight], transition=move_fast)

    play music bgm_ending fadein 2.0
    show cg_hug zorder 8 with dissolve

    r "I'm sorry Patchy!"

    "She cries directly into Patchouli's chest."

    p "U-um, uh..."

    "After a moment, Patchouli gently puts her arms around, and finds herself crying as well."

    r "I'm so useless."

    p "...You're not."

    r "Not good enough."

    p "You are."

    "Remilia squeezes."

    r "I let this all happen in the first place! I'm too weak..."

    p "..."

    "They hold on to each other silently for a long time."

    show cg_hug with fade

    "Eventually, Remilia gently let's go."

    hide cg_hug with dissolve
    
    $ remi.move(left, transition=ease)

    r "Uh, sorry. Thanks. Um, yeah."

    p "Mhm."

    r "I, uh, feel a little better. Thank you."

    p "Yeah, um, yeah. Right. I don't know what I'm doing."

    r "Ha, me neither."

    stop music fadeout 2.0
    play music bgm_emotional fadein 2.0

    $ remi.show(corner_left, flip=True, zorder=6)
    $ pat.show(right, transition=move_slow, flip=True)
    $ pat.show(sitheight, flip=True)

    $ remi.flip(transition=dissolve)

    "Remilia walks away, circling the room. Patchouli sits back down."

    r "So... what now? Ugh, I already asked you that."

    p "Shouldn't you go back to your sister?"

    r "I doubt that's a good idea, she prefers time alone in these situations. I don't want to make her snap."

    p "Oh."

    $ pat.move(hopdown(10, 0.4))

    "Patchouli brings up her legs, tucking them knees into her chest."

    $ remi.move(left, transition=ease)

    r "It's foolish to blame yourself for this. You have already done more for us than anyone ever has."

    p "But I have not done what was promised."

    r "You clearly made an effort."

    p "I don't care. I want to fix those wings."

    r "Mm, any ideas?"

    p "No."

    r "Is there anything you need to study? Shall I fetch you a book?"

    p "There really isn't anything to study. I don't know. I need to think."

    $ remi.flip(transition=dissolve)

    r "I understand. Want me to leave you alone?"

    p "No. Stay."

    $ remi.flip(transition=dissolve_fast)
    $ remi.move([center_left, sitheight], transition=ease)

    r "Sure."

    call show_transition_fade("bg_study") from _call_show_transition_fade_7

    "Hours pass in silence, with Remilia occasional pacing, and Patchouli skimming books, thinking, and putting them away."

    r "Hey, need anything?"

    p "I'm not sure."

    r "Hmm."

    "Remilia walks over to Patchouli."

    $ remi.move([center, standheight], transition=ease)

    r "Here."

    p "...What?"

    "Remilia puts her hands to her chest, turning to the side and sticking her wing out."

    r "I present to you, the pride and soul of all vampires. My gorgeous wings. You wanted to study them. Here you go."

    $ pat.move(standheight, transition=ease)

    "Patchouli stands and smiles."

    p "Oh, I see. You're finally letting Patchy touch your wings?"

    r "Shut up! I'm never calling you that again. Just do it already."

    #TODO wing cg

    $ pat.move(center_right)
    $ remi.show(transition=dissolve, flip=True, zorder=5)

    "Patchouli grabs the wings, thoroughly handling them and feeling each individual part."

    r "Do you need to touch them like that?"

    p "Yes."

    r "Ugh."

    "Ten minutes pass. Then thirty."

    r "How long..."

    p "Hey, Remilia?"

    r "What!"

    p "May I ask a few questions about how wings work?"

    r "Fine. My wealth of knowledge makes me the most qualified. You could not have found anyone better."

    p "What exactly is their function?"

    r "They show the beauty—"

    p "Function."

    r "Ugh, fine. Flight."

    p "Mhm. Anything else."

    r "Um... they are sensitive... help with balance... hmm. I think that's it."

    p "How sensitive?"

    "Patchouli squeezes."

    r "Very! Now stop!"

    p "I simply couldn't resist."

    r "What am I even doing right now..."

    p "Do they have an effect on a vampire's abilities? Outside of flight?"

    r "No. Flandre can do what she normally does, but her balance is poor."

    p "Hm. Interesting. I have much to look into now."

    r "Then let go already!"

    p "Oh."

    # TODO end wing cg

    $ remi.move(corner_left)
    $ pat.move(right, transition=move_slow)

    "Patchouli releases the noble wings."

    $ remi.flip()

    r "Finally! I hope you understand the elegance of wings now."

    p "I do. Thank you."

    $ remi.move(left, transition=move_slow)

    "Remilia approaches Patchouli with a smug smile."

    r "That was a privilege that nobody else in this world has ever experienced. Remember that."

    p "I will."

    "Remilia's smile drops as she looks to the door,"

    r "I should see Flandre now. It shouldn't be put off any longer."

    p "Mm. Good luck."

    $ remi.show(corner_left, transition=move_slow, flip=True)

    $ remi.flip(transition=dissolve)

    r "Um, Patchouli?"

    p "Yes?"

    r "Can you... come with me?"

    p "Would I be helpful?"

    $ remi.flip(transition=dissolve_fast)

    r "No, never mind. This is foolish of me. I'm leaving."

    $ remi.move(offscreenleft, transition=move_slow)

    stop music fadeout 2.0

    call scene_transition_fade("bg_library_stairs") from _call_scene_transition_fade_34

    $ remi.show([center_left, standheight], transition=dissolve, flip=True)

    "She takes a long slow, deep breath."

    r "I have to face her eventually. Come on."

    call scene_transition_fade("black") from _call_scene_transition_fade_35

    "She slowly walks down the stairs, and eventually makes it to the bedroom door."

    "She puts her hand on the doorknob and pauses."

    "She takes a deep breath."

    "She enters."

    call scene_transition_fade("bg_bedroom") from _call_scene_transition_fade_36

    $ flan.show([far_left, standheight, floatup], transition=dissolve, flip=True)
    $ remi.show([right, standheight, enterright()], flip=True)

    "Flandre is sitting in her coffin, unmoved from before. Dried tears cover her face."

    r "Hello, Flandre."

    f "Hi."

    $ remi.move(left, transition=move_slow)
    $ flan.move(hopreset, transition=move_slow)

    "Remilia walks to the bed and hugs her. Flandre leans into her."

    f "They're gone."

    r "Don't worry, Patchouli is working on it."

    f "I am worried. Shut up."

    r "Right. Sorry."

    f "Stop apologizing."

    r "I will."

    f "Never apologize again."

    r "I will. So— So yeah, I'll stop."

    f "You can let go now."

    r "Right, of course."

    $ remi.move(center_right, transition=ease)

    f "If you blame yourself again, I'll hit you."

    r "Right."

    play sound sfx_coffin_close
    $ flan.hide(transition=dissolve)

    "Flandre closes her coffin lid, as Remilia exhales heavily."

    r "..."

    call scene_transition_fade("black") from _call_scene_transition_fade_37

    "She climbs into her coffin and falls asleep instantly."

    return
