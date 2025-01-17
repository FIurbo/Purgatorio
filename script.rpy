define s = Character()
define d = Character("Dante")
define cato = Character("Cato")
define virgil = Character("Virgil")
define souls = Character("The Souls")
define casella = Character("Casella")
define soulsunknown = Character("Unknown Soul")
define proudsouls = Character("The Souls of the Proud")
define manfred = Character("Manfred")
define copo = Character("Iacopo del Cassero")
define conte = Character("Buonconte of Montefeltro")
define pia = Character("Pia")
define sordello = Character("Sordello")
define nino = Character("Nino")
define corrado = Character("Corrado")
define guard = Character("The Guard of Purgatory")
define omberto = Character("Omberto")
define oderisi = Character("Oderisi")
define angel = Character("Angel")
define belacqua = Character("Belacqua")
$ centered = Character(None, xalign=0.5, yalign=2)
define autosaver = Character(None, xalign=1, yalign=0.2)
define gui.text_color = "#FFFFFF"
define gui.text_font = "SuperLegendBoy-4w8Y.ttf"
default _skipping = False
screen mapmaptutorial():
    imagemap:
        xalign 1.0
        yalign 0.15
        ground "minimap.png"
screen minimap():
    imagemap:
        xalign 1.0
        yalign 0.15
        ground "minimap.png"
        hotspot (2, 11, 90, 63) action Show("mapmap")
screen mapmap():
    imagemap:
        xalign 0.5
        yalign 0.5
        ground "mapmap.png"
        hotspot (1101, 39, 64, 55) action Hide("mapmap")
        hotspot (6, 19, 1089, 599) action Show("mapmap")

screen sevenp():
    image "sevenp.png":
        pos(940, 10)
screen sixp():
    image "sixp.png":
        pos(940, 10)
define box = Character(None,
                    what_size=20,
                    what_xalign=0.5,
                    window_xalign=0.5,
                    window_yalign=0.75,
                    what_text_align=0.5,
                    )
define pabtc = Character(None,
                    what_size=20,
                    what_xalign=0.5,
                    window_xalign=0.5,
                    window_yalign=1.3,
                    what_text_align=0.5,
                    )
screen start():
    image "background(1).jpg"
    text "{color=#000000}{size=+45}DANTES PURGATORIO{/font, /size, /color}":
        pos(100, 300)
screen autosave():
    text "{cps=5}{size=+5}Auto Saving...":
        pos(1010, 660)
screen savesave():
    $ renpy.save("1-1")
    text "{cps=5}{size=+5}Saving...":
        pos(1010, 660)
screen popup():
    image "popupdante.jpg" at truecenter
default timer = 10
default timerenabled = True # maybe a variable to track if the timer is currently active
default newtick = 0
init python:
    import time
    def timerdisplay(st, at):
        if store.newtick == 0:
            store.newtick = time.time() +1.0
        else:
            if store.newtick <= time.time(): # It's been more than 1 second, time for new tick
                if store.timerenabled:
                    if store.timer > 0:
                        store.timer = store.timer -1
                        store.newtick = time.time() +1.0 # set it to trigger a second from now
        return Text(str(store.timer)), 1.0 # Runs every second and returns timer as a text string
    def correctanswer():
        store.timer = max(0, store.timer - 50) # Subtract time from the counter. If it goes negative, just set it to 0
    def bigcorrectanswer():
        store.timer = max(0, store.timer - 70)
    def incorrectanswer():
        store.timer = max(0, store.timer + 50)
        return Text(str(store.timer)), 0.0 # Runs every frame and returns timer as a text string
screen countdown:
  text DynamicDisplayable(timerdisplay):
      align(0.5, 0.8)
label start:
    s "{cps=10}Easter Monday..."
    s "{cps=10}08:00 A.M. 1300 A.D."
    s "{cps=20}{outlinecolor=#000000}After a Long Trek{cps=3}...{p=3}"
    s "{cps=15}{outlinecolor=#000000}Through the tunnel from {color=#f00}{b}The Inferno{/color}{/b} You are blinded by the light...{p=3}"
    s "{outlinecolor=#000000}{cps=20}It is like nothing you have ever seen before..."
    s "{outlinecolor=#000000}{cps=20}You, accompanied by Virgil take your first steps out of the tunnel...{p=1}"
    s "{outlinecolor=#000000}{cps=20}And arrive at the base of the mountain of..."
    s "{color=#f00}{b}{size=+10}Purgatory.{/cps, /color, /b}"
    image canto_1_background = "dante.jpg"
    play music "musicforgame.mp3"
    show screen start
    with dissolve
    $ renpy.save("1-1")
    show screen autosave
    pabtc "{cps=15}{size=+30}{color=000000}Press any key to continue..."
    show screen popup
    hide screen autosave
    with dissolve
    box "{size=-2}{cps=10}{color=#FFA500}Note... {color=#000000}{cps=15}Dantes Purgatory is a text-based \n game in which different encounters will\nallow you to advance through the \nlevels of purgatory. If a question is \n answered wrong, the time you spend in that \n level of Purgatory will be reset."
    box "{size=+1}{color=#000000}The timer you see at \nthe bottom of your screen..."
    $ timer = 10
    show screen countdown
    box "{size=+1}{color=#000000}Indicates how much time must be\n spent in a specific part of the game"
    box "{size=+1}{color=#000000}Upon being prompted to advance futher\n if the timer is not zero\n then you must wait"
    hide screen countdown
    jump starting2
    box "{size=+1}{color=#000000}For a visual of where you are.."
    show screen mapmaptutorial
    box "{size=+1}{color=#000000}Feel free to click on the map\nicon in the top right"
    hide screen mapmaptutorial
