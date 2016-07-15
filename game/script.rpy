# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bedbg = "bed-bg.jpg"
image busstop = "bus.jpg"

# Declare characters used by this game.
define m = Character('Makoto', color="#00FFFF")
define t = Character('Takano', color="#FFFFFF")

#Declare Sounds
define audio.ding = "sound/ding.mp3"


# The game starts here.
label start:
    scene bedbg
    "Today is a sunny day"

    m "I wonder what I'm going to do today..."

    m "I know! I'll create a game with a friend!"

    m "Let's call up Takano..."
    
    "Ring.... Ring......"
    
    t "Hello?"
    
    m "Hey Takano, you want to hang out?"
    
    t "Sure."
    
    m "Ok, lets meet up at my house."
    
    t "Ye m8."
    
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
    
    t "Bus... just... missed... me... twice. Send!"
    
    m "lmfao"
    
    
    
    

return
