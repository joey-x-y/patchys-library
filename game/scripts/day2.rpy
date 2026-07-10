label day2:
    call day2_morning
    call day2_library
    call day2_end

    return

label day2_morning:
    
    "Remilia rises out of her coffin and stretches."

    r "I feel rested. Finally."

    "She looks over to Flandre's coffin."

    r "She's still asleep. Now how can I get us out of here?"

    "Flandre's coffin opens."

    f "No, I'm awake."

    r "Oh. How did you sleep?"

    f "Fine. I slept a little, but the pain came back. It was comfy inside so I didn't wanna get up."

    r "You could've woken me up."

    f "No, you needed sleep."

    r "Ok, fair enough. I was exhausted."

    f "And don't try to escape. We'll explode."

    r "She's bluffing. Besides, she can't take me at full power. It would be a slaughter."

    f "Please don't. I don't think she'll harm us if we don't do anything."

    r "We're her test subjects. Who knows what she'll do."

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

    "Remilia sighs as they step into the hallway. A voice resounds."

    p "Go up the stairs."

    f "Whoa, cool."

    r "She's watching us. Great."

    "They step out of the hall, back to the front room. Remilia stares at the exit for a moment before approaching the staircase."

    r "I can fly you up."

    f "Um, no thanks. You don't have to. Let's walk."

    "Remilia nods and follows Flandre to the stairs."

    "She looks around as she ascends. Books everywhere, along with fancy chandeliers lining the ceiling."

    r "You think she's read all those?"

    f "No. Too many."

    r "I bet."

    "They reach the top, approaching a large door."

    p "You may enter."

    "Remilia grabs Flandre's hand, and they walk through the door together."

    return