label starting2:
    box "{size=+1}{color=#000000}Furthermore... the game will be broken up into three sections, ante-Purgatory (Canto I-IX), Purgatory-proper (Canto X-XXVI), the earthly-paradise (Canto XXVII-XXXIII)"
    box "{size=+2}{color=#000000}Space bar, or simply clicking/tapping\n the screen will allow \nyou to skim through dialogue faster."
    hide screen popup
    hide screen start
    with dissolve
    play music "gamemusic.mp3"
    centered "{size=+8}{cps=6}{b}{color=#FFF000}Ante-Purgatory (Canto I - IX){p=2}"
    with dissolve
    centered "{size=+8}{cps=6}{b}{color=#FF7F50}Arrival (Canto I-II){p=2}"
    with dissolve
label levelstart:
    show text "Canto: I \nTime: 5:00 A.M.":
        align(0.0, 0.0)
    $ timer = 100
    $ timerenabled = True
    show screen countdown
    box "At the base of the mountain you notice a man in the distance."
    box "The man's name is Cato, a pagan who has been placed by God as the general gatekeeper and guardian of the base of the mountain."
    cato "Who are you?"
    cato "{cps=25}Who guided you? Who served you as a lamp to light your way out of the heavy night that keeps the pit of Hell forever black?"
menu:
     "Talk to the stubborn gatekeeper?"

     "Yes":
         virgil "{cps=20}Not on my behalf have I come here. A lady sent from Heaven asked me to guide Dante along his way."

     "No":
         "It is probably best you talk to him:)"
         menu:
             "{cps=25}Talk to the stubborn gatekeeper?"

             "Yes":
                 virgil "{cps=20}Not on my behalf have I come here. A lady sent from Heaven asked me to guide Dante along his way."

label after_menu:
    virgil "{cps=25}This is a man of flesh, who is still of body and soul..."
    virgil "A lady from heaven sent me to guide this man up the mountain"
    virgil "{cps=25}Now knowing the circumstances, will you let us pass?"
    cato "{cps=25}You may pass so long as you WASH THE STAIN OF HELL FROM THE MAN and wrap a reed around him."
    "{cps=40}Cato gives instructions on how to scale the mountain and then disappears."
menu:
    "Have Virgil pick the reed and wash your face as Cato commanded?"

    "Pick the reed?":
        "{cps=40}Virgil washes your face, picks the reed and an identical one sprouts up and takes its place."
    "Refuse to listen to instructions.":
        $ incorrectanswer()
        "It is best you do as Cato commands:), {color=#FFF000}50 seconds has been added to your time."
        with dissolve
        menu:
            "Have Virgil pick the reed and wash your face as Cato commanded?"

            "Pick the reed?":
                "{cps=40}Virgil washes your face, picks the reed and an identical one sprouts up and takes its place."

label after_menu1:
    hide text "Canto: I \nTime: 5:00 A.M."
    show text "Canto: II \nTime: 6:00 A.M.":
        align(0.0, 0.0)
    with dissolve
    "You and Virgil are at a standstill at the base of the mountain."
    "Suddenly a bright light comes towards you and is moving extremely quickly..."
    "Virgil commands you to kneel."
    "You find that the bright light is an angel, guiding a boat of souls all singing a pslam in unison."
    "The angel arrives at the shore, makes the sign of the cross and leaves."
    "The souls approach you."
    "They look confused and ask for directions."
    souls "If you should know the road that leads up the mountainside, then show us."
    virgil "You seem to think that we are souls familiar with this place but we, like all of you, are pilgrims here."
    "The souls notice you are a real person and begin to crowd you."
    souls "One soul steps forward and greets you."
    "You attempt to embrace the soul and are unable to do so."
    souls "The shade begins to speak..."
    "And by his voice I knew who this shade was. I begged him to stay and speak to me for a while."
    "It was Casella!"
    casella "Of course I'll stay, but tell me why you're here?"
    d "I make this journey now, Oh, my Casella, hoping one day to come back here again."
    "Casella has died many moons ago.  How is he just now arriving you think to youself."
    d "How did you lose so much time?"
    casella "Casella explains that there is a delay from death to arriving at purgatory."
    "You ask Casella to sing you a song."
    play music "Amor.mp3"
    casella "Casella begins to sing Amor Che Ne La Mente Mi Ragion{p=30}"
    souls "The souls are fascinated as to what was happening."
    "In the midst of the commotion, Cato reappears.."
    stop music
    play music "scratch.mp3" noloop
    cato "WHAT IS THIS YOU LAZY SOULS?"
    cato "MOVE ALONG!"
    hide text "Canto: II \nTime: 6:00 A.M."
    centered "{size=+8}{cps=6}{b}{color=#FF7F50}The Excommunicated(Canto III - IV){p=2}"
    show text "Canto: III \nTime: 7:00 A.M.\nSins: Excommunicated":
        align(0.0, 0.0)
    "You and Virgil move along, splitting from the pack of souls."
    "As you and Virgil move towards the foot of the mountain, Virgil explains that souls in the afterlife can experience physical feelings, even without the body."
    "You and Virgil arrive at the foot of the mountain which is extremely steep."
    "Virgil considers which way will be best for the ascent."
    play music "gamemusic.mp3"
    "While Virgil is thinking, you notice another group of souls moving towards you..."
    "The crowd approaches you."
    virgil "Could someone tell me where this mountain might slope enough to allow us to start our climb?"
    souls "The souls stood quiet."
    souls "Suddenly one soul steps out and begins to speak to you."
    soulsunknown "Do you recognise me?"
    d "I am afraid I do not. Tell me. Who are you?"
    manfred "Manfred, I am, Grandson of Empress Constance."
    "Manfred shows you a fatal wound on his head and explains he sustained the injury after he was excommunicated.{p=5}"
    "Manfred also explains that the group of souls were the excommunicated."

$ choice1 = False
$ choice2 = False
$ choice3 = False

label start2:
    menu:
        "What was Manfred's Injury?"

        "An injury to his leg." if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice1 = True
            jump start2
        "An injury to his head.":
            jump nextpimp
        "An injury to his eye." if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice2 = True
            jump start2
        "An injury to his stomach." if not choice3:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice3 = True
            jump start2
