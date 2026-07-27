label day2:
    call day2_morning from _call_day2_morning
    call day2_library from _call_day2_library
    call day2_end from _call_day2_end

    return

label day2_morning:
    call day_transition_in() from _call_day_transition_in

    play sound sfx_coffin_open

    $ remi.face(flipped=False)
    $ remi.show(tired=False, expression="smile", at=[left, standheight, enterbottom()], zorder=5)
    
    "Remilia rises out of her coffin and stretches."

    r "I feel rested. Finally."

    "She looks over to Flandre's coffin."

    $ remi.show(expression="neutral", at=enterforcefinish)

    r "She's still asleep. Now how can I get us out of here?"

    f "No, I'm awake."

    play sound sfx_coffin_open

    $ flan.face(flipped=False)
    $ flan.show(expression="frown", at=[right, standheight, enterbottom(0.5)])

    r "Oh. Did your wings let you sleep?"

    f "For a little, then the numbness wore off. It was comfy inside, so I didn't wanna get up."

    r "You could've woken me up."

    f "No, you needed sleep."

    r "Fair enough. I was exhausted."

    f "And don't try to escape. We'll explode."

    $ remi.expression("smile")

    r "She's bluffing. Besides, she can't take me at full power. It would be a slaughter."

    f "Please don't. I don't think she'll harm us if we don't do anything."

    $ remi.expression("neutral")

    r "We're her test subjects. Who knows what she'll do?"

    $ flan.expression("holding_tear")

    f "Please, Remi. I'm tired of moving every night. I want my wings numbed again."

    $ remi.expression("annoyed")

    r "Alright, fine. I won't do anything."

    $ remi.expression("neutral")

    r "But don't be careless. This is hostile territory."

    $ flan.expression("frown")

    f "I'll be careful."

    $ remi.expression("smile")

    r "Good. Thank you."

    $ flan.show(expression="neutral", at=right)
    with None
    $ flan.flip(transition=move_fast)

    f "I'm gonna ask her to numb my wings now."

    play sound sfx_door_open
    $ flan.hide(transition=dissolve)

    $ remi.expression("surprised")

    r "Hey, wait!"

    call scene_transition_fade("bg_library") from _call_scene_transition_fade_6

    $ remi.face(flipped=True)
    $ flan.face(flipped=False)

    $ flan.show(expression="frown", at=[center, standheight], zorder=2, transition=dissolve)
    $ remi.show(expression="neutral", at=[right, standheight, enterright()])
    
    r "Don't go alone! You just said you'd be careful."

    $ flan.expression("neutral")

    f "Yeah, let's go together."

    r "Of course we will, but don't wander off like that."

    call generic_spell() from _call_generic_spell_3

    p "Go up the stairs."

    "The magician's voice echoes throughout the room."

    $ flan.expression("question")

    f "Whoa, cool."

    $ flan.expression("neutral")

    r "She's watching us. Great."

    "Remilia stares at the exit. Then, they walk to the staircase."

    r "I can fly you up."

    $ flan.blush()

    f "Um, no need for that. We can walk."

    $ flan.blush(False)

    "Remilia nods and follows Flandre to the stairs."

    call show_transition_fade("bg_library_stairs") from _call_show_transition_fade_2

    "She looks around as they ascend. Books everywhere, along with fancy chandeliers lining the ceiling."

    r "You think she's read all those?"

    f "No. Too many."

    $ remi.expression("smile")

    r "I bet."

    stop music fadeout 2.0

    "They reach the top, approaching a large door."

    p "You may enter."

    $ remi.show(center_right, transition=move_slow)

    play sound sfx_door_open

    "Remilia grabs Flandre's hand as they enter together."

    return

