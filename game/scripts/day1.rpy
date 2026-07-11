label day1:

    call day1_forest
    call day1_library
    call day1_end

    return
    
label day1_forest:
    scene bg_forest

    play music bgm_forest fadein 2.0

    f "Remi! Look out!"

    "Remilia swerves upwards, narrowly avoiding a tree."

    r "That was close."

    f "Just land already! You've been flying for hours!"

    r "No, no, I can still..."

    "They slowly drift downward, back into the treeline."

    f "Remi!"

    r "Oh—"

    "They blast through a wall of thin branches."

    f "See! You're going to kill yourself like this!"

    r "Fine."

    play sound sfx_forest_land

    "Remilia drops down from the air and catches her breath. Flandre steps down from her back."

    f "Geez, Remi."

    "Remilia takes Flandre's hand."

    r "We need to keep moving, trees aren't good enough shelter from the sun. It will cut through the leaves."

    f "But you're pushing yourself to death. Slow down."

    r "I'm just trying to..."

    "She takes a deep breath."

    r "I'll be careful. Are you able to walk?"

    f "I'll try."

    play sound sfx_forest_footsteps
    with forest_walk_fade

    f "Hey... I'm getting really tired. I need a break."

    r "We don't have time. We need to keep moving."

    play sound sfx_forest_land 

    f "I can't."

    "Remilia kneels down and places her hand on Flandre's hat."

    r "Alright. We'll spare a few minutes."

    "Remilia begins to get up, but gets pulled back down."

    f "You need rest too."

    r "It will just be for a moment."

    "Flandre sighs and lets go."

    "Remilia leaves, and quickly returns with a rabbit in hand."

    r "Here."

    f "Thank you."

    "Flandre devours half of it."

    f "Here's the rest."

    r "I'll be alright."

    f "No you won't. You're hungry too."

    r "You need it more. Please finish it."

    f "Fine."

    "Flandre finishes and tosses the bones aside."

    r "How are your wings feeling?"

    f "They hurt."

    r "Has the pain lessened at all?"

    f "No."

    r "I see."

    "Remilia looks off to the sky. The purple foreglow of sunrise begins to show itself."

    r "We need to move."

    f "Ok..."

    "Flandre grabs Remilia's hand and pulls herself up."

    r "There must be some kind of shelter. Hunters build cabins out here."

    f "Vampire hunters?"

    r "No, animal. Don't worry."

    "Flandre grabs Remilia's hand as they begin walking."

    play sound sfx_forest_footsteps
    with forest_walk_fade

    r "Oh?"

    "Among the trees, they find a large, old-looking building."

    r "Odd. But it is shelter."

    f "What if someone scary is in there?"

    play sound sfx_forest_land

    "Remilia steps to the door and grabs the handle."

    r "We have no choice. Come, I'll keep you safe."

    "The edge of the sun begins to rise, stinging their vampiric skin."

    "Then, they enter the mysterious building together."

    return

