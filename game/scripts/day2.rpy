label day2:
    call day2_morning
    call day2_library
    call day2_end

    return

label day2_morning:
    scene bg_bedroom with fade

    play sound sfx_coffin_open
    play music bgm_library fadein 2.0
    
    "Remilia rises out of her coffin and stretches."

    r "I feel rested. Finally."

    "She looks over to Flandre's coffin."

    r "She's still asleep. Now how can I get us out of here?"

    play sound sfx_coffin_open

    "Flandre's coffin flies open."
    
    f "No, I'm awake."

    r "Oh. How did you sleep?"

    f "Fine. I slept a little, but the numbness wore off and woke me up. It was comfy inside so I didn't wanna get up."

    r "You could've woken me up."

    f "No, you needed sleep."

    r "Fair enough. I was exhausted."

    f "And don't try to escape. We'll explode."

    r "She's bluffing. Besides, she can't take me at full power. It would be a slaughter."

    f "Please don't. I don't think she'll harm us if we don't do anything."

    r "We're her test subjects. Who knows what she'll do?"

    f "Please, sis. I'm tired of moving every night. I want my wings numbed again."

    r "Alright, fine. I won't do anything."

    r "But don't be careless. This is hostile territory."

    f "I'll be careful."

    r "Good. Thank you."

    "Flandre hops out of her coffin."

    f "I'm gonna ask her to numb my wings now."

    "Remilia flies after her."

    r "Hey, wait, don't go alone! You just said you'd be careful."

    f "Yeah, let's go together."

    play sound sfx_door_open
    call scene_transition_fade("bg_library")

    "Remilia sighs as they step out of the room. A voice resounds."

    p "Go up the stairs."

    f "Whoa, cool."

    r "She's watching us. Great."

    "Remilia stares at the exit for a moment before approaching the staircase."

    r "I can fly you up."

    f "Um, no thanks. You don't have to. Let's walk."

    "Remilia nods and follows Flandre to the stairs."

    "She looks around as she ascends. Books everywhere, along with fancy chandeliers lining the ceiling."

    r "You think she's read all those?"

    f "No. Too many."

    r "I bet."

    "They reach the top, approaching a large door."

    p "You may enter."

    "Remilia grabs Flandre's hand as they enter together."



    return