label nextpimp:
    "The group of souls begin to move, and You along with Virgil follow them."
    "You soon find yourself at a narrow passage where you and Virgil pass through and begin your climb."
menu:
    "Begin Climb?"

    "Yes?":
        while timer > 0:
            "You have not spent enough time in this level..."
        hide screen countdown
label correct:
    $ timer = 330
    hide text "Canto: III \nTime: 7:00 A.M.\nSins: Excommunicated"
    centered  "{size=+8}{cps=6}{b}{color=#FF7F50}The Late-Repentant (Canto IV - IX){p=2}"
    show text "Canto: IV \nTime: 9:30 A.M.\nSins: Late-Repentant":
        align(0.0, 0.0)
    show screen countdown
    "The climb is no easy task"
    "You soon find it very hard to keep up with Virgil"
    "You and Virgil finally reach a ledge as the sun starts to rise."
    "As the sun rises you notice it is in the west rather than the east."
    "Virgil explains that this is because of the relationship between the mount of purgatory and Jerusalem"
    "As you and Virgil are talking you notice a group of souls sitting on a boulder nearby."
$ choice1 = False
$ choice2 = False
$ choice3 = False
label start3:
    menu:
        "Where does the sun rise in purgatory?"

        "North" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice1 = True
            jump start3
        "South" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice2 = True
            jump start3
        "West":
            jump nextpimp2
        "East" if not choice3:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice3 = True
            jump start3
label nextpimp2:
    "You approach them and start to speak to one of them."
    "An old friend of yours!"
    d "Balecqua!"
    d "Oh, how relieved I am to know your fate!"
    d "But tell me why are you just sitting like this? Are you waiting for a guide or simply being your old self again?"
    belacqua "Brother, what good will climbing do? God's angel sitting at the gate will not let me begin my repentance inside."
    belacqua "Before I start, the heavens must revolve as many times as I was alive, for I put off repenting 'til the end."
    belacqua "Prayers could, of course, make my time shorter here, prayers from a heart that lives in grace."
    belacqua "The rest are worthless, for they go unheard in Heaven!"
    "Virgil interrupts and urges you to move along."
    hide text "Canto: IV \nTime: 9:30 A.M.\nSins: Late-Repentant"
    show text "Canto: V \nTime: 11:00 A.M.\nSins: Late-Repentant\n Description: Killed Violently":
        align(0.0, 0.0)
    souls "Some of the souls from Belacqua's group notice that your body does not allow light to pass through it."
    souls "Look! One of the men climbing has no light shining through!"
    souls "He seems to walk as if he were alive!"
    "You pause to see what they're talking about..."
    virgil "What could you possibly be stopping for now?"
    d "The souls are gossiping about my shadow."
    virgil "So what? Let them talk.  Keep moving!"
    "As you continue to climb another group of souls walks toward you."
    play music "misere.mp3"
    souls "The souls are singing {i}Miserere{/i}"
    "Virgil explains these shades were killed {color=#FF0000}violently{/color} and they repented in the last moments of their lives."
    souls "Again... The souls notice you cast a shadow."
    souls "With an intrigued demeanor, the group sends two messengers in your direction."
    virgil "Report back to your group that this is a man of true flesh and blood."
    souls "The messengers chat amongst the group."
    souls "The group starts moving towards you."
    virgil "Oh, look at all those souls pressing toward us. \n Each one will have his plea.  Listen to them, but move on as you do."
    "You and Virgil continue to move..."
    souls "The souls urge you to stop."
    souls "Oh, wait! Where are you going? Oh, please stop!"
    souls "We are all the souls who met a violent death, but we found God's grace upon death."
    d "I see your faces, but cannot recognize one..."
    souls "One soul steps forward to have his plea.."
    copo "I beg you to ask the people of my town, Fano, to send prayers to me!"
    copo "The man explained he was ambushed, struck, and left to bleed to death in a swamp."
    souls "Another soul interrupts and Iacopo yields the floor."
    conte "I hope your desire to climb the mountain is fulfilled and I beg that you help satisfy my desire."
    conte "I am Buonconte. No one cares for me so I walk with shame among these souls."
    d "How was it that you died and no one found your body?"
    conte "He explains that he was struggling between choosing good or evil.."
    conte "And at his final breath he uttered Mary's name and wept a tear of true repentance."
    conte "His soul was saved but his body was possessed by a demon and his remains were sent down the river channels."
    souls "After Buonconte was finished, a girl steps forward."
    pia "I am La Pia.  All I ask is for you to remember me."
$ choice1 = False
$ choice2 = False
$ choice3 = False
label start4:
    menu:
        "Which of the three was possessed by a demon?"

        "Iacopo del Cassero" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice1 = True
            jump start4
        "Pia" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice2 = True
            jump start4
        "Buonconte of Montefeltro":
            jump start15
$ choice1 = False
$ choice2 = False
$ choice3 = False

label start15:
    menu:
        "What did Belacqua say would shorten time in ante-Purgatory?"

        "Indulgences" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice1 = True
            jump start15
        "Prayers from the living":
            jump nextpimp3
        "True repentance" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice2 = True
            jump start15
label nextpimp3:
    hide text "Canto: V \nTime: 11:00 A.M.\nSins: Late-Repentant\n Description: Killed Violently"
    show text "Canto: VI \nTime: 3:00 P.M.\nSins: Late-Repentant\n Description: Killed Violently":
        align(0.0, 0.0)
    souls "More and more souls from the group continue to crowd around you."
    "Three of which you recognize."
    "You ask Virgil why these souls beg of you to pray for them..."
    virgil "She will explain later. She is the light between truth and intelligence."
    "You start to acknowledge the souls, but Virgil interrupts."
    virgil "We must keep moving."
    "You and Virgil continue to move."
    "Whilst trekking you and Virgil notice a figure in the distance."
    "Virgil approaches the shade who is sitting."
    virgil "Tell me, where might be the best place to scale this mountain?"
    soulsunknown "...{p=4}"
    soulsunknown "And where might you be from?"
    virgil "Mantuan, and my friend --"
    soulsunknown "The man springs to his feet to embrace Virgil."
    sordello "Oh, Mantuan, I am Sordello. I am from your town!"
    "The two embrace each other."
    "As you two embrace each other, you reminisce about the corruption, war, and state of Italy."
