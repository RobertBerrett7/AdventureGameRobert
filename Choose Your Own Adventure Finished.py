i = 0
while i == 0:
    def StartOver():
        StartOver = input("Would you like to play again? \n")
        if StartOver == "Yes":
            i = 0
        if StartOver == "No":
            i = 1

    def start_game():
        print('Amidst a world teeming with humans and the wistful presence of monsters and ghouls, you, a dedicated detective yearning to establish your prowess, found yourself hired to oversee the violent parties unfolding within the shadowy halls of the Wicked Mansion of the West. As you entered, hushed murmurs and suspicious gazes immediately greeted your arrival. Yet, your attention was swiftly captured by a plump, round lady adorned in a sparkly blue dress, accompanied by a gnome-like creature that trailed behind her hidden slightly under her dress.')
        print('"Hello! You must be the detective. What is your name?" the woman inquired, her tone resonating with an air of intrigue and authority.')
        global User_name
        User_name = input("Enter Your Name: ")
        print('"Well, pleased to make your acquaintance, detective ' + User_name + '," Lady Mediterranean, with her majestic centaur-like presence, introduced herself. Her lower half bore the resemblance of a tawny brown horse, exuding an aura of both magnificence and commanding charisma. "I have experienced a series of unfortunate... incidents at my previous gatherings. Hence, I have summoned you to unearth the perpetrators. Although I must confess, I do relish~ the dramatics of it all! You have two areas to inspect presently: the dance floor or the library."')

        Dance_or_Library = input('Enter your choice, 1 is The Dance Floor, 2 is the Library: ')

        if Dance_or_Library == '1':
            Dance_Floor()
        elif Dance_or_Library == '2':
            Library()
        else:
            print('Invalid choice. Try again.')
            start_game()

    def Dance_Floor():
        print('Amidst the pulsating beats of the music, Lady Mediterraneans booming voice directed you toward the dance floor. And Suddenly ' + User_name + ' hears a squeaky voice! "Hello I am the invisible woman, I will be your narrator on this path. Distinguished, fancy, and detailed describe me."  The resonating voice of the centaur faded as you reached the area, scanning the surroundings for any signs of discord. Abruptly, a shrill cry shattered the air: "It is dreadful! It is dreadful! The Mad Scientist is dead!" Rushing to the scene, you find an assemblage encircling the lifeless body of an elderly man, a small fairy sobbing near his side. The deceased figure, dressed  in a lab coat, small spots of small, greenish mutations scattered across his body—an eerie testament to his experiments. Without visible wounds, your deduction pointed to poison as the likely cause of death. Turning to the distraught fairy, you inquired about any potential enemies The Mad Scientist might have had. Trembling, the fairy stuttered, “H-h-hello, ' + User_name + '.  He did not uh have th-the best relationship with a few~ individuals at this gathering, notably The Vampire Twins and his son, Frank the Frankenstein." You decide to speak with one of these individuals')
        TwinsOrFrank = input('Enter your choice (1 is for Vampire Twins or 2 is for Frank): ')

        if TwinsOrFrank == '1':
            Vampire_twins()
        elif TwinsOrFrank == '2':
            Frank()
        else:
            print('Invalid choice. Try again.')
            Dance_Floor()

    def Library():
        print('As our hero steps into the library, they are hit with a sight to behold! First off, they notice the handsome and devious narrator, the invisible man, although they can not see him. They notice that he is the best, and that he will be the one directing them in this part of the story. If you had gone to the dance floor, they would have to deal with too many big words and descriptions with little miss invisible women, too much for the little old, invisible man. Books line the walls like a colorful army of knowledge. But hey, there is this one book standing out like a beacon in the sun, shining brighter than the rest! Then, hold up a sec! What is that on the counter? A crossbow just chilling there, looking all important and stuff. But wait, footsteps echo outside the door. Time is ticking, and it is decision time! Does' + User_name + ' wanna crack open the case of that mysterious book or grab that crossbow and figure out what is up? Choices, choices! So, what is the call, folks? Investigate the mysteriously radiant book or snag that crossbow before someone busts in?')
        Book_or_crossbow = input('Enter your choice (1 for Book or 2 for Crossbow): ')

        if Book_or_crossbow == '1':
            book()
        elif Book_or_crossbow == '2':
            crossbow()
        else:
            print('Invalid choice. Try again.')
            Library()
    
    def Vampire_twins(): 
        print('Opting to investigate further, you approached the area indicated by the fairy, only to be confronted by a surprising sight: conjoined twins, a male and female fused at the hip, their pale complexions and protruding fangs standing out. Your curiosity got the better of you, prompting an unexpected query about their unique arrangement. Responding in unison, the twins revealed, "Mr. Stupid Scientist was furious when our mothers path crossed his, resulting in our lifelong conjoining!" However, when the accusation of The Mad Scientists demise arose, the female twin, Violet, countered with an response, "Oh, so you are pinning this on us. Someone among us decided to go on a spontaneous road trip, causing our delayed arrival so it could not have been us!" She glares at her brother. So with that you decide to leave the twins alone even with your suspicions. You are about to leave to head to Frank but then you start to hear gurgled screams coming from the hallway.. On the other side of the party you see Frank enter small hall.  Do you follow Frank or the screams?')
        Vampire_twins = input('Enter your choice (1 for Scream or 2 for Frank): ')
        if Vampire_twins == '1':
            Scream()
        elif Vampire_twins == '2':
            Follow_Frank()
        else:
            print('Invalid choice. Try again.')
            Vampire_twins()

    def Scream():
        print('Follow Scream: You decide to follow the screams. You creep and slowly follow as the gurgles get louder as you walk. When you arrive you met with with Slumpy the slime monster. Slumpy that says, ”I-I A-a-am SooooOOOoooo Sorry! I was hired to distract you.” you dash out running towards where Frank was but when you arrive he is dead. You look up and the gnome that was behind Mediterranean In front of you with a bow ready to launch. He releases the arrow and it flies at you. Everything fades to black. You have found, ”The Slumpy Ending,”')
        StartOver()
    
    def Frank():
        print('Engaging Frank, an imposing figure resembling a skyscraper, you introduced yourself, cautiously broaching the subject of his fathers demise. His response, dismissive yet emphatic, resonated with a hint of disdain, "Yeah, heard about it you weirdo. My father was a miserable man, but killing him? Too much effort. I would rather indulge in this punch." However, before further inquiries could be made, Franks attention is sharply diverted, his gaze locking onto an unseen presence. With a sudden eruption of anger, he snarled, "I SEE YOU, GET BACK HERE, YOU GNOME!" Hastily, he dashed toward a closing door, leaving a trail of spilled punch in his path. The urgency of the moment prompted a crucial decision: whether to pursue Frank or stay explore an alternative path.')
        Follow_or_Wait = input('Enter your choice (1 for following Frank or 2 for waiting): ')
        if Follow_or_Wait == '1':
            Follow_Frank()
        elif Follow_or_Wait == '2':
            Waiting()
        else:
            print('Invalid choice. Try again.')
            Frank()
    def Follow_Frank():
        print('Chasing after Frank, his looming figure disappearing into the entrance of the library, you hasten your pace to catch up eventually reaching a door. The sounds of murmured voices within urged you to swiftly push open the heavy door. The atmosphere in the library Is charged with an air of suspense, an energy that hinted at revelations just on the cusp of being unveiled. Fumbling through the door, your eyes swiftly surveyed the room. The scene before you unfolding into a tapestry of truths. Standing at the center is Lady Mediterranean, now adorned in a vibrant yellow dress, exuding an air of serene curiosity. "Hello, ' + User_name + ' Do you need anything?" she inquired, her voice carrying a gentle inquisitiveness. Your curiosity sparked a yearning for more Info on her conversation she just had. Probing further, you pressed for details. Lady Mediterranean, or so you thought, suddenly shifted, a sense of quiet vulnerability taking over as she confessed, "I am not actually Mediterranean. I am her sister Marigold. My sister detests these lavish gatherings and often conceals a trick or two up her sleeve during these events. I have a feeling she is hiring someone to take out her enemies. And I have just the idea of how to figure out who." As the words hang in the air, a shift in the rooms dynamics is heralded by the entry of an old woman dressed in a stereotypical witch attire. Frank, present in the room, reacted with a momentary jump but soon regained his composure. The two begin to do an incarnation without an introduction of the old woman. Suddenly Marigolds eyes open in a glow and speaks "I think my sister hired th-," Marigold began before her words were tragically cut short, as she fell to the floor dead. Triggering Screams from around the room. The witch, who you strangely now know the name of, Luna..., with an air of mystery and a hint of arcane power, addressed the situations, explaining, "Marigolds sister must have discovered our plan and took her out. But with my powers, I can bring one individual back. The choice is yours: to revive Marigold or The Mad Scientist."')
        Marigold_or_Scientist = input('Enter 1 for Marigold and 2 for Scientist')
        if Marigold_or_Scientist == '1':
            Revive_Marigold()
        elif Marigold_or_Scientist == '2':
            Revive_Scientist()
        else:
            print('Invalid choice. Try again.')
            Follow_Frank()

    def Revive_Scientist():
        print('As you make the weighty decision to revive The Mad Scientist, the scene around you begins to tremble and whirl. An immense, pulsating light materializes in front of you, casting an eerie glow across the space. With a sudden, otherworldly energy, the space distorts and contorts, as if pulling from the fabric of another dimension. From within this extraordinary display, The Mad Scientist emerges, stepping forth as if through a cosmic gateway. Your questions spill out in a frantic rush, inquiries about his demise, the events that transpired, seeking answers to unravel the mysteries that shrouded his death. The Mad Scientist, wearing a maniacal grin, responds, "I could not see with my awful glasses, but how about I steer you onto a different pathway? What if you ventured into the library?" Abruptly, a whirlwind of washing light envelops you, swirling and spiraling in a torrent of energy. The atmosphere crackles with electricity, as if reality itself bends and reshapes around you. A sensation of weightlessness overcomes you as the world blurs and morphs, transporting you when suddenly you see a second path in this weird space, will you choose path you are supposes to go on number one or  switch to path Two? ')
        One_or_Two = input("Enter 1 for one and 2 for two")
        if One_or_Two == '2':
            Mishap()
        elif One_or_Two == '1':
            Library()
        else:
            print('Invalid choice. Try again.')
            Revive_Scientist()

    def Mishap():
        print('The world wavers when suddenly the tunnel of transportation goes pitch black, with this you end up in the library at a later moment than the original path, and you find yourself transported into the library.  There, in the same space and time, you witness another you– an identical version of yourself hastening through the library doors, desperately in pursuit of Frank. The sheer impossibility of encountering your own self staggers you. The moment is fleeting, for in the next instance, a tragic turn of events unfolds before your eyes. As you stand face-to-face with your own mirrored self, frozen in disbelief, the silence is ruptured by a sudden, fatal shot that echoes through the room. The other "you" collapses, lifeless, in an instance that defies the laws of existence, the consequence of two identical beings coexisting in the same timeline. The fabric of reality quivers, and the world around you starts to dissolve. A disintegration begins, a vanishing act that erases your entire existence as you no longer exist on the timeline, an abrupt dissolution brought on by the impossibility of your presence, leaving behind a void of nothingness. This marks the "Mad Scientist Ending." ')
        StartOver()

    def Revive_Marigold():
        print('In consideration of Lunas observations and insights that Marigold would know more, the decision is made to revive Marigold. The world around you shifts and distorts, ushering in a moment of upheaval. A brilliant, swirling light emerges, birthing Marigold from the confines of the cosmic display. Breathless but resolute, Marigold proclaims, "I know who the killer is. Its my sister and her little gnome!" Her revelation triggers a recollection of the devised plan to expose the culprits and ensure justice. A partnership with Frank was forged, intending to distract the attendees while the other pair would root out the malefactors. The weight of the situation presses, and Luna, the observer, steps forward, her gaze intent. "I have been watching, and Marigold has crucial information," she asserts, her voice carrying a tone of quiet determination. "She has been vigilant and may hold the key to unravelling this mess." As the realization sinks in, the world swirls around you. The emergence of Marigold, an embodiment of this strategic revelation, brings a tense moment of clarity. Positioned within the heart of the gathering with Frank, a profound sense of duty settles upon you. Contemplation ensues – do you adhere to the original strategy, entrusting Marigold and Frank, or do you embrace the pivotal role, seizing the responsibility to uncover the culprits, feeling the weight of honor and duty resting upon your shoulders???')
        Glory = input("Enter 1 if you want to take the glory for yourself and 2 if you follow out the original plan")
        if Glory == '1':
            Take_Glory()
        elif Glory == '2':
            Follow_Plan()
        else:
            print('Invalid choice. Try again.')
            Revive_Marigold()
    
    def Take_Glory():
        print('A sudden urge to alter the course of events takes over. In an unexpected turn of events, you seize the moment and, with a resounding cry, you exclaim, “The killer is the gnome and Lady Mediterranean. She has been commanding the gnome to execute all her desires!" Pandemonium erupts as everyone scans the room for the culprits, the realization dawning too late. Lady Mediterranean, standing by a lever, unleashes a spine-chilling cackle, declaring, "It Is time for you all to perish!" With a malevolent grin, she yanks the lever, triggering a catastrophic explosion that engulfs the mansion in flames. The frantic chaos is punctuated by a deafening roar, and the very last sound heard is a lingering ring. The scene comes to a startling end, marked by an unforeseen and calamitous twist, the revelation that "Glory Was Not The Answer Ending" ')
        StartOver()

    def Follow_Plan():
        print('Feeling a surge of adventurous zeal, you decide to stand by the original plan. With a wink to Frank, the two of you execute an audacious and zany performance, causing a raucous stir, as if you were the masterminds behind it all. "I have got you now, my sister!" Marigold shrieks, appearing out of the blue and restraining Lady Mediterranean, who has taken aback. "Aha! I nabbed the little killer too!" Luna, the witch, adds with an air of triumph. The scene becomes a cacophony of surprises, confusion, and sudden realizations. "In fact," Marigold exclaims, "I am Marigold, Mediterraneans sister! And right here, my trusty sidekick is Luna the witch. My sister is the true perpetrator, and both ' + User_name + ' and Frank played their part splendidly by distracting everyone. This allowed us to apprehend her and her sidekick. It has been my sister guiding the Gnome to unleash havoc on those she despises." Years pass, and life takes a thrilling turn as you become a renowned and prosperous detective, solving case after case. You revel in a sense of fulfillment and joy. Yet, in moments of reflection, an odd discovery comes to light. Glimpsing at your own reflection, you sense a peculiar familiarity, a subtle resemblance to Mediterranean and her mischievous gnome, an unexpected piece of them residing within you. The adventure concludes with an unexpected twist: "But Are You Really Not The Killer? Ending."  ')
        StartOver()

    def Waiting(): 
        print('Amidst the dilemma, you decide to stay behind, feeling a twinge of hesitation about chasing after Frank. But before your contemplation deepens, a sudden shriek pierces the air, delivering haunting news, "F-Frank has been murdered!" An overwhelming sense of regret and guilt engulfs you, the question of what might have transpired if you had chosen differently weighs heavily on your mind. However, the current reality presses on, demanding immediate attention. Abruptly, Lady Mediterraneans voice breaks through the turmoil, drawing everyones focus, "I found a note. It is from the murderer." Her tone, a mix of concern and urgency, rouses the gathering. "It reads, "I want to play a little game with the ' + User_name + '. If you can guess who I am, I shall come forward and you may capture me. But if you fail, you shall all meet a horrible demise." So, ' + User_name + ', who do you think it is?" Time seems to slow, the air heavy with anticipation as every conceivable suspect flickers through your mind. The room falls into an eerie silence, each individual grappling with their suspicions and contemplations. The weight of the situation bears down upon you, the pressure to identify the mysterious orchestrator of these heinous acts mounting.')
        Accusation = input("Please enter the persons name you acuse with correct spelling and a capital at the start of the name. Some options you have met are: Yourself (Put Myself), Frank, Mad Scientist, Vanpire Twins, Mediterranean, Gnome, and (There's also more options from other storylines you can input):\n")
        if Accusation == 'Myself':
            Myself()
        elif Accusation == 'Frank':
            Accuse_Frank()
        elif Accusation == 'Vampire Twins':
            Accuse_twins()
        elif Accusation == 'Mediterranean':
            Mediterranean()
        elif Accusation == 'Gnome':
            Gnome()
        elif Accusation == 'Marigold':
            Accuse_Marigold()
        elif Accusation == 'Luna':
            Luna()
        elif Accusation == 'Sunny':
            Sunny()
        elif Accusation == 'Zero':
            Zero()
        elif Accusation == 'Slumpy':
            Slumpy()
        elif Accusation == 'Mad Scientist':
            Accuse_Mad_Scientist()
        elif Accusation == 'Fairy':
            Fairy()
        else:
            print('Invalid choice or Spelling. Try again.')
            Waiting()

    def Accuse_Mad_Scientist():
        print('Amid the tense silence, the weight of suspicion hung in the air like a heavy fog. The moment had arrived for the grand accusation, the ultimate gamble in this grim game of wits. The detective, with a mix of confidence and trepidation, pointed up dramatically "It is the mad scientist! You are the culprit behind this diabolical scheme!" Lady Mediterraneans eyes widened for a brief moment before she let out a scoff, her voice laced with a mix of disbelief and a touch of dark humor. "The Mad Scientist? You lunatic, look over there, he is already lying lifeless." Her gesture pointed to the corpse, solidifying the futility of the accusation. "But then who—?" The detectives question hung in the air, drowned out by the sudden turn of events. Mediterranean, in an unexpected twist, revealed her true intentions. With a swift, unexpected move, she produced a grappling hook, aiming it at a small, flying contraption maneuvered by none other than the mischievous gnome. "You will all be the same soon," she ominously declared, her words hinting at impending doom. With precision, the grappling hook snaked out, seizing the airborne contraption with the gnome aboard. Before anyone could react, Lady Mediterranean and the gnome soared through a window into the night sky, bidding an enigmatic farewell in French. Suddenly, a deafening explosion shattered the mansion, the force hurling debris in all directions. ' + User_name + ' vision blurred, a white light enveloping the fading sight. Guessed A Corpse Ending')
        StartOver()
    
    def Accuse_Frank():
        print('Amid the tense silence, the weight of suspicion hung in the air like a heavy fog. The moment had arrived for the grand accusation, the ultimate gamble in this grim game of wits. The detective, with a mix of confidence and trepidation, pointed up dramatically "It is the mad scientist! You are the culprit behind this diabolical scheme!" Lady Mediterraneans eyes widened for a brief moment before she let out a scoff, her voice laced with a mix of disbelief and a touch of dark humor. "The Mad Scientist? You lunatic, look over there, he is already lying lifeless." Her gesture pointed to the corpse, solidifying the futility of the accusation. "But then who—?" The detectives question hung in the air, drowned out by the sudden turn of events. Mediterranean, in an unexpected twist, revealed her true intentions. With a swift, unexpected move, she produced a grappling hook, aiming it at a small, flying contraption maneuvered by none other than the mischievous gnome. "You will all be the same soon," she ominously declared, her words hinting at impending doom. With precision, the grappling hook snaked out, seizing the airborne contraption with the gnome aboard. Before anyone could react, Lady Mediterranean and the gnome soared through a window into the night sky, bidding an enigmatic farewell in French. Suddenly, a deafening explosion shattered the mansion, the force hurling debris in all directions. ' + User_name + ' vision blurred, a white light enveloping the fading sight. Guessed A Corpse Ending')
        StartOver()

    def Zero():
        print('In a surprising turn of events, ' + User_name + ', confronted with the challenge of identifying the mysterious culprit, chose to say "zero." Lady Mediterranean stood, almost motionless, a perplexed expression lingering on her face. The gnome, growing impatient, began to scuttle forward, emitting high-pitched squeaks, "The plan, the plan, the plan." As it readied its crossbow, Mediterraneans patience snapped, and with a swift, precise motion, she brought her hoof down with force, shattering the ceramic gnome into a cloud of dust. At that moment, the detectives keen observation took a peculiar turn. A closer scrutiny of Lady Mediterranean unveiled unsettling details: a sinuous, snake-like tongue flickering briefly from her mouth, eyes bearing a vivid yellow shade with a slitted reptilian appearance, and an unexpected sideways blink, mirrored to a reptiles peculiar eye movement. Before anyone could react, the sudden transformation was quickly shrouded in an eerie sense of nothing. The music surged back to life, the lights illuminating the space once more. It was as if a strange force had abruptly ended, and everything reverted to its prior state, erasing the bizarre revelation as if it had never occurred. The air was once again filled with the pulsating beats of the music, the guests resumed their conversations, and the inexplicable occurrence dissolved into the murky shadows of uncertainty, leaving the detective pondering the cryptic enigma that was this Lady Mediterranean. Lady Mediterranean…Ending')
        StartOver()

    def Slumpy():
        print('As the detective identifies "Slump" as the potential culprit, the slimy, slithery creature, Slumpy, gradually inches forward. "WWwwWWwhhHHy dooooOOooo U tink it iss meH?" Slumpys voice, a blend of curiosity and caution, queries the detective.In response, the detective theorizes, "Perhaps the mutations on the Mad Scientists body were caused by Slumpys slime."Slump reacts with a defensive tone, "It wasnt meEEAAAaaaaHhh! I know whooOOOoo the real culprits arrrre, and it waAAAAaaaas not meh. I was just here to distract yoOOOOOOoooooou." With a swift and unexpected revelation, Slump asserts, "It is Mediterranean and the gnome" The detective swiftly turns to find Lady Mediterranean, but she is no longer there, leaving only the gnome behind for arrest. Fast forward to five years later, the detective, now an established and renowned figure in the world of investigation, narrates in a journal entry about the unsolved mystery of that night. Although no one was apprehended, the detectives career flourished. However, the whereabouts of Lady Mediterranean remained a mystery, as she was never found after that fateful night, leaving an enigmatic void in the narrative of that haunting investigation.Meh Ending')
        StartOver()

    def Myself():
        print('Lady Mediterranean, with a quizzical tone, responds, "Huh, okay."Following this unexpected turn, three ghoul police officers rush in, seizing ' + User_name + ' and swiftly dashing out with them in tow. As they reach the exit, ' + User_name + ' catches a glimpse of the ghoul police car with flashing lights waiting outside. However, as ' + User_name + ' is placed in the car, an abrupt explosion shatters the mansion, propelling the vehicle into the air. The car hurtles through the chaotic aftermath, only to find itself plunging into a bottomless pit, descending endlessly into an unknown abyss, perpetually falling for an eternity, leaving ' + User_name + ' trapped in an endless free fall, lost in the enigmatic depths of the void. Call Out Ending ')
        StartOver() 

    def Fairy():
        print('As ' + User_name + ' hesitantly points toward the fairy, Lady Mediterraneans response is one of surprise, "The fairy? Really?" A moment of tense silence envelopes the room, leaving an air of uncertainty hanging heavy in the atmosphere. Suddenly, the fairys delicate wings tremble, and she raises her hands in a defensive gesture, "Wait, it was not not me! I may play mischievous tricks, but I am not capable of such acts." Before any further dialogue could transpire, an unexpected distraction occurs. The lights flicker, plunging the room into momentary darkness. In that split second, Lady Mediterranean vanishes, leaving behind an eerie silence. The detective, bewildered, surveys the room, only to find the fairy gone as well. The guests exchange puzzled looks, perplexed by the abrupt disappearance of both characters. As the detective attempts to make sense of the situation, a mysterious note flutters down from above, landing at their feet. It reads, "The real game has just begun. Watch closely, detective." After the mysterious note falls, the scene shifts to five years later. The detective, now writing in their journal, details the eerie aftermath of that night. They recount how, after the peculiar events at the mansion, a slow unraveling began. It started with minor items vanishing, such as shoes and personal effects. But as time progressed, people close to the detective began to inexplicably disappear. Suddenly, as the narrative unfolds, theres an abrupt revelation. The perspective zooms out, revealing the detective seated in a completely blank room. The once lively space, now reduced to emptiness. All that remains is the detective, the journal filled with the chronicles of their experiences, and the pen in their hand. The chilling realization dawns upon the detective that they are completely alone in this barren, desolate space, surrounded by an unsettling void of nothingness. The enigma of that haunting night at the Wicked Mansion seems to have left a lasting, haunting mark on the detective, as they grapple with the solitude and the lingering mysteries that continue to haunt their existence. Gone Ending')
        StartOver()

    def Accuse_twins():
        print('Upon ' + User_name + ' selecting the vampire twins, Violet, feeling insulted, erupts into an uproar, yelling at the detective. Her brother tries in vain to calm her down, but her outburst is too overwhelming. The commotion alerts the ghoul police, who swiftly intervene along with the rest of the authorities. Amid Violets raging outcry, she cries out, accusing ' + User_name + ' of falsely accusing them and declares that ' + User_name + ' will face consequences. As the ghoul police apprehend the twins, Violet fervently vows revenge, her words echoing in the tense atmosphere. However, following the twins removal, an unsettling turn of events occurs. Lady Mediterranean and the gnome mysteriously vanish, leaving behind a disconcerting void. Shortly after their disappearance, the mansion abruptly explodes, leaving no trace of anyone behind, an eerie and unsettling conclusion to the nights events. Twins Ending')
        StartOver()

    def Accuse_Marigold():
        print('Following the detectives guess of Marigold, a figure dressed in resplendent gold, bearing an uncanny resemblance to Lady Mediterranean, steps forward from the shadows. "I am Marigold, Mediterraneans sister," she announces, revealing her identity. Lady Mediterranean steps out, her expression a mix of shock and disbelief. "I cant believe you wouldve done something like this to my party," she accuses Marigold, swiftly delivering a sharp slap, emphasizing her dismay. In a heated retort, Marigold, her voice laced with anger, counters, "Its actually you, Mediterranean, and your little gnome friend who are behind this." However, her accusation falls on disbelieving ears, as nobody seems to lend credence to her claim. In the midst of the escalating confrontation, the ghoul police arrive, seizing Marigold and promptly arresting her. Following her removal, the mansion succumbs to its usual fate, exploding into chaos as Marigold departs, leaving an unresolved conclusion to the nights events. The disappearance of those involved and the mansions destruction cast a dark shadow over the unexplained mysteries of the Wicked Mansion. ')
        StartOver()

    def Luna():
        print('two witches step forward. While Sunny, a bright yellow dressed witch, remains silent, Luna, stereotypical witch,  reacts by becoming angry and exclaiming, "It couldnt be Me, Or Her, Or Anyone!!! AHHAHAHAHAHA!" She engages in a heated conversation with the user, defending herself vehemently. Lunas anger intensifies, causing her to levitate into the air. Sunny, in sync, also ascends with a peaceful smile. Together, they release powerful beams of purple and yellow magic. The room erupts into chaos as the magic radiates, affecting everyone in the vicinity. As the beams of magic hit, the guests are transformed—some into frogs, others into sunflowers. The mansion itself undergoes a drastic change, turning into an overgrown, mystical swamp, forever altered by the witches powerful magic. The unresolved chaos leaves a haunting and eerie legacy within the Wicked Mansion of the West. Swamp Ending')
        StartOver()

    def Sunny():
        print('two witches step forward. While Sunny, a bright yellow dressed witch, remains silent, Luna, stereotypical witch,  reacts by becoming angry and exclaiming, "It couldnt be Me, Or Her, Or Anyone!!! AHHAHAHAHAHA!" She engages in a heated conversation with the user, defending herself vehemently. Lunas anger intensifies, causing her to levitate into the air. Sunny, in sync, also ascends with a peaceful smile. Together, they release powerful beams of purple and yellow magic. The room erupts into chaos as the magic radiates, affecting everyone in the vicinity. As the beams of magic hit, the guests are transformed—some into frogs, others into sunflowers. The mansion itself undergoes a drastic change, turning into an overgrown, mystical swamp, forever altered by the witches powerful magic. The unresolved chaos leaves a haunting and eerie legacy within the Wicked Mansion of the West. Swamp Ending')
        StartOver()

    def Mediterranean():
        print('Upon the detectives guess, Lady Mediterranean begins to slowly clap, acknowledging the correct deduction. "Congratulations," she chimes. Subsequently, she proceeds to explain that the entire scenario was orchestrated merely for her own amusement, as she harbors a love for mysteries. She discloses that the gnome was her partner, portraying all the "victims" in the elaborate charade. In a moment of disbelief, the twins express their outrage at the revelation, deeming the situation absurd. However, the tumult is interrupted by the sudden arrival of the ghoul police, who promptly arrest Lady Mediterranean. Following her arrest, the user, having unlocked the truth and demonstrated astute deductive skills, rises to prominence as a renowned detective, their name becoming well-known in the realm of solving enigmatic puzzles and mysteries. This unexpected turn of events marks the conclusion of the haunting and perplexing night at the Wicked Mansion of the West. Best Guess Ending')
        StartOver()

    def Gnome():
        print('Lady Mediterranean hands ' + User_name + ' an envelope. Inside, the message reveals the startling truth: “the gnome was indeed responsible for the events. He coerced Mediterranean into inviting guests who had been his past clients at his motor shop. These guests had been disrespectful to him, thus prompting his plan for revenge.” Upon the revelation, the gnome begins to frantically squeak, expressing a mix of denial and desperation saying “no no! Kind of right, Kind of wrong. NO NO!”, but his attempts to refute the accusations come too late. Lady Mediterranean congratulates the user, and the gnome is swiftly arrested, clinging onto Mediterranean as he is being taken away. The rest of the guests, relieved by the resolution, start to celebrate the victory, unaware of the impending danger. In an unforeseen turn, Lady Mediterranean slips away, revealing her own involvement in the plan. As she leaves, she triggers a device, causing the mansion to erupt into a destructive explosion, engulfing everyone inside. The night ends in an unexpected and catastrophic turn of events, leaving the mansion and its secrets buried within the devastation of the explosion. The haunting mysteries of the Wicked Mansion of the West come to a tragic and chilling conclusion. Missed Mastermind Ending')
        StartOver()

    def crossbow():
        print('Whoa,  ' + User_name + '  locks onto the crossbow, checking it out real quick. Its like a work of art, full of fancy intricate designs etched all over. But before they can dive deeper into that fancy piece, in busts...hold up, is that Lady Mediterranean? Dressed all golden and in a rush! She spots our hero holding the crossbow and jumps to conclusions like a sprinter off the block, hollering, "I have nabbed you now! You must be the one SHE hired!" Talk about a big misunderstanding! Now, here is the scene: Lady Med is charging in like a bullet train right at you.  ' + User_name + ' ’s got a choice to make: squeeze that trigger and fire away or just play it cool and let her catch them. Shoot or surrender? What is the move, champ? ')
        ShootSurrender = input("Enter 1 to shoot and 2 too surender")
        if ShootSurrender == '1':
            Shoot()
        elif ShootSurrender == '2':
            Surrender()
        else:
            print('Invalid choice. Try again.')
            crossbow()

    def Surrender():
        print('Whoa, surrendering to the chaos might seem like a safe bet, but here is the kicker! As  ' + User_name + '  throws in the towel, that scene takes a wild turn! Lady Med darts off and our hero runs right after her, aiming for a tackle. But boom! The tackle goes south, and the division between reality and dreamland gets all blurry. Through the fog, they catch a glimpse of a weird setup. A lady steps in and peels off her disguise, revealing she is Mediterraneans sister, Marigold! She spills the beans, claiming that  ' + User_name + '  was hired by Med as the “big baddie” And whoa, turns out our heros been following Meds evil plans! The cuffs come out, and it is off to a chilly jail cell. No more detective dreams – that is a wrap! Dreams Crushed By A Horse Ending. ')
        StartOver()

    def Shoot():
        print('Bam!  ' + User_name + '  takes the shot, and Mediterraneans golden self hits the ground like a sack of potatoes. Seemed like a good move at first, until – hold on to your hats! – in walks this ancient-looking lady. I mean, she is as old as grandpas old boots and dressed in the most “witchy” outfit you can picture. This old gal, Luna, goes bonkers, screaming, "You offed Marigold! Youre the big bad here!" Next thing you know, it is like stepping into a crazy game! Youre caught in a rumble with Luna, who calls in her lil sis, Sunny, another witch in the mix. Things just got turned upside down, landing you in a battlerama against the witchy duo. Get ready for a brawl in the mystical realm!  \n')
        print('Whoa, hold up! It is like suddenly a gaming interface pops above  ' + User_name + 's head, flashing a big ol 20, indicating their health. Looks like they have been sucked into a video game world – wild, right? Or maybe its an ol ilusian from the witches.  Meanwhile, hovering above the witches, Luna shows a 10, as do Sunny, signaling their health meters in this magical showdown. Luna kicks off the fight by sending a blast of purple energy, zapping  ' + User_name + '  for a solid six damage, bringing their health down to 14. At the same time, Sunny whizzes about, conjuring sparkly magic that gives her a health boost of three, perking her up to 13 health.  ' + User_name + '  takes a gander and finds themselves holding two options: a shield and some magical berries, allowing them to heal by four and shield themselves, or the trusty crossbow to nail one of the witches, dealing seven damage. Tough call – heal up and protect or take a shot at those magical mavens')
        ShootOrPro = input("Enter 1 to Protect and 2 too Take a shot")
        if ShootOrPro == '1':
            Protect()
        elif ShootOrPro == '2':
            Shot()
        else:
            print('Invalid choice. Try again.')        
            Shoot()

    def Shot():
        print('In a crucial turn of events,  ' + User_name + ' , feeling confident, takes the shot but unfortunately misses Luna, the intended target. Luna steps forward, a mix of surprise and understanding on her face. "That shot was far off the mark, my friend," Luna explains, her voice tinged with sympathy. "You cant be the culprit. The real mastermind is quite the sharpshooter. That hit on Marigold however earlier was good, she was Mediterraneans sister." Realization dawns on  ' + User_name + '  that Mediterranean, the true orchestrator, is more skilled and is already carrying out her plans, posing a serious threat to their targets. Luna emphasizes the urgency of the situation. "Mediterranean is swift and has already taken down several individuals. Time is crucial now. We must act fast." After a brief moment of discussion, they devise a strategic plan. "Youll confront the Mediterranean and the gnome," Luna explains, determination in her eyes. "While you keep them occupied, I will seize the opportunity to capture the Mediterranean when shes off-guard. And Sunny will do the same with the gnome." They set the plan in motion, each taking their designated roles. As the confrontation unfolds, theres a flurry of tense exchanges and quick movements.  ' + User_name + '  faces the Mediterranean and the gnome, engaging them in conversation about cake vs. pie while keeping them distracted, buying Luna and Sunny time to execute their parts of the plan. Finally, with coordinated efforts, they emerge triumphant. The culprits are apprehended, and peace is restored. "You did it! You helped us bring them down," Luna exclaims, relief evident in her voice. "Youve averted a catastrophe and now, youre well on your way to being one of the best detectives out there!"  ' + User_name + '  receives recognition and applause for their bravery and quick thinking, becoming a celebrated figure in the world of detectives, earning admiration and respect for their role in solving this intricate case. This marks a victorious and fulfilling ending, a testament to  ' + User_name + 's skills and determination. The Great Ending')    
        StartOver()

    def Protect():
        print(' ' + User_name + '  chooses to go for the heal and ends up feeling a lot better, health soaring up to a solid 18. They try to put up that shield to protect themselves, but oops – they fumble and pop it up upside down. Oopsie, a bit of a goof, or so the narrator says. Luna takes this snafu as a chance to strike, aiming a slightly smaller beam at  ' + User_name + ' . But lo and behold, its the shield that takes the hit, shattering in the process. Well, no more shieldy protection for our hero! Meanwhile, Sunny pulls a vanishing act, disappearing in a flash – poof! Its just you and Luna now. Whats the move, champ? Time to pull out the crossbow, have a chit-chat with Luna, or something else, since Sunnys gone missing? ')
        FireOrTalk = input("Enter 1 to Fire away with your crossbow and 2 to brag to Luna")
        if FireOrTalk == '1':
            Fire()
        elif FireOrTalk == '2':
            Talk()
        else:
            print('Invalid choice. Try again.')        
            Protect()
    
    def Talk():
        print('In a dramatic twist,  ' + User_name + '  opts for a chat with Luna, laying it on thick with the boasting: "Im the best, and Im here to best you. You might as well throw in the towel right now." But Luna fires back with an intriguing remark, saying, "I wouldnt be so sure about that." Out of nowhere, a dazzling light bursts behind the user, and Sunny, the sneaky little witch, reappears. She pounces, sinking her teeth into  ' + User_name + ' s neck, and a radiant golden light surges into them. Slowly,  ' + User_name + ' s life energy starts to drain, dwindling all the way down to zero and burning to a crisp, while Sunnys health shoots up to the stars. Sunnys betrayal turns the tide, bringing  ' + User_name + ' s defeat and paving the way for a whole new outcome. Unlocked The Boast To Toast Ending.')
        StartOver()

    def Fire():
        print('  ' + User_name + '  gears up, whips out their crossbow, and pulls off an unexpected move: they give the arrow a lick, adding a splash of water to the end for some extra oomph. The arrow goes zipping off, landing a solid hit on Luna, dealing a hefty blow that shaves a big chunk off her health. Thats a lot for sure! Now Lunas on her last legs, nearly down for the count. She attempts a final desperate blast, but all that comes out is a tiny flicker of energy. The feeble blast strikes the user before bouncing back and clipping Luna, leaving her hanging on with just a single health point. Whats the play here? Finish her off and end this magical melee or opt for a little chat with Luna in her weakened state? The choice is yours! ')
        FinnishOrTalk = input("Enter 1 to finish her off and 2 to brag to Luna")
        if FinnishOrTalk == '1':
            Finish()
        elif FinnishOrTalk == '2':
            Talk()
        else:
            print('Invalid choice. Try again.')        
            Fire()

    def Finish():
        print(' After choosing to finish Luna off,  ' + User_name + '  takes aim and fires, hitting Luna squarely and causing her to melt away, defeated. But wait, as the victory sinks in, a sudden surprise! Sunny reappears behind the user and sinks her teeth into them, draining their health down to just eight. After draining the users health, Sunny, with a mischievous glint in her eye, suddenly whispers something chillingly cute: "You smell like adventure and wonder, but its time to play a different game now, one that you wont win!" The eerie cuteness of her words adds an unsettling yet strangely adorable touch to the intense situation. Now faced with this intense situation,  ' + User_name + '  has a critical choice to make. Should they take a stand and attack Sunny with the crossbow, or will they opt for a chat, trying to reason with her despite the dire circumstances? The decision is yours to make! ')
        FireOrTalk2 = input("Enter 1 to Fire away with your crossbow and 2 to talk with Sunny")
        if FireOrTalk2 == '1':
            Fire2()
        elif FireOrTalk2 == '2':
            Talk2()
        else:
            print('Invalid choice. Try again.')        
            Finish()

    def Fire2():
        print('In this intense moment,  ' + User_name + '  takes the daring step to attack Sunny. As the arrow is released, it strikes Sunny, bringing her down to a mere 1 health. But in a surprising twist, at that exact instant, a small gnome and a peculiar, jiggly slime creature rush in. The gnome glances at the user, snatches the crossbow, and swiftly fires, delivering the final blow to Sunny, ending her. With the chaos around, the slime creature moves closer to  ' + User_name + '  and murmurs in a muffled voice, expressing deep regret: "Im sorry, Ive been commanded to eliminate you by the true mastermind, the gnome." As the scene fades,  ' + User_name + '  starts to vanish from existence. What a whirlwind of an encounter!  ' + User_name + ' , Luna, and Sunny all embroiled in attacks against each other, leading to the gnome and the true mastermind executing their scheme. Unfortunately, this turn of events results in  ' + User_name + ' s loss. Quite the unexpected outcome! Defeat You, Defeat Me Ending')
        StartOver()
    
    def Talk2():
        print('In a last-ditch effort,  ' + User_name + '  attempts to reason with Sunny, suggesting its time to scram and worrying they might have squandered too much time. After much back-and-forth discussion, they eventually team up and head out together. However, when they finally make it outside, its a grim sight: the culprits have already nabbed everyone at the ballroom. Just as hope seems lost, the real Mediterranean, now clad in a blue dress, emerges with the small gnome by her side, claiming victory over  ' + User_name + ' . With a sinister click, she triggers an explosion that engulfs everything. But in a glimmer of hope, Sunny uses her final burst of power to conjure a protective shield around  ' + User_name + ' , shielding them from the blast. While  ' + User_name + '  is saved from the explosion, theyve been propelled too far away. Everyone else, however, has vanished, leaving  ' + User_name + '  utterly alone. Later,  ' + User_name + '  tries to inform the authorities but ends up losing credibility, losing their job as a detective, and finding themselves homeless, living life on the streets. A bittersweet and solitary outcome for  ' + User_name + ' . Ran out of Time Ending')
        StartOver()

    def book():
        print('As  ' + User_name + '  curiously selects the mysterious book, a hidden mechanism is activated, revealing a secret door behind the bookcase. Eagerly exploring this newfound passage,  ' + User_name + '  crawls through the vent system, all the while overhearing snippets of the partys revelry. A rather clumsy moment occurs when part of the vent gives way, sending  ' + User_name + '  plummeting into an unknown room. Upon regaining consciousness,  ' + User_name + '  is greeted by an unusual sight - a peculiar, snake-like creature with a penchant for a sibilant lisp. The creature, whose identity remains shrouded in secrecy, presents an oddly demanding request. "Hello there, User! Now, I cant tell you who I am  but you may call me zero, but Ive got a favor to ask," it hisses, the "s" sounds a bit exaggerated. "Ive got this nifty talent for transforming folks into others, see? And Id love for you to step into the shoes of the gnome." This enigmatic creature goes on to explain that the gnome, acting under the guidance of Mediterranean, is behind the recent mayhem. "Your mission, should you choose to accept it, is to masquerade as the gnome, give em the old heave-ho, and then take their spot in Mediterraneans little get-together," the creature hisses, albeit with a whimsical flair. "Thats all there is to it. What do you say?"')
        AgreeOrNot = input("Enter 1 to agree and 2 to say no")
        if AgreeOrNot == '1':
            Agree()
        elif AgreeOrNot == '2':
            Disagree()
        else:
            print('Invalid choice. Try again.')        
            book()

    def Disagree():
        print(' ' + User_name + '  decides to decline the peculiar snake-like creatures request. In response, the creatures demeanor shifts ominously. It suddenly lunges forward, enveloping  ' + User_name + '  in its coiled body. With an eerie hiss, it commences a transformation, shapeshifting into an exact replica of  ' + User_name + ' . In a bizarre turn of events, the creature takes on the appearance and identity of  ' + User_name + ' , adopting their mannerisms and characteristics. As the real user begins to fade from existence, the replica starts to take over, seamlessly stepping into  ' + User_name + ' s life. Replaced ending')

    def Agree():
        print('As  ' + User_name + '  says "yes" to the snakes request, an eccentric transformation takes place. Suddenly,  ' + User_name + '  undergoes a complete metamorphosis, assuming the appearance and characteristics of the gnome. Clad in the typical gnome attire, the transformed  ' + User_name + '  waddles over to the dance floor. In the midst of the partys chaos,  ' + User_name + '  encounters their identical-looking gnome self, who gestures mysteriously, "Psst, follow me!" The two gnomes, equally baffled by each others presence, hurriedly exit to a hallway. Seizing the moment,  ' + User_name + '  leaps atop the other gnome and engulfs it with a comical flourish, leaving a puzzling scene for onlookers. Returning to the snake, the newly transformed  ' + User_name + '  engages in a peculiar conversation, with both parties exchanging quips and banter. Snake: "Well, well, well, look at you, little gnome! Mission successful?" Gnome- ' + User_name + ' : "You betcha! This whole shapeshifting business is a real gnome-brainer, huh?" Snake: "Ha! Quick and sneaky, just what I needed. Now, time for the next step." Gnome- ' + User_name + ' : "But wait, whats the deal with Mediterranean and her schemes? Whats next on the agenda?" Suddenly, the gnome- ' + User_name + '  is thrust back into the heart of the party, facing Mediterraneans cunning request. Now, a pivotal decision looms large: whether to aid Mediterranean in her grand plan or to sabotage her efforts.')
        SabatageOrHelp = input("Enter 1 to Help and 2 to Sabatage")
        if SabatageOrHelp == '1':
            Help()
        elif SabatageOrHelp == '2':
            Sabatage()
        else:
            print('Invalid choice. Try again.')        
            book()

    def Help():
        print('As the gnome- ' + User_name + '  agrees to assist Mediterranean, Mediterranean is ecstatic, greeting the gnome- ' + User_name + '  with a triumphant jig, exclaiming, "Ha! Youre on board! This will be epic!" Mediterranean shares her delightfully wicked plan, "Okay, listen, dear gnome: your mission is to bring all the party guests together in the ballroom, while I sneak off to this secret chamber and set the stage for the big ka-boom. When I get back, well rock this house with an unforgettable finale. Ready for action?" The gnome- ' + User_name + ' , channeling their inner gnome spirit, responds with an enthusiastic nod. They skip off to the ballroom, leaving a trail of little gnomish giggles in their wake, orchestrating the movement of guests as though it were a charming garden dance. Meanwhile, Mediterranean, in her devious delight, darts off to her secret chamber, cackling with wicked glee as she fine-tunes the detonation contraption, twisting knobs and pushing buttons with an air of melodramatic flair. In the ballroom, the gnome- ' + User_name + '  confidently directs the guests, encouraging them to take their places, even tossing a few silly gnome jokes to keep the atmosphere light. The creatures exchange whispers, perplexed but also oddly amused by the gnome- ' + User_name + ' s peculiar behavior. As Mediterranean finalizes her preparations for the big explosion, the gnome- ' + User_name + '  stands among the guests with an impish grin, giving thumbs-up to fellow creatures, maintaining an air of playful mischief. In the room of detonation, Mediterranean presses the button with a flourish, expecting the impending blast to signal her victory. The gnome runs out screaming and enjoys the show as the ballroom exploades and the gnome  ' + User_name + '  and Meteranean have won. Evil Ending')
        StartOver()

    def Sabatage():
        print('As the gnome-shaped  ' + User_name + '  nods in agreement, Mediterranean steps forward, offering a small, enigmatic smile. "Alright, little one. Here is what I need you to do," she explains, her tone cryptic yet decisive. "You stay back and ensure everyones captured while I leave to handle the detonation. Ill head to the special room to set things in motion. Well explode this place and end this once and for all." The gnome- ' + User_name + '  processes Mediterraneans plan, nodding silently in apparent agreement, promising to fulfill the assigned role as the plan unfolds. With a subtle, understanding nod, Mediterranean departs, confident in the gnomes unwavering compliance.  — As the gnome-shaped  ' + User_name + ' , with a peculiar gnomish accent, sets out to follow through with Mediterraneans plan, they begin ushering everyone out of the room. "Come on now, folks! Time to head out, the partys over!" the gnome- ' + User_name + '  announces cheerily, gesturing towards the exit. Several of the creatures in the room hesitate, murmuring amongst themselves, seemingly reluctant to leave. "But we were just getting started!" one of the monsters complains, voicing their objection to the abrupt end of the gathering. Another chimera-like entity, adorned with numerous eyes and tentacles, pipes up, "This isnt fair! We never get to have any fun!" Despite initial resistance, a wave of compliance eventually sweeps through the crowd as the gnome- ' + User_name + '  persists in their polite but firm request. The creatures, though discontented, eventually shuffle out, grumbling about the sudden conclusion of the festivities. With the last of the party guests leaving the room, the space is emptied, and the gnome- ' + User_name + '  remains behind, awaiting the final outcome. The clock is ticking, and the fate of the room is on the verge of a monumental shift. In the special room, Mediterranean triumphantly announced, "Behold, I have won! You are all about to meet your explosive end!" As she gloatingly approached the detonation button, a voice suddenly echoed throughout the room. "Sorry, but youve been bamboozled!" The room vibrated with  ' + User_name + ' s voice, catching everyone by surprise. With a slight delay, the room shook and quivered, and then it happened: the room containing Mediterranean exploded with a deafening boom. Shards of debris and clouds of dust flew into the air as the blast reverberated throughout the mansion. With a gnome-sized nod to the odd and unexpected turn of events, the world now embraced  ' + User_name + '  as a gnome. Though they were no longer a detective, their newfound celebrity status bloomed. In an unforeseen twist,  ' + User_name + '  found fame as a gnome movie star, landing roles in numerous films, including the ever-popular "Gnomeo and Juliet" and the classic "Sherlock Gnomes". Despite the sudden turn of fate and transformation into a gnome,  ' + User_name + '  discovered a life beyond the investigative world. Adored by many for their gnome-like charm, they found their place in the spotlight, bringing joy and laughter to audiences as a beloved gnome personality. And with that,  ' + User_name + ' s story concluded in a world of cinema, recognized as a superstar gnome with a tale that many would tell and retell for years to come. Happy Ever Gnome After ending ')
        StartOver()
    
    
    #Start the game
    start_game()