label day1_library:
    stop music fadeout 2.0

    call scene_transition_fade("bg_library")

    "They step into a large library. Bookshelves line the walls, and a large staircase lies straight ahead."

    "Flandre leans into her sister's ear."

    f "Do you think anyone is here?"

    "Remilia takes Flandre's hand."

    r "Let's take a look. Try to keep quiet."

    "They take a few steps into the room."

    play sound sfx_magic_clash_2

    "Something fires at Remilia's neck, but she summons her spear to block at the last moment."

    play music bgm_duel fadein 2.0
    
    r "Get behind me!"

    "An onslaught of attacks comes from various directions."

    "The attacks stop as a purple figure appears in the air. A mass of crystals appear around her and begin to glow. Yellow on her left, blue on the right."

    "Remilia lifts her spear, charging it up in response."

    play sound sfx_magic_thunderous

    "The crystals fire beams of light and water, Remilia meets them with a flash of energy from her spear. The attacks cancel each other out."

    "Remilia's knees buckles for a moment. Flandre holds Remilia from behind, stabilizing her. The magician watches intently."

    p "Leave, monsters."

    r "We can't! We just need shelter for the day."

    "The crystals begin charging again."

    p "A shame."

    r "Damn it."

    play sound sfx_magic_thunderous

    "Remilia charges her spear again, and the beams collide. Remilia nearly goes limp in Flandre's arms, heavily breathing."

    f "Sis..."

    play sound sfx_magic_thunderous

    "Again, the crystals charge. The spear charges, but slowly flickers. They collide yet again."

    play sound sfx_body_fall

    "As the crystals charge again, Remilia drops."

    f "Sis, no!"

    play sound sfx_magic_cast

    "Flandre steps in front of Remilia's body and summons her sword. The magician charges her crystals."

    f "Hah!"

    play sound sfx_magic_thunderous

    "The red slash collides with the lasers, splitting them in half and making them hit the ground next to the sisters."

    play sound sfx_body_fall

    "Flandre drops to her knees, breathing frantically."

    stop music fadeout 2.0

    "The magician slowly floats down in front of them."

    p "It appears neither of you can fight anymore."

    f "We never wanted to! We just want to rest!"

    p "This is a magician's domain. A poor choice."

    f "We had to! The sun will kill us!"

    p "Hmm..."

    p "I've never seen vampires before. I want to study you. On that condition, you may stay."

    f "Fine!"

    play sound sfx_door_open

    p "Your room is over there. Go on."

    play sound sfx_rustle_2

    "Flandre slowly picks up Remilia and leans her onto herself, but buckles and drops to her knee."

    p "Hm. I suppose you are rather exhausted."

    play sound sfx_magic_summon

    "They suddenly float into the air."

    f "Whoa."

    call scene_transition_fade("bg_bedroom")

    "They move through the door and gently land on the floor. The magician follows closely behind."

    return

label day1_end:

    p "That is all I shall do for you today. Rest well, I need healthy subjects."

    f "Um... I can't sleep. My wings... they burn."

    p "Hmm. Bring them here."

    "Flandre stumbles over, presenting her back."

    r "What do you plan on doing with them?"

    f "Sis, you're awake!"

    r "I was the whole time. I just couldn't move."

    p "Then you should understand your situation. I am studying a vampire, as agreed. Be silent."

    "Remilia sits up and stares her down."

    "The magician leans in close to the wings for a few moments."

    play sound sfx_magic_summon

    p "I numbed them."

    f "Yay! Thank you!"

    p "Is that all?"

    f "Um... can we have coffins?"

    p "...Why?"

    f "Sorry, never mind."

    p "Then I belie—"

    r "No, it's important. Vampires recover far quicker inside one. If you want your test subjects to be at full health, you should bring some."

    p "Ugh..."

    play sound sfx_magic_summon

    "She summons two coffins onto the bed."

    p "No more."

    play sound sfx_stomach_growling

    r "..."

    f "Um, we're hungry. Sorry."

    p "I'll warp something later."

    "She walks over to the door."

    p "A word of caution. Try anything, you'll explode. So don't."

    "Remilia sighs as the magician finally leaves them alone."

    r "What a ridiculous situation."

    f "But we have shelter."

    "Remilia stands and stretches."

    r "Indeed. How are your wings doing? Did she do anything strange?"

    f "Nope! I can't feel them! It's great! I can finally—"

    play sound sfx_body_fall

    "Remilia drops to the floor."

    f "Ah, Remi!"

    "She runs over and kneels down beside her."

    f "You seriously passed out? Ugh, I told you to eat."

    play sound sfx_rustle_2

    "Flandre picks her up and drops her into a coffin. She sits on the edge of the bed."

    f "We really need food..."

    play sound sfx_magic_summon

    "After a few moments, a dead chicken appears on the table."

    f "Oh, it's here!"

    "She feeds Remilia the chicken's blood."

    f "Take care of yourself too. Stupid sis."

    "Flandre finishes the chicken, then jumps into the other coffin."

    scene black with fade
    play sound sfx_coffin_close

    f "I can finally..."

    "She passes out instantly."

    return
