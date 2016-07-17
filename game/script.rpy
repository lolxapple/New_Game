# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bedbg = "bed-bg.jpg"
image busstop = "bus.jpg"
image house = "house.jpg"

# Declare characters used by this game.
define m = Character('Makoto', color="#00FFFF")
define t = Character('Takano', color="#FFFFFF")

#Declare Sounds
define audio.ding = "sound/ding.mp3"
define audio.dong = "sound/dingdong.mp3"
define audio.morning = "sound/morning.mp3"

#Define Misc



# The game starts here.
label start:

    $ action = False
    $ rom = False
    $ school = False
    
    scene bedbg
    with fade
    
    play audio "<from 0 to 10.4>sound/morning.mp3"
    
    m "What a nice morning..."
    
    ""

    m "I wonder what I'm going to do today..."

    m "I know! I'll create a game with a friend!"

    m "Let's call up Takano..."
    
    "Ring.... Ring......"
    
    t "Hello?"
    
    m "Hey Takano, you want to hang out?"
    
    t "Sure."
    
    m "Ok, lets meet up at my house."
    
    t "Ye m8."
    
    m "Bring your laptop!"
    
    stop sound
    stop audio
    
    
    scene busstop
    with fade
    
    t "Bus should be coming soon..."
    
    t "Ah! The bus is here!"
    
    "The bus doesn't stop and continues driving, skipping Takano."
    
    t "Hey!!! Shoot! The next bus should be coming in about 6 minutes..."
    
    scene busstop
    with fade
    
    "6 Minutes Later"
    
    "The bus comes by again and doesn't stop."
    
    t "No! Wait! Crap, guess I'll use a different bus stop..."
    
    play audio ding
    
    ""
    
    t "Makoto must've texted me asking what's taking so long..."
    
    "Takano replies that two busses just missed him."
    
    m "lmfao"
    
    scene busstop
    with fade
    
    "The bus arrives."
    t "Finally!"
    
    "Takano takes a seat, but then he remembers that his mom had asked him to thaw a chicken!"
    
    t "Oh shit."
    
    "Takano then furiously begins texting his sister, which is at home, to thaw a chicken."
    
    t "I hope she reads it..."
    
    scene house
    with fade
    
    ""
    
    play audio dong
    
    ""
    
    m "Coming!"
    
    "Makoto answers the door."
    
    t "Sup."
    
    m "Come in."
    
    ""
    
    scene bedbg
    with fade
    
    t "So what's up?"
    
    m "Let's make a game!"
    
    t "Hm? What type of game?"
    
    m "A visual novel!"
    
    t "Alright, I know a pretty good engine."
    
    m "Really, what's it called?"
    
    t "It was called Pan.Py or something."
    
    m "Sounds lit."
    
    t "So what's the story about?"
    
    m "Shit, I don't know."
    
    t "Hmm... what do you want it to be about?"
    
    m "Hmm..."
    
menu:
    "What should the visual novel be about?"
    
    "An action.":
        $ action = True
        jump start2
    
    "A romance.":
        $ rom = True
        jump start2
    
    "School life.":
        $ school = True
        jump start2
    
    "Honestly don't know.":
        jump dead1
    
label start2:

    if action:
        m "Let's make it an action!"
        
    if rom:
        m "Let's make it a romance!"
        
    if school:
        m "Let's make a school life!"
        
    t "Alright. Sounds good."
    
    t "So what's the game going to be called?"
    
    m "Shit, I don't know..."
    
    if action:
        $ aname = renpy.input ("What's the name of the action visual novel?")
        if aname == "":
            $ aname = "Fight-on"
    
    m "Let's call it \"%(aname)s!\""
       
    
return
    
    
label dead1:
    t "You don't know?"
    
    m "Completely out of ideas."
    
    t "Oh well. Let's go play some Pokemon GO!"
    
    ""
    
    ".:. Bad Ending."
    
    return
    
    
    
return