label day2_library:
    "They step into a large room lined with even more books. Patchouli sits in front of them at a large desk."

    p "Welcome to my study."

    f "Whoa, cool!"

    r "Would you numb Flandre's wings again?"

    p "Sure. I can make it last longer this time. Come here."

    "Flandre walks over, and the magician casts the spell."

    f "Thank you... uh, what's your name?"

    $ magician_name = real_magician_name

    p "Patchouli."

    f "Thank you, Patchouli! I'm Flandre Scarlet, that's my cranky sister Remilia Scarlet!"

    p "Well met, Scarlets."

    "Remilia steps forward."

    r "What do you intend on doing with us?"

    p "Observe. Study. Stuff like that."

    r "What exactly do you mean by that?"

    "Flandre tugs the back of Remilia's shirt."

    f "You're being rude, sis."

    r "I must know. I will only tolerate so much. I have dignity I wish to maintain."

    p "I'm not a mad magician, I won't do anything too harsh. I just want to understand vampires more. I've never seen one. It's very interesting. Why does simple sunlight hurt them when they are so durable? There's a lot of questions."

    r "So we're your entertainment?"

    p "Hmm. Yeah."

    r "Great."

    "Flandre gently tugs Remilia's shirt, and she steps back next to her."

    f "You can ask stuff now."

    p "So I shall. The first question is about healing. Vampires heal themselves, correct?"

    r "Yes, if they rest."

    p "Is Flandre not a vampire?"

    "Flandre raises her hand."

    f "I am!"

    p "Your wings didn't heal."

    f "Uh, yeah."

    r "She didn't sleep enough, your numb spell was too short."

    f "No, that's not it. Don't blame her. They haven't healed at all, no matter what."

    p "What caused it?"

    "Flandre crosses her arms and looks down."

    f "Um... well, a blade. It burned."

    p "What kind of blade was it?"

    f "Uh... I don't know!"

    "Remilia gently puts her hands on Flandre's shoulders."

    r "That's quite enough."

    p "I suppose it is. I have an idea now."

    "Flandre looks back up at Patchouli."

    f "Um... if it's ok, do you think you can fix it? Please?"

    p "Hmm... that would make for an interesting project."

    r "That's a good idea. A good vampiric study."

    p "When you put it like that... never mind."

    r "What?! I thought you wanted to!"

    p "The way you suggest things... it's kind of annoying..."

    r "How so?"

    f "Sis, be quiet."

    "Flandre steps forward out of Remilia's grip. Remilia mouth opens, but quickly closes again."

    f "Patchouli, could you please try? The pain... I hate it. Please. I'll help however you want."

    "Remilia bows her head."

    r "Please help my sister."

    "Patchouli sighs."

    p "Very well. I'll do it."

    "Flandre hops in the air."

    f "Yay! Thank you!"

    p "I'll analyze your wings. Lay on the table."

    f "Ok!"

    "Flandre hops up on the table and lies on her face. Patchouli floats over her."

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
    
    "Patchouli drops out of the air, onto her feet."

    p "I'm done."

    r "Are they fixed?"

    p "No, I'm tired."

    "Remilia pushes off the wall she was leaning on, approaching Patchouli."

    r "Did you learn anything useful?"

    "Patchouli yawns. Flandre hops off the table and starts doing stretches on the ground."

    p "These wings won't heal themselves, they were cut by something abnormal. I must figure out exactly what that abnormality is."

    "She walks off deeper into the room."

    r "Hey, what now?"

    p "Do whatever."

    r "Ugh, alright then. Hey, Flan—hey where are you?"

    "She looks to where she was, but she's gone."

    f "Huh? It's all symbols?"

    "Flandre is at a bookshelf, with a stack of books next to her."

    f "Bleh. This stuff is too complicated."

    "Remilia walks over to her."

    r "What are you doing?"

    f "Reading. Or, trying."

    r "Right. How are your wings feeling?"

    f "Numb."

    r "Can I check them?"

    f "Yeah."

    "Remilia goes behind Flandre and observes the wings."

    r "They are... hmm."

    f "Um, are they good? I mean, still the same?"

    r "...Yeah. Same."

    "Flandre turns around."

    f "Are you sure?"

    r "I'm pretty sure."

    f "Well, ok. I'm gonna find a readable book now."

    r "Alright, I'm going to talk to the librarian."

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

    "Flandre runs over to more bookshelves, as Remilia walks deeper into the room."

    "Patchouli is sitting at a table, looking at the many open books in front of her."

    r "Hey, um, can I ask some more questions?"

    p "Sure."

    "Her attention stays down in her books as she responds."

    r "Did Flandre's wings change at all while you were studying them?"

    p "No."

    r "Are you absolutely certain?"

    p "Yes. I would have noticed change."

    r "Well... they looked different last time I checked."

    "Patchouli finally looks up."

    p "When was that?"

    r "A few hours before coming here."

    p "Hm. Interesting. Perhaps they are deteriorating? That would be unsurprising."

    r "Really? Why?"

    p "If something can block regeneration, it is not unusual for it to cause slow deterioration as well."

    r "I see."

    p "Thank you for sharing that, it is useful information."

    "Remilia crosses her arms and smiles."

    r "Of course."

    p "Do you know anything else that Flandre couldn't say?"

    "Remilia smile drops."

    r "No."

    p "I see."

    r "And don't ask her about it again."

    p "I won't."

    r "Good."

    "Remilia's smile returns as Patchouli stands up."

    p "Mind if I check something?"

    r "Go right ahead."

    "Patchouli grabs Remilia's wing."

    r "Huh, wait, hey!"

    "Remilia quickly leaps across the room, out of her grip."

    r "What are you doing, fiend?"

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

    r "Oh, Flandre."

    p "I'm learning vampire etiquette."

    r "She touched my wing without a care in the world. Heathen."

    f "Oh. Is that one of those weird things you were worried about, sis?"

    r "No. Never mind, this is stupid."

    "Remilia briskly walks out of the room."

    f "Wait, sis!"

    "She runs after her."

    f "Where are you going?"

    r "I'm tired. I'm going to sleep."

    f "Me too, those books are confusing."

    r "Did you learn anything from them?"

    f "Mercury is cool."

    r "Hm. Ok then."

    "Remilia picks Flandre up."

    r "Let me fly you down this time."

    f "Ok!"

    "Remilia leaps into the air over the balcony. She hovers along the ceiling, weaving between the various chandeliers."

    f "It's fun, seeing things from way up."

    r "Indeed."

    f "I can't wait for Patchouli to fix my wings. We'll fly all over the world!"

    r "I'd love that."

    r "Hey, watch your foot! Don't break the chandeliers."

    f "Oops."

    "They continue to float around the room."

    f "Hey, hey, were you getting along with her?"

    r "Um, kind of?"

    f "What did you two talk about?"

    r "Your wings. She seems to be getting a better idea of the situation."

    f "And then she touched yours?"

    r "Yeah... then she did that. Her understanding of vampires is woefully inadequate."

    f "We have to fix that."

    r "Yes. If she goes around touching wings like that, she won't live very long."

    f "Hehe, not at all."

    "They touch down to the ground, then walk into the bedroom together."

    f "Yay, another chicken!"

    r "Out of everything in the forest, a chicken? Bland."

    f "But the feathers are nice."

    r "You aren't supposed to eat that."

    f "I meant they look nice, stupid."

    r "Mhm, sure."

    "They eat together, then go to sleep."

    return
