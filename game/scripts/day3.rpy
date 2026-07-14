label day3:
    call day3_morning

    return

label day3_morning:
    scene bg_bedroom with fade
    play music bgm_library fadein 2.0

    $ flan.flip()
    $ flan.show(at=[center, standheight], transition=dissolve)

    "Flandre hops over and shakes Remilia's coffin."

    f "Remi! Get up already!"

    play sound sfx_coffin_open

    "The lid slowly cracks open, revealing the sleepy vampire within."

    $ remi.flip()
    $ remi.show(at=[left, standheight, enterbottom(speed=2)])

    r "What... it's too early for yelling..."

    f "I slept the whole night!"

    r "That's great. Are they still numb?"

    f "Mostly. It's fading a little."

    r "Hm. We'll go see that librarian soon."

    $ flan.move(hop)

    f "No, let's go now!"

    r "Geez, hold on."

    scene black with fade

    "Flandre drags her out of the room, all the way to Patchouli's study."

    scene bg_study with fade
    play sound sfx_door_open

    $ pat.show(hat=True, at=[right, standheight], transition=dissolve, zorder=1)

    "Flandre flings the door open."

    $ flan.flip()
    $ flan.move([offscreenleft, standheight])
    $ flan.show(at=[center, standheight, enterleft()], zorder=2)
    with None
    $ pat.move(far_right, transition=move_slow)

    f "Patchy! More numbness!"

    p "Uh, yeah, sure."

    $ pat.show(magic=True, transition=dissolve_fast)
    call generic_spell()

    "She casts the spell once again."

    f "Yay."

    $ remi.show(at=[far_left, standheight, enterleft()], zorder=3)

    r "Her name is Patchouli."

    f "That's too long. She's Patchy now."

    $ pat.show(magic=False, transition=dissolve_fast)

    p "It works."

    $ flan.move(center_left, transition=ease)

    "Remilia looks to the mountain of books on Patchouli's desk."

    r "You've been busy."

    "Patchouli smiles."

    p "Indeed. I've been doing research on what might be blocking your regeneration."

    p "There are various possibilities, like poisons, wound-blocking magic, sun-specific afflictions. I'll craft some potions to try on you tomorrow."

    f "Ooh cool, potions? What do they do?"

    p "You'll see. As for the possibility of deterioration, I haven't found anything specific. Could I see your wings?"

    f "Huh, what, deterioration?"

    p "Yes. I want to check and see if they've changed."

    f "Um... okay."

    $ flan.move(right, transition=move_slow)
    $ flan.flip(transition=dissolve_fast)

    "She walks over. Patchouli inspects them closely."

    p "Hmm."

    "Seconds pass. Patchouli gently puts her fingers on the flaps around the holes."

    p "No change."

    $ remi.show(zorder=1)
    $ flan.move(center_left, transition=ease)
    $ flan.flip(transition=dissolve_fast)
    $ pat.move(right, transition=move_slow)

    f "Thank goodness. Surely they can't get worse."

    p "I'll keep checking on it. Remilia noticed some changes, so I want to monitor them closely."

    f "What? When?"

    p "Yesterday."

    $ flan.flip(transition=dissolve_fast)

    "Flandre crosses her arms as she glares at Remilia."

    f "So, you {i}did{/i} notice something yesterday? That's what you were talking to Patchouli about, then?"

    r "Um, yes. I—"

    f "Why did you lie?"

    r "I wanted to be sure before I said anything."

    f "They are {i}my{/i} wings! I want to know everything!"

    "Remilia averts her gaze."

    f "Anything else I should know?"

    r "No. I just thought the holes might be slightly bigger, but I'm not certain. I wanted to be sure before making you worry."

    f "Well I'm a part of this too, so tell me."

    r "Right. Sorry."

    $ flan.move(offscreenleft, transition=move_slow)

    stop music fadeout 2.0

    "Flandre lets out a heavy sigh as she leaves the room."

    p "Apologies."

    $ remi.move(center_left, transition=move_slow)

    "Remilia lets out a sigh of her own as she drops into a chair at Patchouli's table."

    $ remi.show(sitheight, transition=move_slow)

    play music bgm_emotional fadein 2.0

    r "That's just how it is. I suppose I handled things poorly."

    p "Yes."

    r "You don't have to agree."

    p "Are you leaving her alone?"

    r "For now. I'll give her time. I still need to keep an eye on you."

    p "Mm."

    $ pat.move(sitheight, transition=move_slow)

    show layer master at table_zoom

    "Patchouli looks back down at her books. Remilia watches for a while, before breaking the silence."

    r "Are you confident you can fix the wings?"

    p "Fairly so. There almost certainly is some kind of solution. I've solved far more difficult problems than this."

    r "Good. You seem very experienced with magic."

    p "Yes. I am a natural-born Magician, after all."

    r "What does that mean?"

    p "It means I was created as a Magician. Unlike others, I didn't need to transform."

    r "Uh... got it."

    p "Perhaps I'll educate you on what Magicians are later."

    "Patchouli points over her shoulder, behind herself."

    p "Now could you grab me that vial over there?"

    "Remilia glances over to a vial sitting on a bookshelf, a few feet behind Patchouli."

    r "Ah, am I the servant? I believe I am more fit to be served."

    p "Not really."

    $ remi.move(standheight, transition=move_slow)

    "Remilia spreads her arms and wings wide."

    r "Why not? I believe it would be a great honor to serve a vampire like me."

    p "No. Please grab it for me. I'd rather not exert myself."

    r "Oh, fine."

    $ remi.move(offscreenright, transition=ease)
    $ remi.flip()
    $ remi.move(center_left, transition=ease)
    $ remi.flip(transition=dissolve_fast)

    r "Here. Satisfied?"

    p "Yes. Thank you."

    r "It was only a few steps away."

    p "I am not one for physical labor. I stick to my strengths."

    r "I'm no laborer..."

    $ remi.move(sitheight, transition=move_slow)

    "Remilia grumbles as she sits back down. She silently observes Patchouli."

    "The magician moves between different books scattered across the table, jotting notes on occasion."

    "Every once in a while, a smile flashes for a moment, before returning to her usual deadpan expression."

    "Remilia reaches towards one of the notes."

    play sound sfx_magic_clash_1
    $ remi.move(hop(height=30))

    r "Ow! My finger!"

    "A spark vaporizes her finger instantly. As the blood flies towards the table, another spark vaporizes it, protecting the books. Patchouli does not react."

    "Remilia looks at her hand in awe."

    r "Did you do that?"

    p "Mm."

    r "Geez. Fine, I won't interfere."

    "Remilia pouts as her fingertip regenerates. She continues her silent observation."

    show bg_study with fade

    "Eventually, the books all close at the same time."

    p "I'm done. Would you get Flandre? I want to check something."

    r "Sure."

    $ remi.flip()
    $ remi.move(offscreenleft, transition=move_slow)
    

    stop music fadeout 2.0
    scene bg_library with fade
    $ flan.flip()
    $ flan.show(at=[right, sitheight], transition=dissolve)

    "Flandre is sitting still, staring at the wall. A few books are scattered around her."

    $ remi.flip()
    $ remi.show(at=[left, standheight, enterleft()])

    r "Hey."

    f "Hi."

    r "Patchouli wants to check your wings again."

    f "Sure."

    $ flan.move(standheight, transition=move_slow)
    $ flan.flip(transition=dissolve_fast)

    $ remi.move(center, transition=move_slow)

    "Remilia extends her arms."

    r "I can fly you up."

    f "No. I don't want to."

    r "Right. Um... sorry, about—"

    f "It's fine. I'm not really mad anymore."

    r "Oh. Good."

    $ flan.move(offscreenleft, transition=move_slow)

    f "Hurry up, slow face."

    $ remi.flip(transition=dissolve)

    scene bg_study with fade

    $ pat.show(at=[right, standheight], transition=dissolve)

    $ flan.show(at=[center_left, standheight, enterleft()], flip=True)
    $ remi.show(at=[far_left, standheight, enterleft()], flip=True)

    play music bgm_library fadein 2.0

    pause 0.3

    f "Delivery. Flan wings."

    $ flan.move(enterforcefinish)
    with None
    $ flan.move(center_right, transition=move_slow)
    $ flan.flip(transition=dissolve_fast)

    p "They look the same. Good. Still numb?"

    f "Yeah."

    p "How long does it last on you?"

    f "Nearly 'till morning. It was starting to wear off though."

    call generic_spell()

    p "Now it should be good until next time I see you."

    f "Oh, thanks!"

    p "I have many experiments ready for tomorrow. I'll need you here all night."

    $ flan.move(center_left, transition=move_fast)
    $ flan.flip(transition=dissolve_fast)

    "Flandre spins and salutes."

    $ flan.move(hop(height=30))

    f "Yes ma'am! See ya!"

    scene bg_bedroom with fade

    $ flan.show(at=[left, standheight])
    $ remi.show(at=[center_right, standheight], flip=True, transition=dissolve)

    "The sisters gather around their daily dead chicken."

    r "Hey... I'm sorry about..."

    f "I know."

    r "I was just... trying to help."

    "Flandre points at Remilia."

    f "I know. Stop talking about that. Give me the chicken leg if you want forgiveness."

    r "Here, ma'am."

    f "Thank you, my servant. The dark meat is all mine today."

    r "Oh, come on."

    "Flandre takes a massive chomp."

    f "I'm upset about my wings. I don't want to lose them."

    r "Patchouli said she's confident she can restore them."

    f "Does she really mean it? Is she telling the truth?"

    r "Yes, I am sure. She's been consistently honest, and appears competent. I've been watching her very closely."

    "Remilia looks to the side."

    r "I'm the only one that's been... not so straightforward."

    $ remi.move(small_shake())

    "Flandre tosses the bone onto Remilia's lap."

    f "Ha, it sounds like you're the one defending Patchy now."

    r "Uh, I wouldn't say that. But I do think she's trustworthy now."

    f "I believe you."

    $ flan.move(center, transition=move_slow)

    "Flandre leans into Remilia."

    f "You wouldn't lie about that. You never advocate for people."

    r "I cannot deny that."

    f "Thanks for trusting someone for me."

    $ flan.move([far_left, floatup], transition=move_fast)

    "Flandre jumps into her coffin."

    f "I'm tired now. Bye."

    r "You forgot something."

    "Remilia tosses the bone at her, but she catches and dunks it into Remilia's coffin."
    
    f "Heh."

    play sound sfx_coffin_close
    $ flan.hide(dissolve)
    
    "Flandre's coffin slams shut."

    r "Ugh."

    scene black with fade

    "Remilia empties her coffin and sleeps."

    return