label start7:
    hide text "Canto: VI \nTime: 3:00 P.M.\nSins: Late-Repentant\n Description: Killed Violently"
    show text "Canto: VII \nTime: 5:00 P.M.\nSins: Late-Repentant\n Description: The Negligent Rulers":
        align(0.0, 0.0)
    sordello "Tell me who you are!"
    virgil "I am Virgil!"
    sordello "It is! It cannot be!"
    "Sordello bows his head as if he was speaking to royalty."
    sordello "You bring immense glory to the Latin race!"
    sordello "How are you able to be here? Are you from hell? If so, what area?"
    show text "{cps=20}Virgil explains a place in hell called 'Limbo' where infants and virtuous pagans reside."
    virgil "I am from a place where infant souls are sent, not because of what they did, but because they were not washed of orginal sin."
    virgil "I reside there not because of what I did, but because of what I did not do..."
    hide text "{cps=20}Virgil explains a place in hell called 'Limbo' where infants and virtuous pagans reside"
    show text "Canto: VII \nTime: 5:00 P.M.\nSins: Late-Repentant\n Description: The Negligent Rulers":
        align(0.0, 0.0)
    virgil "But tell me, do you know the way up the mountain?"
    sordello "I am not confined to one spot.  Allow me to be your guide!"
    sordello "But note, night is falling upon us.  We may not scale any further."
    sordello "We best find a place to rest..."
    jump menu6

label sordello2:
    d "Wait, Sordello! Won't you tell me how it all works?"
    sordello "Sure! At night a soul cannot scale the mountain..."
    "Sordello draws a line in the dirt with his finger."
    sordello "After sun sets, you could not go beyond this line even if you wanted to."
    sordello "Nothing prevents you from going up except the darkness of the shadows..."
    sordello "This alone will make a man impotent."
    sordello "This is because without the light of God, we may not make it to paradise."
    d "Thank you!"
    jump menu7
label menu6:
    show text "No wrong answer.":
        align(0.5, 0.0)
    menu:
        "Ask Sordello how night works in purgatory?"

        "Sure!":
            jump sordello2
            hide text

        "I would like to keep moving.":
            jump menu7
            hide text
label menu7:
    hide text "No wrong answer."
    virgil "Where might we find the place of satisfying rest?"
    sordello "Off to the right here is a group of souls. let me take you there. I believe you will find pleasure in meeting them."
    "We started on our way and soon we found a valley on the mountain's slope. This was the Valley of the Princes, filled with negligent rulers..."
    "As soon as we get to the rim of the valley, Virgil in a tiresome manner finds a spot on the mountain side and makes himself comfy."
    "Sordello and I peek over the side looking into the valley."
    "I glance back at Virgil."
    virgil "Do not even think about asking me to lead you down there where you can meet all the souls you please until morning."
    "Virgil seemed very tired..."
    play music "salve.mp3"
    "I look back over the ledge and hear the group of souls singing {i}Salve Regina{/i}"
    "From this overpass I found it much easier to see the faces of the shades"
    sordello "Look, the one not joining in psalm is Rudolph, Emperor, who could have saved the battle scars of Italy"
    sordello "The one comforting Rudolph once ruled Bohemia..."
    "Sordello goes on naming the different rulers that reside in the Valley..."
$ choice1 = False
$ choice2 = False
$ choice3 = False
label start6:
    menu:
        "What does Sordello say keeps you from travling at night?"


        "At night, God's light is not guiding you.":
            jump nextpimp5
        "Night is reserved for Heavenly traffic only, travling souls may interrupt this." if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice1 = True
            jump start6
        "At night, increases the slope of the mountain, rendering it impossible for souls to ascend." if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice2 = True
            jump start6

label nextpimp5:
    hide text "Canto: VII \nTime: 5:00 P.M.\nSins: Late-Repentant\n Description: The Negligent Rulers"
    show text "Canto: VIII \nTime: 6:00-7:00 P.M.\nSins: Late-Repentant\n Description: The Negligent Rulers":
        align(0.0, 0.0)
    menu:
        "Continue?"

        "Yes?":
            while timer > 0:
                "You have not spent enough time here..."
            hide screen countdown
    $ timer = 200
    show screen countdown
    play music "lucis.mp3"
    "As you and Sordello peek over the edge, one soul steps away from the group and starts singing {i}Te lucis ante{/i}"
    "The rest join in..."
    "{p=10}..."
    "The souls look up to the heavens."
    play music "battlemusic.mp3"
    "Two angels wielding {color=#FF0000}Flaming Swords{/color} wearing green garments."
    "One of the angels took his stand on our side of the valley and the other on the opposite side."
    sordello "They have come from heaven to defend us from the serpent in the vail..."
    sordello "He will be here soon."
    "Fearfully, I drew closer Virgil who woke from the commotion."
    sordello "It is time we all joined the group of souls at the bottom. They will be pleased to speak with you, Dante."
    "When I reached the bottom a shade studied my face."
    "We both paced towards each other."
    d "Noble Judge Nino, oh how pleased I am to see you are not damned!"
    "Nino did not seem to be interested in my sentiment."
    nino "How long ago was it that you arrived to the mountain of purgatory?"
    d "Oh"
    d "{p=2}..."
    d "I left the pit of hell this morning, I am not dead either. I hope to gain eternal life by the road I take."
    "Sordello and Nino backed away and were shocked at what they heard.."
    "Nino cries to his friend.."
    nino "Corrado! Come quick! see what God's grace has willed!"
    "Corrado is now listening in on your conversation with Nino"
    nino "Oh, please! I beg of you please! tell my daughter Giovanna to pray for me!"
    nino "I think her mother has stopped loving me!"
    "My mind wandered as Nino talked. I couldn't help but notice what was going on in the sky."
    virgil "What are you staring at?"
    d "The brilliant torches lighting the polar region here!"
    "But just as Virgil spoke Sordello interrupted"
    sordello "Look! Just over there!"
    "He pointed at the valley's little open side, where a serpent moved."
    "Perhaps he was the one who offered Eve the bitter fruit to eat."
    "The two angels took flight!"
    "and upon hearing their wings slice through the air, the serpent fled."
    "{p=3}..."
    "The shade Nino called earlier asks to have a word with you."
    corrado "Do you bear any recent news about the kingdom {color=#ff0d00}Val di Magra{/color}. I once ruled that land."
    d "Oh, I have never visited the lands you ruled, though the whole of Europe has heard about your glorious domain."
    "Corrado goes on to spew that soon, you will be exiled from Florence..."
