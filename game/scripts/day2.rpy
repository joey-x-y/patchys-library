label day2:
    call day2_morning
    call day2_library
    call day2_end

    return

label day2_morning:
    
    "Remilia rises out of her coffin and stretches."

    r "I finally feel rested."

    "She looks over to Flandre's coffin."

    r "She's still asleep. I should think of a way out of here."

    "Flandre rises out of the other coffin."

    f "No, I'm awake."

    r "Oh. How did you sleep?"

    f "Ok. I slept a little, but the pain came back. I was just lying for a while."

    r "Oh."

    f "Don't try to escape. We'll explode."

    r "She's bluffing. Besides, she can't take me at full power anyway."

    f "Please don't. I don't think she'll harm us if we don't do anything."

    r "We're her test subjects. Who knows what she'll do."

    f "Please, sis. I'm tired of moving every night. And I want my wings numbed again."

    r "Ok, fine. But don't be careless. This is hostile territory."

    f "I'll be careful."

    r "Good."

    "Flandre hops up."

    f "I'm gonna ask her to numb my wings now."

    "Remilia hops quickly after her."

    r "Hey, wait, don't go alone. You just said you'd be careful!"

    f "Yeah, let's go together."

    "They step into the hallway. A voice resounds."

    p "Go up the stairs."

    f "Whoa, cool."

    r "Great. We're being watched."

    "They step out of the hall, back to the front room. Remilia stares at the door for a moment before approaching the staircase."

    r "I can fly you up."

    f "Um, it's ok. You don't have to. Let's walk."

    r "Ok."

    "Flandre walks up the stairs. Remilia continues to follow."

    "Remilia looks around as she ascends. The front hall is dark again. Lantern light comes from the top of the stairs. Various paintings cover the walls."

    "They reach the top, and a large door is in front of them."

    p "You may enter."

    "Remilia grabs Flandre's hand. They walk through the door."
    
    return

label day2_library:
    "They enter a library. Bookshelves line the room. In front of them is Patchouli, sitting at a table."

    p "Welcome."

    f "Hi."

    r "Would you numb Flandre's wings again?"

    p "Sure. I'll make it last longer this time. Come here."

    "Flandre walks over, and the magician casts the spell."

    f "Thanks, um... what's your name?"

    $ magician_name = real_magician_name

    p "Patchouli."

    f "Thanks, Patchouli! I'm Flandre Scarlet, that's my sister Remilia Scarlet!"

    p "Mhm."

    r "What do you intend on doing with us?"

    p "Observe. Study. Stuff like that."

    r "What exactly do you mean by that?"

    f "Stop being so rude."

    r "I need to know. I will only tolerate so much. I have dignity I wish to maintain."

    p "I'm not a mad magician, I won't do anything too harsh. I just want to understand vampires more. I've never seen one. It's very interesting. Why does sunlight hurt them when they are so durable? There's a lot of questions."

    r "So we're just here to entertain you?"

    p "Hmm, I guess so."

    r "Great."

    p "My first question is about healing. Vampires heal themselves right?"

    r "Yes, if they rest."

    p "Is Flandre not a vampire?"

    f "I am!"

    p "Your wings didn't heal."

    f "Uh, yeah."

    r "She didn't sleep all day, your numb spell didn't last long enough."

    f "No, that's not it. Don't blame her. They haven't healed at all, no matter what."

    p "What caused it?"

    f "Um... well, a knife. It burned."

    p "What kind of knife was it?"

    f "Uh... I don't know!"

    r "That's quite enough."

    p "Ok. That gives me ideas, at least."

    f "Can you... fix it?"

    p "Hmm... I don't know. That would make for an interesting project."

    r "That's a good idea. A good vampiric study."

    p "When you put it like that... never mind."

    r "What?! I thought you wanted to!"

    p "The way you say things... it's kind of annoying."

    r "How so?"

    f "Sis, please be quiet. Let me ask."

    "Remilia almost speaks, but stops."

    f "Patchouli, could you please try? The pain... I hate it. Please. I'll help however you want."

    "Remilia bows her head."

    r "Please help my sister."

    p "Alright. I'll do it."

    f "Thank you!"

    p "I'm going to analyze your wings. Lay on the table."

    f "Ok."

    "Flandre hops up on the table and lies on her face. Patchouli floats over."

    r "Please don't do anything weird."

    p "Like what?"

    r "Um, I don't know."

    p "Then you can go do whatever you want. But don't break anything. And don't disturb me."

    r "I'm not leaving her alone."

    p "Ok. You can read a book if you'd like. But don't damage it, or you'll explode."

    r "Explode how?"

    "Patchouli begins her analysis with various spells and potions. Remilia stands in the corner and watches for the rest of the night."

    return