label day2_library:

    call scene_transition_fade("bg_study")
    "They step into a large room lined with even more books. Patchouli sits in front of them at a large desk."

    p "Welcome to my study."

    f "Whoa, cool!"

    r "Would you numb Flandre's wings again?"

    p "I suppose. I will make it last longer this time. Come here."

    play sound sfx_magic_summon

    "Flandre walks over, and the magician casts the spell."

    f "Thank you... uh, what's your name?"

    $ magician_name = real_magician_name

    p "Patchouli."

    f "Thank you, Patchouli! I'm Flandre Scarlet, that's my cranky sister Remilia Scarlet!"

    p "Well met, Scarlets."

    "Remilia steps forward."

    r "What do you intend to do with us?"

    p "Observe. Study. Gather some useful data."

    r "What exactly do you mean by that?"

    play sound sfx_rustle_3

    "Flandre tugs the back of Remilia's shirt."

    f "You're being rude, sis."

    r "I must know. I will only tolerate so much. I have dignity I wish to maintain."

    p "I'm not a mad magician, I won't do anything too harsh. I just want to understand vampires more. I've never seen one. It's fascinating."
    
    p "Why does simple sunlight hurt them when they are so durable? There are many questions to be answered."

    r "So we are your entertainment?"

    p "Hmm. Yeah."

    r "Great."

    play sound sfx_rustle_3

    "Flandre gently tugs Remilia's shirt, and she steps back next to her."

    f "She's done. You can ask stuff now."

    p "So I shall. For my first question, I believe vampires have the ability to regenerate themselves, correct?"

    r "Yes, if they rest."

    p "Is Flandre not a vampire?"

    "Flandre raises her hand."

    f "I am!"

    p "Your wings aren't regenerating."

    f "Uh, yeah."

    r "She didn't sleep enough, your numb spell was too short."

    f "No, that's not it. Don't blame her. They haven't healed at all, no matter what we do."

    p "What caused it?"

    "Flandre crosses her arms and looks down."

    f "Um... well, a blade. It burned."

    p "What kind of blade was it?"

    f "Uh... I don't know!"

    "Remilia gently puts her hands on Flandre's shoulders."

    r "That's quite enough."

    p "I suppose it is. I have an idea now."

    "Flandre looks back up to Patchouli."

    f "Um... if it's ok, do you think you can fix it? Please?"

    p "Hmm... that would make for an interesting project."

    r "Marvelous idea. It will make for a good vampiric study."

    p "When you put it like that... never mind."

    r "What?! I thought you wanted to!"

    p "The way you suggest things... it is rather bothersome..."

    r "How so?"

    f "Sis, be quiet."

    "Flandre steps forward out of Remilia's grip. Remilia mouth opens, but quickly closes again."

    f "Patchouli, could you please try? The pain... I hate it. Please. I'll help however you want."

    "Remilia bows her head."

    r "Please help my sister."

    "Patchouli sighs."

    p "Very well."

    "Flandre hops into the air."

    f "Yay! Thank you!"

    p "I'll analyze your wings. Lay on the table."

    play sound sfx_body_fall

    "Flandre leaps onto the table face-first, pointing her back towards the ceiling. Patchouli floats over her."

    r "Please don't do anything weird to her."

    p "Like what?"

    r "Uh... I don't know."

    p "In that case, you are free to go do whatever you want. But don't break anything. And don't disturb me."

    r "I'm not leaving her alone."

    p "Fair enough. You can grab a book if you'd like. Don't damage any, or you'll explode."

    r "Explode how?"

    "Patchouli begins her analysis with various spells and potions. Remilia stands in the corner and watches for the rest of the night."

    return