$ choice1 = False
$ choice2 = False
$ choice3 = False
label start8:
    menu:
        "What kingdom did Corrado rule?"

        "Florenca" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice1 = True
            jump start8
        "Val di Magra":
            jump nextpimp4
        "Termine de Epueta" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time.."
            with dissolve
            $ choice2 = True
            jump start8
    hide text "Canto: VIII \nTime: 6:00-7:00 P.M.\nSins: Late-Repentant\n Description: The Negligent Rulers"
label nextpimp4:
    show text "Canto: IX \nTime: 8:00-9:00 P.M.\nDescription: The Ascent to the Gate":
        align(0.0, 0.0)
    "After your chat with Corrado, you grow tiresome"
    "You doze off..."
    "An eagle!"
    "It swoops down and carries me in a ball of {color=#FF0000}fire"
    "I wake..."
    "The imaginary heat from my dream launches me back to reality."
    hide text "Canto: IX \nTime: 8:00-9:00 P.M.\nDescription: The Ascent to the Gate"
    show text "Canto: IX \nTime: 6:00 A.M. Monday\nDescription: The Ascent to the Gate":
        align(0.0, 0.0)
    "I am terrified, but find that my Comfort, Virgil, is not far..."
    virgil "You must not be afraid, for we are well on our way..."
    virgil "You have arrived at the gates of Purgatory now."
    virgil "While you were asleep, a lady came..."
    virgil "The lady said 'I am Lucia, let me take this man who lies asleep, I want to speed his journey.' Sordello and the other shades stayed behind..."
    "Close to the top, you reach a point from where you see somewhat of a gate, although it appeared as just a mere gap upon the wall."
    "..."
    "leading up to it, there were three steps, each one a different color and you see the silent figure of someone on guard."
    "On the highest step stood the guard"
    "In his hand he holds a naked sword, so bright that each time you try to look you are blinded."
    guard "Speak up from where you are. What is it that you want? Where is your guide? Beware, you may regret your coming here."
    virgil "A lady from heaven sent us, she led us to your gate."
    guard "May she continue guiding you to good, and so, come forward now up to our stairs."
    "And so you climb the steps"
    "White marble was first, so polished I could see my own reflection."
    "The second one was the darkest purple you have ever seen, made of rough and crumbling, fire-corroded stone, with cracks across its surface"
    "The third one, lying heavy at the top, appeared to be of flaming porphyry, red as the blood that spurts out from a vein"
    "upon this step the angel of the Lord rested his feet, he sat upon the sill which seemed to be of adamantine rock"
    "And with his sword he scarred your forehead with seven P's"
    show screen sevenp
    guard "Make sure that as you move through Purgatory, you wash the blemishes away."
    "The angel had two keys, silver and gold."
    "He inserted the silver key, then the gold."
    guard "Enter"
    menu:
        "Continue?"

        "Yes":
            while timer > 0:
                "You have not spent enough time here."
            hide screen countdown
    "As we started to enter the Guard had one last thought."
    guard "{b}but first be warned, to look back means to go back out again."
    play music "endcredit.mp3"
    show image "endpic.jpg"
    show screen popup
    with dissolve
    define correct2 = True
    menu:
        centered "{color=#000000}Would you like to \ncontinue to the first terrace?"

        "No, main menu":
            "{color=#000000}Thank you for playing,\n more levels in the future to come..."
            return
        "Yes":
            "Enjoy..."
            jump sneakpeak