label day2_library:

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_7

    play music bgm_library fadein 2.0

    $ pat.show(hat=False, expression="smile", flip=True, at=[right, sitheight], transition=dissolve, zorder=2)

    "They step into yet another room lined with even more books. Patchouli sits in front at her desk large desk."

    $ remi.face(flipped=False)
    $ flan.face(flipped=True)

    $ remi.show(expression="neutral", at=[left, standheight, enterleft()])
    $ flan.show(at=[corner_left, standheight, enterleft()])

    p "Welcome to my study."

    $ pat.move(standheight, transition=move_slow)

    "She stands dramatically, gesturing her arms out wide."

    p "My vast collection of knowledge lies before you."

    $ flan.show(expression="question", at=enterforcefinish)
    $ remi.move(enterforcefinish)
    with None

    $ flan.expression("question")

    f "Whoa, cool!"

    $ flan.expression("neutral")

    r "Apply that numbing spell again, would you?"

    $ pat.expression("annoyed")

    p "Hold a moment."

    $ pat.show(magic=True, transition=dissolve_fast)
    call generic_spell() from _call_generic_spell_4
    $ remi.show(dirty=False, at=enterforcefinish)
    $ flan.show(dirty=False, at=enterforcefinish)
    with dissolve

    $ pat.show(magic=False, transition=dissolve_fast)

    p "I would appreciate it if you don't sully my carpets on your way in."

    $ remi.expression("smile")

    r "Oh, you can clean people with magic? Useful."

    $ pat.expression("neutral")

    f "You don't stink any more, Remi! Finally."

    $ pat.expression("smile")
    $ remi.show(expression="angry", flip=True, at=hop(20))

    r "What?!"

    $ pat.show(expression="neutral", magic=True)

    p "Now come here. I will numb your wings longer this time."

    $ remi.show(expression="neutral", flip=True, at=hopreset)
    $ flan.move(center_right, transition=ease)

    call generic_spell() from _call_generic_spell_5

    $ flan.show(center, zorder=1, transition=move_slow)
    $ pat.show(magic=False, transition=dissolve_fast)
    $ flan.expression("frown")

    f "Thank you... uh, what's your name?"

    $ magician_name = real_magician_name

    p "Patchouli."

    $ flan.expression("smile")

    f "Thank you Patchouli! I'm Flandre Scarlet, that's my cranky sister Remilia Scarlet!"

    p "Well met, Scarlets."
    
    $ flan.expression("question")

    f "Where'd your cool hat go?"

    p "Hm, just not in the mood for it today."

    $ flan.expression("frown")

    f "Aw."

    $ remi.move(at=center_left)
    $ flan.show(expression="neutral", at=far_left)
    with move_slow

    r "What do you intend to do with us?"

    p "Observe. Study. Gather useful data."

    r "What exactly do you mean by that?"

    $ flan.show(expression="frown", at=left, transition=move)
    $ remi.move(shake(0.5))

    play sound sfx_rustle_3

    "Flandre tugs the back of Remilia's dress."

    f "You're being rude."

    $ remi.expression("serious")

    r "I must know. I will only tolerate so much. I have dignity I wish to maintain."

    $ pat.expression("smile")

    p "I'm not a mad magician, I won't do anything too harsh. I just want to understand vampires more. I've never seen one. It's fascinating."

    $ pat.expression("curious")
    
    p "Why does simple sunlight hurt them when they are so durable? There are many questions to be answered."

    r "So we are your entertainment?"

    $ pat.expression("think")

    p "Hmm. Yeah."

    $ remi.expression("annoyed")
    $ pat.expression("neutral")

    r "Great."

    $ remi.expression("neutral")

    play sound sfx_rustle_3

    $ remi.move(far_left)
    with move_slow

    "Flandre gently tugs again, and Remilia reluctantly steps back next to her."

    $ flan.expression("question")

    f "She's done. You can ask stuff now."

    $ pat.expression("curious")
    $ flan.expression("neutral")

    p "So I shall. For my first question, I believe vampires have the ability to regenerate themselves, correct?"

    r "Yes, if they rest."

    p "Is Flandre not a vampire?"

    $ flan.show(expression="smile", at=hop)

    f "I am!"

    p "Your wings aren't regenerating."

    $ flan.move(hopreset)
    $ flan.show(expression="frown", at=small_shake())

    f "Uh, yeah."

    r "She couldn't sleep enough, your numb spell was too short."

    $ flan.expression("serious")

    f "That's not the problem. Don't blame her. They haven't healed at all, no matter what we do."

    p "What caused the injury?"

    $ flan.expression("frown")

    "Flandre crosses her arms and looks down."

    f "Um... well, a blade. It burned."

    p "What kind of blade?"

    $ flan.move(shakereset)
    $ flan.show(expression="holding_tear", at=small_shake(7, 0.2))

    f "Uh... I don't know!"

    $ pat.expression("neutral")
    $ flan.expression("frown")
    $ remi.show(scoot_right, expression="serious")
    play sound sfx_rustle_3

    "Remilia gently puts her hands on Flandre's shoulders."

    r "That's quite enough."

    p "I suppose it is. I have an idea now."

    $ remi.expression("neutral")
    $ flan.expression("holding_tear")

    "Flandre looks down at Patchouli's shoes."

    f "Um... if it's not too much trouble, do you think you can fix them? Please?"

    $ pat.expression("think")

    p "Hmm... that would make for an interesting project."

    $ remi.expression("smile")

    r "Marvelous idea. This will make for a fine vampiric study."

    $ pat.expression("annoyed")

    p "When you put it like that... never mind."

    $ flan.expression("surprised")
    $ remi.expression("serious")

    r "What?! I thought you wanted to!"

    p "The way you suggest things... it is rather bothersome..."

    r "How so?"

    $ flan.expression("angry")

    f "Be quiet, Remi."

    $ remi.show(unscoot, expression="neutral")
    $ flan.show(expression="frown", at=center_left)
    with move_slow

    $ flan.show(zorder=7)

    "Flandre steps forward out of Remilia's grip. Remilia's mouth opens, then silently closes."

    $ flan.expression("holding_tear")

    f "U-um..."

    $ pat.expression("neutral")
    $ flan.move(hopdown(height=10, length=0.3))
    pause 0.3

    f "Patchouli, could you try? The pain... I hate it. Please. I'll help however you want."

    $ remi.show(expression="annoyed", at=hopdown(length=0.5))

    "Remilia bows her head."

    r "Please heal my sister."

    $ pat.expression("think")
    $ remi.show(expression="neutral", at=hopreset)

    "Patchouli sighs."

    $ pat.expression("neutral")

    p "Very well."

    $ remi.expression("smile")
    $ flan.expression("question", transition=dissolve_fast)

    f "W-will you really? Are you sure?"

    $ pat.expression("annoyed")

    p "I said yes."

    $ flan.show(expression="smile", at=hop)

    f "Yay! You're awesome!"

    $ pat.expression("neutral")

    p "I'll analyze your wings. Lay on the table."

    $ pat.show(zorder=8)

    $ flan.move(hopreset)
    $ flan.show(expression="neutral", at=right, transition=move_fast)
    play sound sfx_body_fall

    "Flandre dives onto the table, pointing her back towards the ceiling."

    $ remi.expression("neutral")
    $ pat.move(center_right, transition=ease)
    $ pat.face(flipped=False)
    $ pat.show(magic=True, transition=dissolve_fast, zorder=0.8)

    r "Don't do anything weird to her."

    $ pat.show(at=center, flip=True, magic=False)

    p "Like what?"

    $ remi.expression("embarrassed")

    r "Uh... I don't know."

    $ remi.expression("neutral")
    $ pat.show(expression="smile", at=center_right, flip=True, magic=True)

    p "In that case, you are free to go do whatever you want. But don't break anything. And don't disturb me."

    r "I'm not leaving her alone."

    $ pat.expression("neutral")

    p "Fair enough. You can grab a book if you'd like. Don't damage any, or you'll explode."

    $ remi.expression("angry")

    r "Explode how?"

    call scene_transition_fade("black") from _call_scene_transition_fade_8
    stop music fadeout 2.0

    "Patchouli begins her analysis, floating above Flandre and applying various spells and potions. Remilia stands in the corner and watches for the rest of the night."

    return