label day2_end:

    call scene_transition_fade("bg_study")
    
    "Patchouli drops out of the air, onto her feet."

    p "I'm done."

    r "Are they fixed?"

    p "No, I'm tired."

    "Remilia pushes off the wall she was leaning on, approaching Patchouli."

    r "Did you learn anything useful?"

    "Patchouli yawns. Flandre hops off the table and starts doing stretches on the floor."

    p "These wings won't heal themselves, they were cut by something abnormal. I must figure out exactly what that abnormality is."

    "She walks off deeper into the room."

    r "Hey, what now?"

    p "Do whatever."

    r "Ugh, fine then. Hey, Flan—hey where are you?"

    "She looks to where she was, but she's gone."

    f "Huh? It's all symbols?"

    "Flandre stands at a shelf with books scattered around her. Her face is buried in a large tome."

    f "Bleh. This stuff is too complicated."

    "She tosses it aside, nearly crushing her sister's foot."

    r "What are you doing?"

    f "Reading. Or, trying."

    r "Sure you are. How do you wings feel?"

    f "Numb."

    r "Can I check them?"

    "Flandre turns and presents them to Remilia."

    r "They are... hmm."

    f "Um, are they good? I mean, still the same?"

    r "...Yeah. Same."

    "Flandre turns around."

    f "Are you sure?"

    r "I'm pretty sure."

    f "Well, ok. Can you help me find a readable book?"

    r "Not now. I'm going to talk to the librarian."

    f "Patchouli?"

    r "Yeah, sure."

    f "About what?"

    r "I want to ask a few questions."

    f "That's all?"

    r "Yes."

    f "Don't be mean to her."

    r "I don't plan on it."

    f "If you make her change her mind again... just don't."

    r "I won't. I'll be careful about that. I'll be right back, alright?"

    f "Fine."

    scene black with fade

    "Flandre runs over to more bookshelves as Remilia walks deeper into the room."

    scene bg_study with fade

    "Patchouli is sitting at a table, looking at the many open books in front of her."

    r "Hey, can I ask some more questions?"

    p "Sure."

    "Her attention stays fixed on her books as she responds."

    r "Did Flandre's wings change at all while you were studying them?"

    p "No."

    r "Are you absolutely certain?"

    p "Yes. I would have noticed change."

    r "Well... they looked different the last time I checked."

    "Patchouli looks up."

    p "When was that?"

    r "A few hours before coming here."

    p "Hm. Interesting. Perhaps they are deteriorating? That would be unsurprising."

    r "Really? Why?"

    p "If something can block regeneration, it is not unusual for it to cause slow deterioration as well."

    r "I see."

    p "Thank you for sharing that, it is useful information."

    "Remilia crosses her arms and smiles."

    r "Of course."

    p "Do you know anything else about Flandre's injuries that she didn't tell me?"

    "Remilia's smile drops."

    r "No."

    p "I see."

    r "And don't ask her about it again."

    p "I won't."

    r "Good."

    "Remilia's smile returns as Patchouli stands up."

    p "Mind if I check something?"

    r "Go right ahead."

    # show cg

    "Patchouli grabs Remilia's wing."

    r "Huh? W-wait, hey!"

    # hide cg
    scene bg_study

    "Remilia quickly leaps across the room, out of her grip."

    r "What are you doing, fiend?!"

    p "Checking your wings."

    r "Hands off!"

    p "But you said go ahead?"

    r "I didn't mean me!"

    p "Oh. Sorry."

    r "Don't just touch a vampire's wing like that. Understand?"

    p "But I've been touching Flandre's."

    r "That's clinical. It's obviously different."

    f "What are you two doing?"

    "Remilia jumps."

    r "Flandre?"

    p "I'm learning vampire etiquette."

    r "This {i}heathen{/i} just touched my wing without a care in the world. As if it bore no sanctity at all."

    f "Oh. Is that one of those weird things you were worried about, sis?"

    r "No! Never mind, this is stupid."

    "Remilia flies past Flandre, out of the room."

    f "Wait, sis!"

    "She runs after her."

    call scene_transition_fade("bg_library")

    f "Where are you going?"

    r "I'm tired. I'm going to sleep."

    f "Me too, those books are confusing."

    r "Did you learn anything from them?"

    f "Mercury is cool."

    r "Hm. Ok then."

    play sfx_rustle_2

    "Remilia picks Flandre up."

    r "Let me fly you down this time."

    f "Woohoo!"

    play music bgm_emotional fadein 2.0

    "Remilia leaps into the air. They hover along the ceiling, weaving between the various chandeliers."

    f "It's fun, seeing things from way up. It's been so long."

    r "Indeed."

    f "I can't wait for Patchouli to fix my wings. We'll fly all over the world!"

    r "I'd love that."

    play sound sfx_crystals_clacking

    r "Watch your foot! Don't break the chandeliers."

    f "Oops."

    "Remilia moves to the bookshelf-lined walls, minimizing the risk of a tragic accident."

    f "Hey hey, were you getting along with her?"

    r "Um, kind of?"

    f "What did you two talk about?"

    r "Your wings. She seems to be getting a better idea of the situation."

    f "And then she touched yours?"

    r "Yeah...and then she touched mine. Her understanding of vampires is woefully inadequate."

    f "We have to fix that."

    r "Yes. If she goes around touching wings like that, she won't live very long."

    f "Hehe, not at all."

    "They touch down to the ground, then walk into the bedroom together."

    call scene_transition_fade("bg_bedroom")

    f "Yay, another chicken!"

    r "Really? Out of everything in the forest? So bland."

    f "But the feathers are nice."

    r "You aren't supposed to eat that."

    f "I meant they look nice, stupid."

    r "Mhm, sure you did."

    "They eat together, then go to sleep."

    scene black with fade
    stop music fadeout 2.0

    return