label sneakpeak:
    hide screen countdown
    stop music
    hide image "endpic.jpg"
    hide screen popup
    with dissolve
    show screen popup
    centered "{color=#000000}In purgatory proper, answering \n questions correctly\n will remove time from the timer."
    hide screen popup
    centered "{size=+8}{cps=6}{b}{color=#FF7F50}Purgatory-proper{p=2}"
    centered "{size=+8}{cps=6}{b}{color=#FFF000}Terrace 1, {color=#805b87}Pride{p=2}"
    show text "Canto: X \nTime: 9:30 A.M. \nSins: {color=#805b87}The Prideful":
        align(0.0, 0.0)
    $ timer = 500
    show screen countdown
    "You and Virgil pass through the threshold of the gate..."
    play music "gateshutting.mp3" noloop
    "The gate closes behind you"
    $ renpy.pause(delay = 5.0, hard = True)
    "You fight the urge to look back, keeping in mind what the gate keeper had told you..."
    "You and your guide carry on..."
    "You climb through a narrow cleft..."
    $ renpy.save("1-1")
    show screen autosave
    virgil "Now, we are at the point where we must use our wits: when the path bends, we keep close to the far side of the curve."
    hide screen autosave
    "Your steps grow smaller"
    "You finally squeeze through the needle's eye."
    "From the opening laid a path alongside the mount, wide enough to form a ledge."
    "Both you and Virgil grow tired and have no sense of direction up the mount."
    "You peer ahead and notice that the side of the mount is no longer climbable."
    "Instead it was pure white marble with various carvings."
    "These carvings are the opposite virtue of {color=#805b87}Pride."
    "These are examples of Humility."
    "Mother Mary was there in the closest carving."
    "It depicted the scene of the annunciation..."
    "Where Mary put aside everything and said yes to the will of God."
    "You gaze upon it in awe."
    "The outlines of her image carved the words {i}Ecce ancilla Dei{/i} clearly cut into the stone."
    virgil "Why don't you take a look at the other parts as well?"
    "You take one final look at the statue then see Virgil standing where he prompted you to go."
    "You quickly catch up to him..."
    "More stories carved in the wall."
    "The next carving depicted David, who set aside his kingly duties to serve the Lord."
    "After that was the story of a great Trajan Emperor.."
    "Who halted his entire army just to hear a plea of grief from a widowed woman."
    "As you marvel at these great carvings Virgil interrupts.."
    virgil "Look ahead, a group of souls approach us..."
    virgil "They might be able to give us directions."
    "You notice that the group of shades have something off about them."
    d "Master, those --"
    d "Those things dont appear to be shades at all."
    d "My sight confuses me..."
    virgil "The grevious nature of their punishment bends their bodies to the ground."
    "Upon the souls' backs lay large slabs of stones.."
    "Some larger, some smaller..."
    "Each putting more or less weight on each one's back."
default incorrectans = False
$ choice1 = False
$ choice2 = False
$ choice3 = False
$ incorrectans = False
label start9:
    menu:
        "What is the Opposite Virtue of Pride."

        "Chastity" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice1 = True
            $ incorrectans = True
            jump start9
        "Humility":
            if incorrectans == True:
                jump nextpimp6
            else:
                $ correctanswer()
                "Correct! {color=#FFF000}50 seconds has been subtracted from your time!"
                jump nextpimp6
        "Charity" if not choice3:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice3 = True
            $ incorrectans = True
            jump start9
        "Diligence" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice2 = True
            $ incorrectans = True
            jump start9
label nextpimp6:

    hide text "Canto: X \nTime: 9:30 A.M. \nSins: {color=#805b87}The Prideful"
    show text "Canto: XI \nTime: 10:00 A.M. \nSins: {color=#805b87}The Prideful":
        align(0.0, 0.0)
    play music "battlemusic.mp3"
    "Virgil approaches a member of the group."
    virgil "Might you be able to help us find a way up this mountain?"
    virgil "The man I am with bares flesh and blood, rendering our climbing slow."
    proudsouls "Follow this bank along the right with us, and you will find the road that you can surely climb."
    soulsunknown "If I was not bound to this stone that keeps my head facing the ground, perhaps I could look at your face and know who you are..."
    soulsunknown "My father was a great Tuscan..."
    omberto "I am Omberto, the sin of {color=#805b87}Pride{/color} ruined not only me, but my whole family..."
    omberto "I must carry this weight, which I refused to carry when I was alive, until God is satisfied."
    "You are crouching down in order to hear the man speak.."
    "Another shade speaks out and knows you..."
    "You turn your attention towards the familliar shade."
    jump menu8
label sordello5:
    d "You must be Oderisi of Gubbio, the famous painter, whose art the men in Paris call 'Illuminating'"
    oderisi "the work of Franco Bolognese is far better than the likes of mine..."
    "Oderisi goes on to exclaim the utter insignificance of human accomplishments..."
    "For nothing is compared to the accomplishment of eternal life."
    "Oderisi makes an example of one of the souls..."
    oderisi "You see that souls ahead?"
    oderisi "All of Tuscany resented his name."
    oderisi "Now, not even his own people remember him..."
    oderisi "He was once a proud man, now he is as corrupt as a whore."
    oderisi "Your fame on earth is like the grass, He who makes it grow will make it fade again."
    d "Your words have moved me, Oderisi."
    d "But tell me who is the man you spoke of?"
    oderisi "He is Provenzan Salvani."
    oderisi "He is here because he sought to gain control of all of Siena"
    oderisi "So he crawls on, and has crawled since he died, knowing no rest. And such coin is paid here by those who were presumptuous down there."
    d "If this is true, and he repented in the last moments of his life, then how did he get through Ante-Purgatory so fast?"
    oderisi "While at the apex of his glory, in Siena's marketplace, of his free will"
    oderisi "putting aside all shame, he took his stand"
    oderisi "and there, to ransom from his suffering"
    oderisi "a friend who was immured in Charles's jail, brought himself to do what chilled his veins!"
    oderisi "This confusion, my friend, will be explained later... until now, know that this is why Provenzan Salvani was sped here."
    jump menu9
label menu8:
    show text "It is encouraged to talk to as\n many people as possible in purgatory":
        align(0.5, 0.0)
    menu:
        "Listen to your old friend?"

        "Yes":
            jump sordello5
            hide text "It is encouraged to talk to as many people as possible in purgatory"

        "I would like to keep moving. I am an expert.":
            jump menu9
            hide text "It is encouraged to talk to as many people as possible in purgatory"
label menu9:
    hide text "Canto: XI \nTime: 10:00 A.M. \nSins: {color=#805b87}The Prideful"
    show text "Canto: XII \nTime: 11:00 A.M. \nSins: {color=#805b87}The Prideful":
        align(0.0, 0.0)
    "Once Oderisi was finished his stories.."
    "You and Virgil continue to move"
    "You move, happily following Virgil, both of you showing how light of feet you have become"
    virgil "Now look down..."
    virgil "You will be pleased, and it will make your journey easier, to see this bed of stone beneath your feet."
    "Beneath my feet were the carvings of a dead man's life preserved in the stone."
    "On the stone are examples of the vice of {color=#805b87}Pride"
    "These stones depicted carvings of Satan"
    "Next came Briareus, pierced by a thurnderbolt, frozen in death"
    "After came Thymbraeus, looking down on a scene of severed giants"
    "Next was the mighty Nimrod, gazing upon the construction of the Tower of Babel"
    "Next Niobe, then Saul, then Arachne, and so on and so fourth"
