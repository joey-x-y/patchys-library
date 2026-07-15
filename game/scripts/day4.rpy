label day4:
    call day4_morning from _call_day4_morning


    return

label day4_morning:
    call day_transition_in() from _call_day_transition_in_2

    $ flan.show(wings="mid", at=[center_right, standheight, enterbottom()], flip=True)
    
    "Flandre pops open her coffin and stands on the bed."

    f "Hey, my wings are still fully numb!"

    "Remilia's coffin swings open."

    $ remi.show(at=[left, standheight], flip=True, transition=dissolve, zorder=3)

    r "Oh, that's... good."

    stop music fadeout 2.0

    "Remilia freezes as she looks at Flandre."

    f "Um, Remi? What is it?"

    "Remilia looks away for a moment before looking back."

    r "Can I look at your wings for a moment?"

    f "Are they worse?"

    r "Um... I think it might be a little worse. I want to make sure."

    f "..."

    $ flan.show(center_left, transition=move_slow, zorder=5)
    $ flan.flip(transition=dissolve_fast)

    r "The holes are a little bigger."

    f "Mm."

    r "It's not a lot worse, just a little."

    f "Mhm."

    r "I'll take you to Patchouli."

    $ flan.show(zorder=1, flip=True, transition=dissolve_fast)
    pause 0.3
    $ remi.move(offscreenright)
    $ flan.move(offscreenright, transition=move_slow)

    call scene_transition_fade("black") from _call_scene_transition_fade_21

    "Flandre grabs onto Remilia, who flies them to the study."

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_22

    $ pat.show(hat=False, at=[right, standheight], transition=dissolve, zorder=2)

    $ remi.show(at=[far_left, standheight, enterleft()], zorder=5)
    $ flan.show(at=[left, standheight, enterleft()], zorder=3)

    r "Patchouli. I believe her wings have deteriorated."

    p "Oh. Let me see."

    $ pat.move(center_left, transition=move_slow)

    p "They did. Odd, this is a sudden change."

    f "Is it bad?"

    p "I was expecting this eventually, but more gradually. I'll look into it today."

    f "Mm."

    $ flan.forget_position()
    
    $ flan.show(at=[right, standheight], flip=True, transition=move_slow)
    
    $ pat.show(magic=True, at=center, transition=dissolve_fast, flip=True)
    call generic_spell from _call_generic_spell_8

    "Flandre takes her spot on the table, as Patchouli reapplies the numb spell."

    play music bgm_library fadein 2.0

    $ pat.flip(transition=dissolve_fast)

    p "Are you going to stand in the corner and watch us all night again?"

    r "I don't believe that's necessary anymore."

    $ flan.flip(transition=dissolve_fast)

    f "Was it ever?"

    r "Yes. You are vulnerable in that position."

    f "Oh, right. You were worried about her doing weird stuff."

    "Remilia shrugs."

    r "Sure. Whatever."

    "She points to Patchouli."

    r "Would you unlock the front door? I want to go out."

    p "Unlock?"

    r "Yes."

    p "It was never locked."

    r "What? I thought you locked us in?"

    p "No."

    $ remi.move(hopdown(height=10))

    "Remilia sighs heavily with her hand on her face."

    r "I guess I never checked. We were free all along?"

    p "I would rather not deal with trapped, angry vampires. I would've let you leave, even if it would ruin my study project."

    f "What about the explody thing?"

    p "I'm not capable of that."

    r "I knew it."

    p "But the stakes were too high to test it."

    r "Bah. This deception will not go unanswered."

    $ remi.flip()
    $ remi.move(offscreenleft, transition=move_slow)

    $ flan.show(sitheight, flip=True)
    $ pat.show(sitheight, flip=True, transition=dissolve)

    call table_zoom_l from _call_table_zoom_l_1

    "Patchouli grabs a potion and begins rubbing it into the wings."

    f "What does that stuff do?"

    p "One of them could restore your wings, if we are fortunate. But regardless, they'll help me figure out what's going on with them. I'll spare you the details."

    call show_transition_fade("bg_study") from _call_show_transition_fade_4

    "A few hours pass as she applies many more."

    f "Hey Patchy, are you getting along with Remi?"

    p "Well enough, I think."

    f "Is she still mean to you?"

    p "Was she mean before?"

    f "Uh, yeah. Wasn't she?"

    p "Seemed normal to me."

    f "Really? Huh."

    "A large mass of empty potions float into a box."

    $ pat.show(magic=False, transition=dissolve_fast)

    p "That's all of them. Your wings aren't fixed, but I gained valuable information. Enough to form theories."

    $ flan.show(flip=True, zorder=1)

    f "Ooh, like what?"

    p "The most likely cause is a form of poison. Your body is clearly not poisoned, but perhaps there is a residual effect in the wings."

    f "Poison?"

    p "I would also be curious if something specific to vampires is involved. Perhaps some form of sun magic. Unfortunately I am not familiar with how exactly sunlight affects vampires."

    p "Speaking of which, have you ever been harmed by the sun before?"

    f "Not really. I've had tiny moments where it touches me, but it just stings a tiny bit. That's all."

    p "Do you know if sun wounds heal normally? If your arm was stuck out of a window and incinerated, would it come back?"

    f "Uh... I don't know. That sounds scary."

    p "I see. That would make for an interesting experiment."

    f "No!"

    p "I won't."

    f "Phew."

    $ flan.move(far_right)
    $ pat.move(center_left, transition=move_slow)
    $ flan.move(hopdown(height=10))
    $ pat.move(hopdown(height=10))

    "They both take a seat. A tea set floats over and serves them."

    p "Time for a break. I shouldn't need your wings for a few days."

    "She nods and grabs her tea. They sip in silence."

    "Flandre's legs slowly swing. Patchouli is still, her eyes closed but occasionally opening for a peek. Eventually, they stick to Flandre."

    p "Where do you two come from?"

    f "The noble Scarlet house!"

    p "Noble house, hmm? That explains your sister's... peculiar charm."

    f "Haha, peculiar."

    p "Indeed. What brought you two into this forest?"

    f "Well... humans don't like vampires. We had to leave, or kill everyone."

    $ flan.move(at=[standheight, floatup], transition=move_fast)

    "Flandre hops to her feet and spreads her arms."

    f "But now we're here! This place is really nice."

    "Patchouli puts a proud hand to her chest."

    p "Good eye. It is my creation, after all."

    f "Really? How did you make it?"

    p "Magic and imagination."

    f "You are a terrible storyteller."

    p "Fine. I studied some libraries and learned how to manipulate materials to take the shape of the ideal design."

    f "Wow, cool. How did you do the magic?"

    p "It requires many years of magical study. You need to do that before you could even begin to understand."

    f "Oh. Never mind."

    $ flan.move(hopreset)
    $ flan.move(at=sitheight, transition=move_fast)

    "Flandre plops back down and picks up her tea."

    f "Hey, do you like Remilia?"

    "Patchouli takes a long drink before responding."

    p "Mhm. She's interesting, I suppose."

    f "Good. She can be really nice too. The nicest ever. But she can be annoying, being mean to new people. How do you expect to make friends like that? Ugh."

    p "Being cautious isn't so bad."

    f "I guess. But it's been excessive since it happened. Like it's somehow her fault."

    p "Since what?"

    f "Um..."

    p "Oh, never mind."

    "Flandre lets out a deep sigh."

    f "I can't complain, though. She makes me feel safe. I appreciate it. But she's annoying."

    "Patchouli sips tea, and smiles as she sets the cup down."

    p "That is—"

    play sound sfx_door_open

    call table_unzoom_l from _call_table_unzoom_l

    r "I'm back!"

    $ remi.show(at=[far_left, standheight, enterleft()], zorder=5, flip=True)
    $ pat.move(at=[center_right, standheight], transition=move_slow)
    $ pat.flip(transition=dissolve_fast)

    "Remilia flies in with a large bag."

    p "Is that one of my bookshelf covers?"

    r "Good eye. 'Tis a small price to pay for your deception."

    f "Hypocrite."

    r "Oh shut up."

    "She tosses her delivery to the floor."

    r "I've brought a feast. No more chickens!"

    "She opens it, revealing a mass of rabbit carcasses."

    f "Yay!"

    p "This is not what the covers are for."

    call table_zoom_l from _call_table_zoom_l_2

    $ remi.move(at=[center_left, sitheight])
    $ flan.show(center_right, flip=True)
    $ pat.move(at=[far_right, sitheight])
    with move_slow 

    "Remilia begins her feast, causing blood to drip down her face."

    $ flan.flip(transition=dissolve_fast)

    "Flandre does her best to protect the floor, cupping her hands in front of her sister."

    f "Remi... this is someone else's home. Come on."

    r "Blood is meant to be spilled, no?"

    $ flan.show(center, flip=True, transition=dissolve_fast)

    f "Ugh. Sorry Patchy, she is a terrible eater."

    p "Please keep the floors clean. I have not invested in mops."

    f "I'll do my best."

    p "I was talking to Remilia."

    "Remilia tosses her half-eaten mess back into the pile."

    f "Ugh... that's gross..."

    r "I'm satisfied."

    "Flandre grabs herself two fresh rabbits, carefully avoiding her sister's former meal."

    call generic_spell from _call_generic_spell_9
    
    "Then, the bag vanishes."

    r "Huh? My food?"

    p "They're in your room now."

    r "Cool, you can just teleport anything, anywhere you want?"

    p "Within my domain, most inanimate things."

    r "And you can eavesdrop on anyone, and make your voice appear anywhere?"

    p "Not eavesdrop. I just know where people are."

    r "Oh, good. So you weren't eavesdropping after all?"

    p "That would be useful, but no."

    r "What were those lasers you fired at me? Those were cool."

    p "It was a mixture of water and sun magic."

    r "Uhh... sun?"

    p "Useful against vampires, but at a cost. Lasers require an undesirable level of exertion."

    r "I'm sure it does. Though you had no problem spamming them."

    "Patchouli crosses her arms with a big grin."

    p "Of course not. When your opponent's knees are buckling, it's only natural to deliver a swift finish, no?"

    play music bgm_duel

    r "Bold words, book girl. Someday I'll demonstrate the true power of my Gungnir, when I'm not half-dead."

    $ flan.flip()
    $ remi.move(shake)

    "Flandre throws a bone at Remilia's face point blank."

    r "Hey!"

    f "Stop talking about fighting. I don't wanna fight more."

    r "We're not even fighting yet, just planning our rematch. Isn't that right, master of this random library in the middle of nowhere?"

    stop music

    p "Rematch declined."

    r "Oh, come on."

    f "Good."

    play music bgm_library fadein 2.0

    "Patchouli points to Flandre's pile of rabbit remains."

    p "Put those at the table around the corner. Those bones will be useful for future concoctions."

    $ flan.show(standheight, transition=move_fast, flip=True)

    f "Aye!"

    $ flan.move(offscreenright, transition=move_slow)
    $ flan.flip()

    "Remilia sips tea, but pauses midway through. She slams it down."

    r "Hey, wait just a minute! You can teleport things, but made me grab a vial for you?"

    p "Moving things with magic takes effort too. Not only lasers."

    $ flan.move(center_right, transition=move_fast)

    $ flan.flip(transition=dissolve_fast)

    f "What? You made The Remilia Scarlet grab something for you?"

    p "Yes. Her labor was much appreciated."

    f "Wow. You're amazing. She doesn't do that for anyone."

    $ flan.move(hop)

    "Flandre smiles and points at herself."

    f "Well, except for me. I'm special."

    r "How rude. I did what I had to do to ensure your wings recover in a timely manner."

    p "After complaining."

    r "Oh, be quiet. When we first arrived, you were groaning about providing us simple necessities like coffins."

    "Patchouli sighs and presses her forehead into her tome."

    p "You are truly a silly creature."

    r "Excuse me?"

    $ flan.show(center, transition=move_fast, flip=True)

    "Flandre pulls Remilia's shirt."

    f "I'm sleepy now. I ate too much."

    r "Fantastic. A proper meal must be followed by a proper rest. Shall we?"

    f "Finally, you two never stop bickering."

    r "Alas, that girl just keeps provoking me. Let's escape while we can."

    call scene_transition_fade("bg_bedroom") from _call_scene_transition_fade_23

    $ remi.show(at=[center, standheight, enterright()], flip=True)
    $ flan.show(at=[far_right, standheight, enterright()])

    "Remilia drags Flandre down the stairs to their room. The bag of furry corpses is stashed in the corner."

    

    r "Delightful. The fruit of my labor."

    f "Is chasing bunnies all you did today?"

    $ remi.move(enterforcefinish)
    $ remi.flip()

    r "How rude. I thoroughly explored the area. It is pleasantly secluded. Plenty of wildlife to feed off of. Patchouli has a rather clever chicken trap as well."

    f "It's a nice place to build a library."

    $ remi.show(flip=True, at=left, transition=move_slow)

    "Remilia dramatically flairs her arms out as she walks over to the bed."

    r "Truly a lucky find. I'd keep this all to myself as well. Or perhaps it was gifted to her? I must ask her how she got her hands on such a fine place."

    f "She made it herself."

    $ remi.flip(transition=dissolve_fast)

    r "Huh? Really?"

    f "Yup. She told me all about it. Magic and creativity!"

    r "Right. What else?"

    f "That's it."

    r "How exactly is that 'all about it'? That's hardly any information."

    $ flan.move(scoot_left)

    f "You're reeeally curious."

    r "Eh, not really."

    f "You are."

    $ flan.move(left)
    $ remi.move(right)
    with move_slow
    $ flan.move(offscreenleft, transition=dissolve)

    play sound sfx_coffin_close

    $ remi.flip(transition=dissolve_fast)

    "She quickly escapes to her coffin."

    r "Goodness."

    play sound sfx_coffin_open
    
    $ flan.show(flip=True, at=[left, floatup], transition=dissolve_fast)

    f "Oh, um... thanks. You told me about my wings this time."

    r "Of course. I won't repeat the same mistake."

    f "Mhm. See you, Remi."

    stop music fadeout 2.0
    call scene_transition_fade("black") from _call_scene_transition_fade_24

    "Flandre's coffin closes once again, as Remilia retires into her own."

    return
