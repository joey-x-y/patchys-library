label day5:
    call day5_morning from _call_day5_morning

    return

label day5_morning:
    call day_transition_in from _call_day_transition_in_3

    $ flan.show(at=[center, standheight], flip=True, zorder=6)
    $ remi.show(at=[left, standheight], flip=True)
    with dissolve

    $ remi.move(center_right, transition=move_fast)
    $ remi.flip(transition=dissolve_fast)

    r "..."

    r "Wings look the same."

    f "Phew."

    play music bgm_emotional fadein 2.0

    $ flan.move(far_left, transition=move_slow)
    play sound sfx_rustle_1
    $ flan.move(hopdown(150, length=0.5))

    "Flandre grabs a rabbit out of the bag."

    r "Already? We just ate before our slumber."

    $ flan.move(hopreset)
    $ flan.flip(transition=dissolve_fast)

    f "Not everyone has your puny appetite."

    $ flan.flip(transition=dissolve_fast)
    $ flan.move(hopdown(150, length=0.5))

    r "Guess not. I'm going on ahead."

    $ remi.show(offscreenright, flip=True, transition=move_slow)
    $ flan.move(hopreset)
    $ flan.flip()

    f "Mmf, mmph mm mmf!"

    call scene_transition_fade("bg_study") from _call_scene_transition_fade_25

    $ pat.show([right, sitheight], transition=dissolve, hat=True)

    "Patchouli sits with a book placed in her lap."

    $ remi.show(at=[corner_left, standheight, enterleft()], zorder=5)

    p "Oh, you're alone today."

    r "Yeah, she was hungry."

    p "Mm."

    "A minute passes with Remilia standing awkwardly at the front. Patchouli is focused on her book."

    r "Hey... how come you built your library all the way out in a forest like this?"

    p "It is secluded."

    $ remi.move(enterforcefinish)
    $ remi.move(left, transition=move_slow)

    "Remilia smiles as she walks forward."

    r "It really is. This place is quite peaceful. Do you enjoy seclusion?"

    p "Yes. No distractions."

    r "Hmm. Do you prefer being alone?"

    p "It depends."

    r "On what?"

    p "How bothersome they are."

    r "Ah yes, much like servants. Some are obedient and serve great food, some are better off being the food themselves."

    p "Right. On the subject of servitude, would you fetch my tea set?"

    pause 0.5

    "Remilia stares for a few seconds, then gives an exasperated sigh."

    $ remi.move(offscreenright, transition=ease)
    $ remi.flip()
    $ remi.move(center_left, transition=ease)
    $ remi.flip(transition=dissolve_fast)

    $ remi.move(sitheight, transition=move_fast)

    "She sets the tea set down roughly."

    r "You pour."

    call table_zoom_l from _call_table_zoom_l_3

    "Remilia sits as Patchouli serves tea with her magic, not moving a muscle."

    "They drink in silence for a few minutes."

    r "Would you say we've been a bother?"

    p "No."

    r "Why not?"

    p "You aren't bothersome."

    r "Really. That's surprising."

    p "You two have made things interesting, I have no complaints."

    r "I guess we did. Now, more tea."

    "Their cups refill, and the drinks continue."

    r "So, you told us in the beginning that you want to study vampires, but you've only focused on Flandre's wings. You haven't gone any further."

    p "I tried, but you didn't want me to."

    r "What do you mean?"

    "Patchouli makes a grabbing gesture with her hand. Remilia grits her teeth in response."

    p "You looked rather silly in that moment."

    "Remilia smiles and looks away, crossing her arms."

    r "If I weren't such a gracious vampire, your life would have ended after such an offense."

    p "Gracious indeed. But really, the wings became a problem I wanted to solve. And so I will."

    "Remilia looks back and leans forward, picking up her second round of tea."

    r "Wonderful. I truly am grateful for that."

    "Patchouli grabs hers and takes a sip."

    p "I imagine seeing your sister fly again will be a delightful moment for you."

    r "It will. I've been dreaming of it."

    "She looks down, staring into her cup."

    r "This was all because of my negligence. I would do anything for it to be fixed. Nothing is more important."

    "Remilia leans back again and looks directly at Patchouli."

    r "So yeah, thanks."

    p "I am merely doing what I want, but I will accept your gratitude."

    "They sit in silence for a few minutes."

    p "Say, what is it like, having a sister?"

    r "A liability."

    $ pat.move(hop(10))

    p "Huh?"

    r "But in a good way, I mean. Flandre is someone to keep safe at all times. If servants are incapable of doing it, I have to."

    "Patchouli takes a long sip, letting several seconds pass before responding."

    p "I see."

    $ remi.move(standheight, transition=move_slow)

    "Remilia stands and points her tea cup at Patchouli with a massive grin."

    r "I've never seen your face so confused before. Who's the one looking rather silly now?"

    p "You should use your words better."

    r "Semantics. I still win."

    $ remi.move(sitheight, transition=move_fast)

    "She downs the rest and sits back down."

    r "A sister is like a companion. That's a simpler way of putting it. I'm not alone."

    "Patchouli looks down into her cup."

    p "Hmm, that's family in general, right?"

    r "Yes. Did your family not want to come here with you?"

    p "I simply left on my own. I was not needed where I was created."

    r "Um... what does that mean?"

    "Patchouli sets her tea cup down, looking to Remilia."

    p "I suppose it is time for your lesson on Magicians."

    r "Is it not just a magic-user?"

    p "More than that. They are a separate species from human. One whose body can survive on magical energy alone. Biological needs are removed."

    r "Removing biological needs? How does that work?"

    p "Converting one's body into that state requires a sophisticated form of magic, one that many magic-users never discover."

    r "Ah, but a smart girl like you figured it out, then?"

    p "No. I am an exception. I was born as a Magician."

    r "Whoa, that's pretty cool. How does that even work though?"

    p "I am not certain. I only know that some form of special magic was used. I would like to figure that out someday."

    r "That's very interesting indeed. It sounds very special."

    p "It is, I suppose. But every shortcut pays a price. My physical attributes are rather... poor."

    $ remi.move(hop(10))

    "Remilia laughs."

    r "No kidding. You might even be more qualified to own servants than me."

    p "I—"

    r "No, I take that back. Don't get too full of yourself."

    "Patchouli lets out a sigh."

    p "Tomfoolery of the highest order."

    r "Hmph. More tea, now."

    "The rounds of tea continue."

    r "Why did you leave that place if you want to understand that Magician birth magic?"

    p "The knowledge would never be given to me. I have to pursue my own knowledge."

    r "So, is solving your birth a mission of sorts?"

    p "Not particularly. I simply enjoy seeking knowledge, and this library allows me to do so without others meddling."

    r "You sure are interested in knowledge, eh?"

    p "Yes, and it has become a most suitable surname."

    r "What? Surname?"

    p "I am Patchouli Knowledge."

    r "Go figure. Who named you that?"

    p "I did."

    "Remilia smacks her own face with her palm."

    r "Of course you did."

    $ remi.move(scoot_left)

    "Patchouli smiles to herself. Remilia leans back and puts up her feet as if it were a recliner."

    p "Does my past interest you? You look so curious."

    r "W-what, n-no. Not really."

    p "Oh. I see."

    "Patchouli takes a small sip, and fiddles with the cup."

    r "You know, libraries are quite nice. Truly a staple for any good mansion."

    p "I haven't seen you touch a book."

    r "That's not the point. It's the atmosphere. Status. A wealth of books convey a wealth of knowledge."

    p "Does that matter if you've never read them and haven't accumulated said knowledge?"

    r "Nah. That's the librarian's job. Delegation is the most important skill of a noble. Remember that."

    p "That is rather shameless."

    r "The only shame here is the severe lack of sofas. I could use more space to spread my poor wings."

    f "Your true colors are showing."

    

    $ flan.show(at=[far_left, standheight], transition=dissolve, zorder=1)

    call table_unzoom_l from _call_table_unzoom_l_1

    r "Oh, hello Flandre. Hey, wait, what does that mean?!"

    $ pat.show(magic=True)
    call generic_spell from _call_generic_spell_10

    f "Nice aim. You can do numb me from there?"

    $ pat.show(magic=False, transition=dissolve_fast, zorder=2)

    p "Yes."

    f "You two were so deeply engaged with each other, I didn't have the heart to interrupt. But then boredom happened. What a shame."

    $ remi.flip(transition=dissolve_fast)

    r "How long have you been here?"

    f "I got here right after you."

    r "That long. Ugh."

    $ flan.move(at=[center, sitheight], transition=move_slow)
    $ remi.flip(transition=dissolve_fast)

    call table_zoom_l from _call_table_zoom_l_4

    "Flandre crashes into the tea party."

    $ flan.flip(transition=dissolve_fast)

    f "Your peculiar charm is overwhelming Patchy."

    r "My what now? Peculiar? I am no such thing."

    $ flan.flip(transition=dissolve_fast)

    "Flandre aims her fingers at Patchouli."

    f "I'm jealous now. Don't steal my sister. I'm watching you."

    r "She won't just magically become my sister. Well, unless there's a spell for that."

    p "There is. But I don't know that one."

    r "See? Nothing to worry about."

    f "Hmph. I didn't mean it like that."

    r "Enough worrying. Put your feet on the table like a proper noble."

    f "Heh. That's stupid."

    $ flan.move(hop(10))

    "She puts them up."

    call show_transition_fade("bg_study") from _call_show_transition_fade_5

    "They continue to relax at the table for the next few hours, with Patchouli passively researching despite the vampire's distractions."

    "Flandre lets out a big yawn."

    r "I think it's bedtime."

    f "Yeah... carry me."

    stop music fadeout 2.0
    call scene_transition_fade("black") from _call_scene_transition_fade_26

    "Remilia drags Flandre to their bedroom."

    play music bgm_library fadein 2.0
    call scene_transition_fade("bg_bedroom") from _call_scene_transition_fade_27

    $ remi.show(at=[left, standheight], zorder=2)
    $ flan.show(at=[center_right, standheight], flip=True, transition=dissolve)

    f "I'm happy you made a friend."

    r "Did you doubt I would?"

    f "Um... maybe?"

    "Remilia sighs."

    r "How rude. Of course I did."

    f "Congrats."

    $ remi.move(center, transition=move_slow)

    "Remilia puts her hand on Flandre's head."

    r "You'll always be my sister, Flandre. Don't worry."

    f "I know. I was picking on you."

    r "Ah, the usual."

    play sound sfx_coffin_close

    call scene_transition_fade("black") from _call_scene_transition_fade_28

    "After their routine meal, they retire to their coffins."

    return