label day2_end:

    play music bgm_emotional fadein 2.0
    call scene_transition_fade("bg_study") from _call_scene_transition_fade_9

    $ remi.show(expression="neutral", at=[corner_left, standheight], zorder=1.5)
    $ pat.show(at=[center_right, standheight])
    $ flan.show(at=[right, standheight])
    with dissolve

    $ pat.show(center, transition=move_fast)
    
    "Patchouli drops out of the air, onto her feet."

    $ pat.show(magic=False, transition=dissolve_fast, zorder=2)

    p "I'm done."

    r "Are they fixed?"

    $ pat.show(expression="annoyed", flip=True, transition=dissolve_fast)

    p "No, I'm tired."

    $ flan.move(corner_right)
    $ pat.show(expression="neutral", at=center_right)
    $ remi.move(left, transition=ease)

    "Remilia pushes off the wall she was leaning on, approaching Patchouli."

    r "Did you learn anything useful?"

    $ flan.show(drophalf, zorder=0.5)

    "Patchouli yawns, while Flandre starts doing stretches on the floor."

    $ flan.face(flipped=False)

    p "These wings won't heal themselves, they were cut by something abnormal. I must figure out exactly what that abnormality is."

    $ flan.move(center_right)
    $ pat.face(flipped=False, transition=dissolve_fast)

    $ pat.move(offscreenright)
    $ flan.move(corner_left, transition=move_slow)

    "She walks off deeper into the room."

    $ flan.move(standheight)
    $ remi.show(expression="annoyed", at=center, transition=ease)

    r "Hey, what now?"

    $ flan.expression("question")

    p "Do whatever."

    $ flan.expression("frown")

    r "Ugh, fine then. Hey, Flan—hey where are you?"

    $ flan.expression("question")
    $ remi.expression("neutral")

    f "This one is all symbols?"

    $ flan.show(zorder=1)
    $ remi.face(flipped=True)

    "Flandre stands at a shelf with books scattered around her. Her face is buried in a large tome."

    $ flan.expression("frown")

    f "Bleh. This stuff is too complicated."

    $ remi.move(hop)

    "She tosses it aside, nearly crushing her sister's foot."

    call left_zoom_l from _call_left_zoom_l

    $ remi.move(hopreset)
    with None
    $ remi.show(expression="annoyed", at=left, transition=move_slow)

    r "What are you doing?"

    $ flan.flip()

    f "Reading. Or, trying."

    $ remi.expression("smile")

    r "Sure you are. How do your wings feel?"

    f "Numb."

    r "Can I check them?"

    $ flan.flip()

    $ remi.expression("serious")

    r "They are... hmm."

    f "Um, are they good? I mean, still the same?"

    $ remi.expression("neutral")

    r "...Yeah. Same."

    $ flan.flip()
    $ flan.expression("question")

    f "Are you sure?"

    r "I'm pretty sure."

    $ flan.expression("neutral")

    f "Well, alright then. Can you help me find a readable book?"

    r "Not now. I'm going to talk to the librarian."

    $ flan.expression("frown")

    f "Patchouli?"

    r "Yeah, sure."

    f "About what?"

    r "I want to ask a few questions."

    f "That's all?"

    r "Yes."

    f "Don't be mean to her."

    r "I don't plan on it."

    $ flan.expression("serious")

    f "If you make her change her mind again... just don't."

    $ remi.expression("smile")

    r "I won't. I'll be careful about that. I'll be right back, alright?"

    $ flan.expression("neutral")

    f "Okay."

    call left_unzoom_l from _call_left_unzoom_l

    $ remi.flip(dissolve_fast)

    call scene_transition_fade("black") from _call_scene_transition_fade_10

    "Flandre runs over to more bookshelves as Remilia walks deeper into the room."

    play music bgm_library fadein 2.0
    call scene_transition_fade("bg_study") from _call_scene_transition_fade_11
    $ pat.flip()
    $ pat.show(expression="annoyed", at=[right, standheight], transition=dissolve)

    "Patchouli is sitting at a table, looking at the vast collection of open books in front of her."

    $ remi.show(expression="neutral", at=[left, standheight, enterleft])

    r "Hey, I have a few questions for you."

    p "Sure."

    "Her attention stays glued to her books."

    r "Did Flandre's wings change at all while you were studying them?"

    p "No."

    r "Are you absolutely certain?"

    p "Yes. I would have noticed change."

    r "Well... they looked different the last time I checked."

    $ pat.expression("neutral")

    "Patchouli finally looks up."

    p "When was that?"

    r "A few hours before coming here."

    $ pat.expression("think")

    p "Hm. Interesting. Perhaps they are deteriorating? That would be unsurprising."

    $ remi.expression("surprised")

    r "Really? Why?"

    $ pat.expression("curious")

    p "If something can block regeneration, it is not unlikely for deterioration to follow."

    $ remi.expression("annoyed")

    r "I see."

    $ pat.expression("smile")
    $ remi.expression("neutral")

    p "Thank you for sharing that. It is useful information."

    $ remi.expression("smile")

    "Remilia gives a self-satisfied grin."

    r "Why, of course."

    $ pat.expression("curious")

    p "Do you know anything else about Flandre's injuries that she didn't tell me?"

    $ remi.expression("serious")

    r "No."

    $ pat.expression("neutral")

    p "I see."

    r "And don't ask her about it again."

    p "I won't."

    $ remi.expression("smile")

    r "Good."

    $ pat.move(center_right, transition=move_slow)

    "Remilia's smug grin returns as Patchouli stands up."

    $ pat.expression("curious")

    p "Mind if I check something?"

    r "Go right ahead."

    call summon_cg("cg_wingtouch") from _call_summon_cg

    $ remi.show(expression="surprised", blush=True)
    $ pat.expression("neutral")

    r "Huh? W-wait, hey!{w=0.5}{nw}"

    call dismiss_cg from _call_dismiss_cg

    $ remi.move(corner_left, transition=move_fast)
    $ remi.move(hop)

    "Remilia quickly leaps across the room, out of her grip."

    $ remi.expression("angry")

    r "W-what are you doing, fiend?! Unhand me!"

    $ pat.expression("confused")

    p "Checking your wings?"

    r "Unacceptable!"

    p "But you said go ahead?"

    r "I wasn't talking about me!"

    $ pat.expression("neutral")

    p "Oh."

    $ remi.show(expression="neutral", blush=False)

    "The rattled vampire clears her throat."

    $ remi.move(hopreset)
    with None
    $ remi.move(far_left, transition=ease)

    $ remi.expression("smile")

    r "Don't just touch a vampire's wing like that. Understand?"

    $ pat.expression("confused")

    p "But I've been touching Flandre's."

    $ remi.expression("neutral")

    r "That's clinical. It's obviously different."

    $ remi.show(expression="surprised", blush=True, at=hop)

    f "What are you two doing?"

    $ remi.move(hopreset, transition=None)
    $ remi.move(center)
    $ pat.move(far_right, transition=ease)
    $ remi.flip(dissolve_fast)
    $ flan.show(blush=True, at=[far_left, standheight, enterleft], zorder=6)
    $ flan.forget_position()

    $ remi.expression("neutral")

    r "Flandre?"

    p "I'm learning vampire etiquette."

    $ remi.expression("smile")

    r "This {i}heathen{/i} touched my wing without a care. As if it were some trinket from a market stall."

    $ flan.expression("surprised")

    f "Whoa. Is that one of those weird things you were worried about, sis?"

    $ remi.expression("neutral")

    r "No... Never mind. This is stupid."

    $ remi.show(blush=False, at=offscreenleft, transition=move_slow)
    $ flan.show(blush=False, expression="question", flip=True, transition=dissolve_fast)

    f "Wait, Remi!"

    $ flan.move(offscreenleft, transition=move_slow)

    call scene_transition_fade("bg_library_stairs") from _call_scene_transition_fade_12

    $ remi.show(blush=False, at=[center_left, standheight], transition=dissolve)
    $ flan.show(at=[right, standheight, enterright(0.5)]) 

    f "Where are you going?"

    $ remi.flip()

    r "Back to my coffin. Cursed tormentors, the lot of you."

    $ flan.show(at=enterforcefinish, expression="neutral")
    with None

    f "I'm going too. Those books melted my brain. Knowledge overload."

    r "Did you learn anything useful from them?"

    f "Mercury is cool."

    r "Hm. Okay then."

    play sound sfx_rustle_2
    $ remi.show(expression="smile", at=[center_right, scoot_left], transition=ease)
    $ flan.show(wings="rightwing", transition=dissolve_fast)
    $ flan.show(expression="question", at=floatup, transition=move_fast)

    "Remilia picks Flandre up."

    stop music fadeout 3.0

    r "Let me fly you down this time."

    $ flan.expression("smile")

    f "Yay! We're flying!"

    play music bgm_title fadein 2.0
    
    $ remi.show(at=[closeup, room_pacing(start_pos=0.4)])
    $ flan.show(expression="neutral", at=[closeup, room_pacing(start_pos=0.55)])
    show f at closeup, room_pacing(start_pos=0.55)
    show r at closeup, room_pacing(start_pos=0.4)
    with dissolve

    call dim_screen from _call_dim_screen_1

    "Remilia leaps into the air. They hover along the ceiling, weaving between the various chandeliers."

    f "It's fun, seeing things from way up. It's been so long."

    r "Indeed."

    show f smile

    f "I can't wait for Patchouli to fix my wings. We'll fly all over the world!"

    r "I'd love that."

    play sound sfx_crystals_clacking

    show layer master at shake()

    show r neutral
    show f surprised

    r "Watch your foot! Don't break the chandeliers."

    f "Oops."

    show bg_library onlayer background behind f, r, black, black_2 with dissolve

    show r smile
    show f neutral

    "Remilia moves to the bookshelf-lined walls, minimizing the risk of a tragic accident."

    show f question

    f "Hey hey, were you getting along with her?"

    r "Um, kind of?"

    show f neutral

    f "What did you two talk about?"

    r "Your wings. She seems to be getting a better idea of the situation."

    show f question

    f "And then she touched your wings?"

    show r neutral
    show f neutral

    r "Yeah... and then she touched my wings. Her understanding of vampires is woefully inadequate."

    f "We have to fix that."

    r "Yes. If she goes around touching wings like that, she won't live very long."

    f "Hehe, not at all."

    $ remi.hide()
    $ flan.hide()
    with dissolve_fast

    $ remi.show(expression="smile", at=[center_left, standheight], zorder=8)
    $ flan.show(expression="neutral", wings="default", at=[center_right, standheight])
    with dissolve
    
    call dim_screen_revert from _call_dim_screen_revert_1

    r "How was that? Your sister is a rather elegant flier, is she not?"

    $ flan.expression("frown")

    f "Mhm. I miss flying. I was the fastest in the world."

    $ remi.expression("neutral")

    r "Yeah..."

    $ flan.expression("question")
    play sound sfx_stomach_growling

    f "Though right now, I just want food."

    $ remi.expression("smile")

    r "That sounds wonderful. Hopefully that librarian warped us a decent meal."

    $ flan.expression("frown")

    f "Can't you call her Patchouli? You shouldn't be rude forever, she might get mad."

    $ remi.expression("neutral")

    r "Fine. Patchouli. It's rather long. A mouthful, isn't it?"

    $ flan.expression("neutral")

    f "Librarian isn't any shorter, though?"

    $ remi.expression("annoyed")

    r "Huh. Fair point."

    $ flan.expression("question")
    $ remi.expression("neutral")

    f "Enough blabbing. Food!"

    $ flan.show(flip=True, at=offscreenright, transition=ease)

    call scene_transition_fade("bg_bedroom") from _call_scene_transition_fade_13

    $ flan.show(expression="smile", flip=True, at=[left, standheight, enterright()])
    $ remi.show(flip=True, at=[right, standheight, enterright()])

    f "Yay, another chicken!"

    r "Really? Out of everything in the forest? So bland."

    $ flan.show(expression="frown", at=enterforcefinish)
    $ flan.flip(dissolve_fast)

    f "But the feathers are nice."

    r "You aren't supposed to eat that part."

    f "I meant they look nice, stupid."

    $ remi.expression("smile")

    r "Mhm, sure you did."

    call scene_transition_fade("black") from _call_scene_transition_fade_14
    play sound sfx_coffin_open
    stop music fadeout 2.0

    "After they devour their feathery meal, they go to sleep."

    return