label day2_end:
    
    p "Alright, I'm done."

    r "Are they fixed?"

    p "No, I'm tired."

    r "Did you learn anything from all that stuff you did?"

    "She yawns. Flandre hops off the table."

    p "Yes. These wings won't heal themselves, they were cut by something abnormal. I must figure out exactly what that is."

    "She walks off deeper into the library."

    r "Hey, what now?"

    p "Do whatever."

    r "Ugh, alright then."

    f "I bet she has some cool books!"

    "Flandre pulls a book off a shelf."

    f "It's all symbols?"

    "She puts it back."

    f "Never mind. This stuff is too complicated."

    r "How do your wings feel now?"

    f "Numb."

    r "So you didn't feel anything that whole time then?"

    f "Nope."

    r "Ok. Let me see."

    "Remilia goes behind Flandre and observes the wings."

    r "They are... hmm."

    f "Um, are they fine? No, the same?"

    r "...Yeah. Same."

    "Remilia walks back in front of her."

    f "Are you sure?"

    r "I'm pretty sure."

    f "Well, ok then."

    "Flandre looks around."

    f "I'm gonna find a readable book."

    r "Ok. I'm going to talk to the librarian."

    f "About what?"

    r "Just ask a few questions."

    f "Are you sure?"

    r "Yes."

    f "Don't be mean to her."

    r "I don't plan on it."

    f "If you make her change her mind again... don't."

    r "I won't. I'll be careful about that. I'll be right back, ok?"

    f "Fine."

    "Flandre walks to the bookshelves."

    "Remilia walks into the library and finds Patchouli."

    p "Hello."

    r "Hi. Um, can I ask some more questions?"

    p "Sure."

    r "Did Flandre's wing change at all while you were studying them?"

    p "No."

    r "Um, are you absolutely certain?"

    p "Yes. I would have noticed change."

    r "Well... they looked differently last time I checked."

    p "When was that?"

    r "A few hours before coming here."

    p "Hm. Interesting. Perhaps they are deteriorating? That would be unsurprising."

    r "Really? Why?"

    p "If something can't heal itself, slow deterioration is not unusual."

    r "I see."

    p "Do you know anything about the injury that Flandre didn't say?"

    r "No."

    p "Ok."

    r "And don't push her about it."

    p "I won't."

    r "Good."

    "Patchouli stands up."

    p "I'm going to check something."

    r "Ok. Go ahead."

    "Patchouli grabs Remilia's wings. Remilia quickly leaps across the room, out of her grip."

    r "Hey! What are you doing?"

    p "Checking your wings."

    r "Don't touch them like that!"

    p "But you said go ahead?"

    r "I didn't mean me!"

    p "Oh. Sorry."

    r "Don't just touch a vampire's wing like that."

    f "What are you doing?"

    "Remilia jumps."

    r "Oh, Flandre."

    p "I'm learning vampire etiquette."

    r "She touched my wing without a care in the world."

    f "Oh. Is that one of those weird things you were worried about, sis?"

    r "No. Never mind, this is stupid."

    "Remilia walks out of the library."

    f "Wait, sis!"

    "She follows her out."

    f "Where are you going?"

    r "I'm tired. I'm going to sleep."

    f "Ok. Me too, those books are confusing."

    r "Did you learn anything from them?"

    f "Mercury is cool."

    r "Hm. Ok then."

    "Remilia picks Flandre up."

    r "Let me fly you down this time."

    f "Ok."

    "They hover over the main hall."

    f "It's fun, seeing things from way up."

    r "Yes. It is."

    f "I can't wait for Patchouli to fix my wings. Then we can fly all over the world."

    r "I'd love that."

    "They continue to float around the room."

    f "Were you getting along with her?"

    r "Um, kind of?"

    f "What did you talk about?"

    r "Just about the wings more. She seems to be getting a better idea."

    f "And then she touched yours?"

    r "Yeah... then she did that. She doesn't understand vampires too well yet."

    f "We have to fix that."

    r "Yes. If she goes around touching wings like that, she won't live very long."

    f "Hehe, not at all."

    "They fly down to the ground at the door, then enter their room."

    f "Oh, another chicken!"

    r "Chicken again?"

    "They eat together, then go to sleep."
    
    return