$ incorrectans = False
$ choice1 = False
$ choice2 = False
$ choice3 = False
$ incorrectans = False
label start11:
    menu:
        "Who was Oderisi making an example of?"

        "Provenzan Salvani" if not choice1:
            if incorrectans == True:
                jump start10
            else:
                $ correctanswer()
                "Correct! {color=#FFF000}50 seconds has been subtracted from your time!"
                jump start10
        "Gennaro Pontarelli" if not choice3:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice3 = True
            $ incorrectans = True
            jump start11
        "Tiziano Nalbone":
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice1 = True
            $ incorrectans = True
            jump start11
        "Duccio Nardini" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice2 = True
            $ incorrectans = True
            jump start11
$ incorrectans = False
$ choice1 = False
$ choice2 = False
$ choice3 = False
$ incorrectans = False
label start10:
    menu:
        "What was Oderisi known for?"

        "A famous inventor" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice1 = True
            $ incorrectans = True
            jump start10
        "A famous sculpter" if not choice3:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice3 = True
            $ incorrectans = True
            jump start10
        "A famous painter":
            if incorrectans == True:
                jump start12
            else:
                $ bigcorrectanswer()
                "Correct! {color=#FFF000}70 seconds has been subtracted from your time!"
                jump start12
        "A famous carpenter" if not choice2:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice2 = True
            $ incorrectans = True
            jump start10
$ incorrectans = False
$ choice1 = False
$ choice2 = False
$ choice3 = False
$ incorrectans = False
label start12:
    menu:
        "What were the carvings below your feet depictions of?"


        "The Vice of Pride":
            if incorrectans == True:
                jump nextpimp7
            else:
                $ bigcorrectanswer()
                "Correct! {color=#FFF000}70 seconds has been subtracted from your time!"
                jump nextpimp7
        "The Virtue of Pride" if not choice1:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice1 = True
            $ incorrectans = True
            jump start12
        "The Marian Example of Pride" if not choice3:
            $ incorrectanswer()
            "Incorrect, {color=#FFF000}50 seconds has been added to your time."
            with dissolve
            $ choice3 = True
            $ incorrectans = True
            jump start12
label nextpimp7:
    virgil "Raise your head now, you have spent enough time lost in your thoughts"
    virgil "Look over there, the angel comes!"
    virgil "Fix yourself! Show reverence!"
    stop music fadeout 2.0
    "You fix your posture"
    play music "wings.mp3" noloop
    "Clothed in white, the angel descended upon us..."
    $ renpy.pause(delay = 6.0, hard = True)
    angel "Come, now the steps are very close, the climb will soon be much easier"
    "The angel then rubbed his wing against my head"
    "Assuring me a safe ascent"
    play music "woosh.mp3" noloop
    hide screen sevenp
    show screen sixp
    with dissolve
    "And with that your first P was removed"
    "The angel led us straight to an opening amongst the rocks"
    "The steepness of the ascent was made easy with steps"
    menu:
        "Continue on..."

        "Yes?":
            while timer > 0:
                "You must wait to continue"
            hide screen countdown
    play music "beati.mp3"
    "While you are walking toward those steps, the song {i}Beati pauperes spiritu!{/i} rang out"
    "You begin your ascent to the second terrace..."
    "And as you are walking up the steps you feel incredibly lighter"
    d "Master! tell me, what heavy thing has been removed from me?"
    d "I feel as if to keep on climbing would be effortless"
    virgil "When the P's that still remain on your brow shall be erased completely like the first..."
    virgil "then will your feet be light with good desire, they will no longer feel the heavy road but will rejoice as they are urged to climb."
    "So you do what any man might do... you try and feel the marks on your forehead"
    "Virgil sees this and smiles"
    hide screen countdown
    play music "endcredit.mp3"
    show image "white.jpg"
    with dissolve
    centered "{cps=4}{size=+60}{color=#000000}To be continued..."
    centered "{cps=8}{size=+40}{color=#000000}Produced by\nCharles McKinney, DeMatha Class of 2022"
return





label second_beginning:
    # Game Introduction
   

    narrator "Welcome to the story of Dante's ascent through Purgatory, as envisioned in Chapters XIII through XXI of the '{color=#FF0000}Purgatorio{/color}'."
    narrator "You will journey alongside Dante and Virgil, observing their encounters and reflecting on the lessons they reveal."

    jump canto_13

label canto_13:
    # Canto 13: The Envious
    show text "Canto: XIII \n{color=#FF0000}The Envious{/color}":
        align(0.5, 0.25)

  

    narrator "Dante and Virgil stepped into the second terrace of Purgatory, a dim, oppressive space filled with shadowy forms."
    narrator "Here, the envious souls were clothed in coarse garments, their eyes cruelly sewn shut with iron wire—a punishment that mirrored their inability to see the good in others during their lives."
    narrator "The air was heavy with the sound of their chants, each voice lifting examples of generosity to counter their own failings."

    narrator "Virgil turned to Dante, explaining the symbolism of their blindness. 'Envy clouds the soul, preventing it from seeing the light of virtue and joy in others.'"

    narrator "He began to understand the destructive nature of envy and the necessity of celebrating others' successes."
    narrator "The chants resonated deeply, and Dante reflected on the power of generosity to heal the wounds of envy."

    jump canto_14

