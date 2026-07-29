label day4:
    call day4_morning from _call_day4_morning

    return

label day4_morning:
    call day_transition_in() from _call_day_transition_in_2

    $ flan.show(wings="mid", at=[center_right, standheight], flip=True, transition=dissolve)
    
    "Flandre pops open her coffin and stands on the bed."

    $ flan.expression("smile")

    f "Hey, my wings are still fully numb!"

    $ flan.expression("neutral")

    "Remilia's coffin swings open."

    $ remi.show(at=[left, standheight], expression="neutral", flip=True, transition=dissolve, zorder=3)

    r "Oh, that's... good."

    stop music fadeout 2.0

    $ remi.expression("annoyed", transition=dissolve)

    "Remilia freezes as she looks at Flandre."

    $ flan.expression("frown")

    f "Um, Remi? What is it?"
    
    $ remi.expression("embarrassed")

    "Remilia looks away for a moment before looking back."

    r "Can I look at your wings for a moment?"

    f "Are they worse?"

    $ remi.expression("neutral")

    r "Um... I think it might be a little worse. I want to make sure."

    $ flan.expression("holding_tear")

    f "..."

    $ flan.show(center_left, transition=move_slow, zorder=5)
    $ flan.flip(transition=dissolve_fast)

    r "The holes are a little bigger."

    f "Mm."

    r "It's not a lot worse, just a little."

    f "Mhm."

    r "...I'll take you to Patchouli."

    $ flan.show(zorder=1, flip=True, transition=dissolve_fast)
    pause 0.3
    $ remi.move(offscreenright)
    $ flan.move(offscreenright, transition=move_slow)

    call scene_transition_fade("black") from _call_scene_transition_fade_21

    "Flandre grabs onto Remilia, and they fly to the study."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_22

    $ pat.show(hat=False, at=[right, standheight], transition=dissolve, zorder=4)

    $ remi.show(at=[far_left, standheight, enterleft()], zorder=6)
    $ flan.show(at=[left, standheight, enterleft()], zorder=5)

    r "Patchouli. I believe her wings have deteriorated."

    $ pat.expression("serious")

    p "Oh. Let me see."

    $ pat.move(center_left, transition=move_slow)

    p "They did. Odd, this is a sudden change."

    $ flan.show(expression="frown", at=enterforcefinish)

    f "Is it bad?"

    p "I was expecting this eventually, but more gradual. I'll look into it today."

    f "Mm."

    $ flan.move(enterforcefinish)
    with None
    $ flan.show(at=[right, standheight], flip=True, transition=move_slow)
    
    $ pat.show(magic=True, expression="neutral", at=center, transition=dissolve_fast, flip=True)
    call generic_spell from _call_generic_spell_8

    "Flandre takes her spot on the table as Patchouli reapplies the numb spell."

    play music bgm_library fadein 2.0

    $ pat.show(expression="smile", flip=True, transition=dissolve_fast)

    p "Are you going to stand in the corner and watch us all night again?"

    r "I don't believe that's necessary anymore."

    $ flan.flip(transition=dissolve_fast)

    f "Was it ever?"

    r "Yes. You are vulnerable in that position."

    $ flan.blush()

    f "Oh, right. You were worried about her doing weird stuff."

    $ remi.expression("smile")

    "Remilia shrugs."

    r "Sure. Whatever."

    $ flan.show(blush=False, flip=True)
    $ remi.expression("neutral")

    "She points to Patchouli."

    r "Would you unlock the front door? I want to go out."

    $ pat.expression("curious")

    p "Unlock?"

    r "Yes."

    $ pat.expression("neutral")

    p "It was never locked."

    $ remi.expression("annoyed")

    r "What? I thought you locked us in?"

    p "No."

    $ flan.expression("neutral")
    $ remi.show(expression="neutral", at=hopdown(height=10))

    "Remilia sighs heavily with her hand on her face."

    r "I guess I never checked. We were free all along?"

    p "I would rather not deal with trapped, angry vampires. I would've let you escape, even if it means my study project is ruined."

    $ flan.flip()

    f "What about the explody thing?"

    p "I'm not capable of that."

    $ remi.expression("smile")

    r "I knew it."

    p "But the stakes were too high to test it."

    $ remi.show(expression="neutral", blush=True)

    r "Bah. This deception will not go unanswered."

    $ remi.flip()
    with None
    $ remi.move(offscreenleft, transition=move_slow)

    $ flan.show(sitheight, flip=True)
    $ pat.show(sitheight, flip=True, transition=dissolve)

    call table_zoom_l from _call_table_zoom_l_1

    "Patchouli grabs a potion and begins rubbing it into the wings."

    f "What does that stuff do?"

    p "One of them could restore your wings, if we are fortunate. But regardless, they'll help me figure out what's going on with them. I'll spare you the details."

    f "Kay."

    call show_transition_fade("bg_study") from _call_show_transition_fade_4

    "A few hours pass as she applies many more."

    f "Patchy, are you getting along with Remi?"

    $ pat.expression("curious")

    p "Well enough, I think."

    $ flan.expression("frown")

    f "Is she still mean to you?"

    $ pat.expression("confused")

    p "Was she mean before?"

    f "Uh, yeah. Wasn't she?"

    $ pat.expression("neutral")

    p "Seemed normal to me."

    f "Really? Huh."

    "She tosses aside the last empty potion into the pile, and they all float into a box."

    $ pat.show(magic=False, transition=dissolve_fast)

    p "That's all of them. Your wings aren't fixed, but I gained valuable information. Enough to form theories."

    $ flan.show(expression="neutral", flip=True, zorder=3)

    f "Ooh, like what?"

    $ pat.expression("curious")

    p "The most likely cause is a form of poison. Your body is clearly not poisoned, but perhaps there is a residual effect in the wings."

    $ flan.expression("frown")

    f "Poison?"

    p "I would also be curious if something specific to vampires is involved. Perhaps a form of sun magic? Unfortunately, I am not familiar with how exactly sunlight affects vampires."

    p "Speaking of which, have you ever been harmed by the sun before?"

    f "Not really. I've had tiny moments where it touches me, but it just stings a tiny bit."

    p "Do you know if sun wounds heal normally? If your arm was stuck out of a window and incinerated, would it come back?"

    $ flan.expression("holding_tear")

    f "Uh... I don't know. That sounds scary."

    $ pat.expression("smile")

    p "I see. That would make for an interesting experiment."

    $ flan.expression("surprised")

    f "No!"

    $ pat.expression("neutral")

    p "I won't."

    $ flan.expression("neutral")

    f "Phew."

    $ flan.move(scoot_right)
    $ pat.move(scoot_left, transition=move_slow)
    $ flan.move(hopdown(height=10))
    $ pat.move(hopdown(height=10))

    "They both take a seat. A tea set floats over and serves them."

    p "That is all for now. I shouldn't need your wings for a few days."

    "She nods and grabs her tea. They sip in silence."

    "Flandre's legs slowly swing. Patchouli is still, her eyes closed but occasionally opening for a peek. Eventually, they stick to Flandre."

    p "Where did you two come from?"

    $ flan.expression("smile")

    f "The noble Scarlet house!"

    $ pat.expression("think")

    p "Noble house, hmm? That explains your sister's... peculiar charm."

    f "Haha, peculiar."

    $ pat.expression("smile")

    p "Indeed. What brought you two into this forest?"

    $ flan.expression("frown")

    f "Well... humans don't like vampires. We had to leave, or kill everyone..."

    $ flan.show(expression="smile", at=[standheight], transition=move_fast)

    f "But now we're here! This place is really nice."

    $ flan.expression("neutral")
    $ pat.move(hop(5))

    "Patchouli puts a proud hand to her chest."

    p "Good eye. It is my creation, after all."

    $ flan.expression("question")

    f "Really? How did you make it?"

    p "Magic and imagination."

    $ flan.expression("frown")

    f "You are a terrible storyteller."

    $ pat.expression("curious")

    p "Fine. I studied some libraries and learned how to manipulate materials to take the shape of the ideal design."

    $ flan.expression("question")

    f "Wow, cool. How did you do the magic?"

    $ pat.expression("smile")

    p "It requires many years of magical study. You need to do that before you could even begin to understand."

    $ flan.expression("frown")

    f "Oh. Never mind."

    $ flan.show(expression="neutral", at=sitheight, transition=move_fast)

    "Flandre plops back down and picks up her tea."

    f "Hey, do you like Remilia?"

    $ pat.expression("think")

    "Patchouli takes a long drink before responding."

    $ pat.expression("neutral")

    p "Mhm. She's interesting, I suppose."

    f "Good. She can be really nice too. The nicest ever. But she can be annoying, being mean to new people. How do you expect to make friends like that? Ugh."

    p "Being cautious isn't so bad."

    $ flan.expression("frown")

    f "I guess. But it's been excessive since it happened. Like it's somehow her fault."

    $ pat.expression("curious")

    p "Since what?"

    $ flan.expression("holding_tear")

    f "Um..."

    $ pat.expression("confused")

    p "Oh, never mind."

    $ flan.expression("frown")
    $ pat.expression("neutral")
    with dissolve_fast

    "Flandre lets out a deep sigh."

    $ flan.expression("neutral")

    f "I can't complain, though. She makes me feel safe. I appreciate it. But she's annoying."

    "Patchouli sips tea, and smiles as she sets the cup down."

    $ pat.expression("smile")

    p "That is—"

    play sound sfx_door_open
    stop music fadeout 1.0

    call table_unzoom_l from _call_table_unzoom_l

    play music bgm_emotional fadein 2.0

    r "I'm back!"

    $ remi.show(expression="smile", blush=False, glove="Blood", dirty=True, at=[far_left, standheight, enterleft()], flip=True)
    $ pat.show(expression="neutral", at=[center_right, standheight], transition=move_slow, zorder=2)
    $ pat.flip(transition=dissolve_fast)

    "Remilia flies in with a large bag."

    $ pat.expression("confused")

    p "Is that one of my bookshelf covers?"

    r "Very observant of you. 'Tis a small price to pay for your deception."

    $ flan.expression("frown")

    f "Hypocrite."

    $ remi.show(expression="angry", at=enterforcefinish)
    $ flan.expression("neutral")
    $ pat.expression("smile")

    r "Oh shut up!"

    $ remi.expression("smile")
    play sound sfx_body_fall

    "She tosses her delivery to the floor."

    r "I've brought a feast. No more chickens!"

    $ pat.expression("annoyed")

    "She opens it, revealing a mass of rabbit carcasses."

    $ flan.expression("smile")

    f "Yay!"

    $ flan.expression("neutral")

    p "This is not what the covers are for."

    r "They weren't doing anything anyway. Just shoved in a random corner."

    p "Yes, for future use. And must you bring in so much filth?"

    call generic_spell from _call_generic_spell_13
    $ remi.show(dirty=False, glove="Off", transition=dissolve_fast)

    r "That's just how hunting works. Hands get dirty. It is what it is."

    f "How unnoble."

    $ remi.expression("neutral")
    $ pat.expression("smile")

    r "Quiet, you."

    $ remi.move(at=[center_left, sitheight])
    $ flan.show(center_right, flip=True)
    $ pat.show(at=[far_right, sitheight], zorder=5)
    with ease 

    call table_zoom_l from _call_table_zoom_l_2
    with None

    $ flan.expression("frown")
    $ remi.show(glove="Blood", expression="smile", transition=dissolve)
    
    "Remilia begins her feast, causing blood to drip down her face."

    $ pat.expression("neutral")
    $ flan.flip(transition=dissolve_fast)

    "Flandre does her best to protect the floor, cupping her hands in front of her sister."

    $ flan.blush()

    f "Remi... this is someone else's home. Come on."

    r "Blood is meant to be spilled, no?"

    $ flan.show(center, flip=True, transition=dissolve_fast)

    f "Sorry Patchy, she is a terrible eater."

    $ pat.expression("annoyed")

    p "Please keep the floors clean. I have not invested in mops."

    $ flan.expression("neutral")

    f "I'll do my best."

    p "I was talking to Remilia."

    $ pat.expression("neutral")

    "Remilia tosses her half-eaten mess back into the pile."

    $ flan.show(expression="frown", blush=False)

    f "Ugh... that's gross..."

    r "I'm satisfied."

    $ flan.expression("neutral")

    "Flandre grabs herself two fresh rabbits, carefully avoiding her sister's former meal."

    call generic_spell from _call_generic_spell_9
    
    $ remi.show(glove="Off", hat=False, transition=dissolve_fast)

    "Then, the bag vanishes."

    $ remi.expression("surprised")

    r "Huh? My food?"

    p "I've moved your things to your room."

    $ remi.expression("smile")

    r "Cool, you can just teleport anything, anywhere you want?"

    $ pat.expression("smile")

    p "Within my domain, most inanimate things. Books, dead animals, hats, whatever."

    $ pat.show(magic=True, transition=dissolve_fast)
    call generic_spell from _call_generic_spell_14
    $ pat.show(hat=True, transition=dissolve_fast)

    p "Like that."

    $ flan.expression("question")
    $ pat.show(magic=False, transition=dissolve_fast)

    f "Cool!"

    $ flan.expression("neutral")

    r "And you can also eavesdrop on anyone, and make your voice appear anywhere?"

    p "Not eavesdrop. I just know where people are."

    r "Oh, good. So you weren't eavesdropping after all?"

    p "That would be useful, but no."

    r "..."

    $ remi.expression("neutral")

    "Remilia puts her hand in her hair."

    r "Hey. You warped my crown."

    p "Very observant of you. You'll find it eventually."

    r "Fantastic. You sure have a lot of tricks. What were those lasers you fired at me?"

    $ flan.expression("frown")

    p "It was a mixture of water and sun magic."

    $ remi.expression("annoyed")

    r "Uhh... sun?"

    $ pat.expression("neutral")

    p "Useful against vampires, but at a cost. Lasers require an undesirable level of exertion."

    $ remi.expression("neutral")

    r "I'm sure it does. Though you had no problem spamming them."

    $ pat.show(expression="smile", at=hop(10))

    "Patchouli crosses her arms with a big grin."

    p "Of course not. When your opponent's knees are buckling, it's only natural to deliver a swift finish, no?"

    play music bgm_duel
    $ remi.expression("smile")

    r "Bold words, book girl. Someday I'll demonstrate the true power of my Gungnir, when I'm not half-dead."

    $ flan.flip()
    $ remi.show(expression="surprised", at=shake)

    "Flandre throws a bone at Remilia's face point blank."

    $ remi.expression("angry")

    r "Hey!"

    f "Stop talking about fighting. I don't wanna fight more."

    $ remi.expression("smile")

    r "We're not even fighting yet, just planning our rematch. Isn't that right, master of this random library in the middle of nowhere?"

    stop music

    $ pat.expression("neutral")

    p "Rematch declined."

    $ remi.expression("annoyed")
    $ flan.expression("neutral")

    r "Oh, come on."

    f "Good."

    play music bgm_library fadein 2.0

    $ remi.expression("neutral")

    "Patchouli points to Flandre's pile of rabbit remains."

    p "Put those at the table around the corner. Those bones will be useful for future concoctions."

    $ flan.show(standheight, transition=move_fast, flip=True)

    f "Aye!"

    $ flan.move(offscreenright, transition=move_slow)
    $ flan.flip()

    $ remi.move(hop(10))

    "Remilia sips tea, but pauses midway through. She slams it down."

    $ remi.expression("annoyed")

    r "Hey, wait just a minute! You can teleport things, but made me grab a vial for you?"

    $ pat.expression("smile")

    p "Moving things with magic takes effort too. Not only lasers."

    $ remi.expression("neutral")

    $ flan.show(expression="surprised", at=center_right, transition=move_fast)
    $ flan.flip(transition=dissolve_fast)

    f "What? You made The Remilia Scarlet grab something for you?"

    p "Yes. Her labor was much appreciated."

    $ flan.expression("question")

    f "Wow. You're amazing. She doesn't do that for anyone."

    $ flan.show(expression="smile", at=hop(10))

    "Flandre points her thumb at herself."

    f "Well, except for me. I'm special."

    $ flan.expression("neutral")

    r "How rude. I did what was necessary to ensure your wings recover in a timely manner."

    $ pat.expression("annoyed")

    p "After complaining."

    r "Oh, be quiet. When we first arrived, you were groaning about providing us simple necessities like coffins."

    $ pat.expression("confused")
    $ pat.move(hopdown(30))

    "Patchouli sighs and presses her forehead into her tome."

    p "You are truly a silly creature."

    r "Excuse me?"

    $ pat.expression("neutral")
    $ flan.show(expression="frown", at=center, transition=move_fast, flip=True)

    "Flandre pulls Remilia's shirt."

    f "I'm sleepy now. Ate too many bunnies."

    $ remi.expression("smile")

    r "Fantastic. A proper meal must be followed by a proper rest. Shall we?"

    f "Finally, you two never stop bickering."

    $ pat.expression("smile")

    r "Alas, that girl just keeps provoking me. Let's escape while we can."

    call scene_transition_fade("bg_bedroom") from _call_scene_transition_fade_23

    $ remi.show(at=[center, standheight, enterright()], flip=True)
    $ flan.show(at=[far_right, standheight, enterright()])

    "Remilia drags Flandre down the stairs to their room. The bag of furry corpses is stashed in the corner, with a hat on top."

    r "Delightful. The fruit of my labor."

    f "Is chasing bunnies all you did today?"

    $ remi.show(flip=True,at=enterforcefinish)

    r "Rude. I thoroughly explored the area. It is pleasantly secluded. Plenty of wildlife to feed off of. Patchouli has a rather clever chicken trap as well."

    $ flan.show(expression="neutral", at=enterforcefinish)

    f "It's a nice place to build a library."

    call table_unzoom_l from _call_table_unzoom_l_5

    $ remi.show(flip=True, at=left, transition=move_slow)

    "Remilia dramatically flairs out her arms as she walks over to the bed."

    r "Truly a lucky find. I'd keep this all to myself as well. Or perhaps it was gifted to her? I must ask her how she got her hands on such a fine place."

    f "She made it herself."

    $ remi.expression("neutral")
    $ remi.flip(transition=dissolve_fast)

    r "Huh. Really?"

    f "Yup. She told me everything. Magic and creativity!"

    r "Right. What else?"

    f "That's it."

    $ remi.expression("annoyed")

    r "How exactly is that 'everything'? That's hardly any information."

    $ flan.show(scoot_left, expression="question", zorder=8)

    f "You're reeeally curious."

    $ remi.expression("embarrassed")

    r "Eh, not really."

    $ flan.expression("neutral")

    f "You are."

    $ flan.move(left)
    $ remi.move(right)
    with move_slow
    $ flan.move(offscreenleft, transition=dissolve)

    play sound sfx_coffin_close

    $ remi.show(expression="neutral", flip=True, transition=dissolve_fast)

    "She quickly escapes to her coffin."

    r "Goodness."

    play sound sfx_coffin_open
    
    $ flan.show(expression="frown", flip=True, at=[left, floatup], transition=dissolve_fast)

    f "Oh, um... thanks. You told me about my wings this time."

    r "Of course. I won't repeat the same mistake."

    $ flan.show(expression="neutral", blush=True)

    f "Mhm. See you, Remi."

    stop music fadeout 2.0
    call scene_transition_fade("black") from _call_scene_transition_fade_24

    "Flandre's coffin closes once again, as Remilia retires into her own."

    return