label canto_14:
    # Canto 14: Examples of Envy
    hide text "Canto: XIII \nThe Envious"
    show text "Canto: XIV \n{color=#FF0000}Examples of Envy{/color}":
        align(0.5, 0.25)


  

    narrator "As they ascended, the voices of the envious grew fainter, replaced by the murmurs of two souls nearby."
    narrator "The pair spoke of their lives, lamenting how envy had poisoned their relationships and blinded them to the blessings they had been given."

    narrator "One soul, pale and shadowy, turned to Dante. 'We envied the fortunes of others so fiercely that we could not see our own gifts. Now, we sing of generosity to cleanse our hearts.'"

    narrator "Their stories of regret and newfound hope deepened Dante's understanding of envy and its cure."
    narrator "Watching the souls, Dante saw the profound sorrow etched into their forms and the potential for redemption through humility."

    jump canto_15

label canto_15:
    # Canto 15: The Third Terrace - Wrath
    hide text "Canto: XIV \nExamples of Envy"
    show text "Canto: XV \n{color=#FF0000}Terrace of Wrath{/color}":
        align(0.5, 0.25)

    

    narrator "The third terrace loomed ahead, shrouded in a thick, choking smoke that veiled everything in darkness."
    narrator "Dante clung to Virgil as they navigated the blinding haze, hearing cries of anguish from the wrathful."
    narrator "These souls, consumed by anger in life, were now enveloped in smoke that mirrored the blinding nature of wrath."

    narrator "Amid the smoke, examples of meekness shone through in voices that recounted tales of forgiveness and peace, offering a stark contrast to the torment around them."

    narrator "He recalled moments of forgiveness he had witnessed and felt a deep sense of peace settle in his heart."
    narrator "The struggle through darkness tested Dante's patience, teaching him to endure adversity with grace."

    jump canto_16

label canto_16:
    # Canto 16: Free Will and Moral Responsibility
    hide text "Canto: XV \nTerrace of Wrath"
    show text "Canto: XVI \n{color=#FF0000}Free Will and Moral Responsibility{/color}":
        align(0.5, 0.25)


    narrator "Emerging from the smoke, Dante found himself on a quieter path, bathed in the soft glow of twilight."
    narrator "Virgil began to speak of free will, explaining how every soul has the power to choose their path, shaping their destiny through their actions."
    narrator "'It is not the stars that determine our fate,' Virgil said, 'but the choices we make with the gift of free will.'"

    narrator "Their conversation illuminated the delicate balance between divine guidance and human freedom."
    narrator "He considered how his own choices had led him to this journey, and the responsibility he bore for his future."

    jump canto_17

label canto_17:
    # Canto 17: The Nature of Love
    hide text "Canto: XVI \nFree Will and Moral Responsibility"
    show text "Canto: XVII \n{color=#FF0000}The Nature of Love{/color}":
        align(0.5, 0.25)



    narrator "Reaching the summit of the terrace, Virgil spoke of the force that drives all human actions: love."
    narrator "'Love, whether directed rightly or wrongly, is the root of every deed,' he explained. 'Misguided love leads to sin, while pure love elevates the soul.'"

    narrator "Dante listened intently, contemplating the complexities of love and its impact on human lives."

    narrator "Virgil explained how distorted love could lead to greed, envy, and wrath, offering examples that deepened Dante's understanding."
    narrator "He felt a growing connection to the divine, inspired by the idea of love as a guiding light."

    jump canto_18

label canto_18:
    # Canto 18: The Slothful
    hide text "Canto: XVII \nThe Nature of Love"
    show text "Canto: XVIII \n{color=#FF0000}The Slothful{/color}":
        align(0.5, 0.25)

  

    narrator "The fourth terrace was alive with movement, as the slothful ran ceaselessly along the path, their pace driven by the urgency they had lacked in life."
    narrator "Dante watched their desperate race, understanding how spiritual laziness had held them back from pursuing good."

    narrator "He felt the burning drive to overcome inertia and pursue purpose with all his strength."
    narrator "Their struggle served as a vivid reminder of the importance of persistence and determination."

    jump canto_19

label canto_19:
    # Canto 19: The Dream of the Siren
    hide text "Canto: XVIII \nThe Slothful"
    show text "Canto: XIX \n{color=#FF0000}The Dream of the Siren{/color}":
        align(0.5, 0.25)


    narrator "As night fell, Dante was overcome by a vivid dream of a siren."
    narrator "The siren sang a song of false allure, her beauty masking the decay beneath."
    narrator "Virgil appeared, dispelling the illusion and reinforcing the importance of discernment in the face of temptation."

    narrator "Virgil explained how the siren symbolized misplaced desires, urging Dante to seek higher truths."
    narrator "He reflected on the dangers of superficial attractions and the need for clarity of purpose."

    jump canto_20

label canto_20:
    # Canto 20: The Avaricious
    hide text "Canto: XIX \nThe Dream of the Siren"
    show text "Canto: XX \n{color=#FF0000}The Avaricious{/color}":
        align(0.5, 0.25)
    

    narrator "The fifth terrace stretched before them, where the avaricious lay prostrate on the ground, their faces pressed into the earth."
    narrator "Their weeping echoed through the terrace, lamenting their obsession with material wealth."
    narrator "'Here, they learn that true treasure lies not in gold, but in the richness of the spirit,' Virgil explained."

    narrator "He saw how the pursuit of wealth had shackled these souls, and vowed to value spiritual riches."
    narrator "His words brought a moment of solace to the suffering, and he felt their gratitude."

    jump canto_21

label canto_21:
    # Canto 21: The Sixth Terrace - Gluttony
    hide text "Canto: XX \nThe Avaricious"
    show text "Canto: XXI \n{color=#FF0000}Gluttony{/color}":
        align(0.5, 0.25)

    narrator "On the sixth terrace, Dante and Virgil encountered the gluttonous, who wandered eternally beneath fruit-laden trees."
    narrator "The tantalizing scent of the fruit tormented them, symbolizing their insatiable hunger in life."

    narrator "Virgil spoke of temperance, urging Dante to embrace moderation in all things."

    narrator "He understood the value of balance and the dangers of excess."
    narrator "Their stories of indulgence and regret moved him deeply, inspiring compassion and resolve."

    return


