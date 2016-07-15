# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
image bedbg = "bed-bg.jpg"
image busstop = "bus.jpg"

# Declare characters used by this game.
define m = Character('Makoto', color="#00FFFF")
define t = Character('Takano', color="#FFFFFF")


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
    
    m "Bus should be coming soon..."
    
    m "Ah! The bus is here!"
    
    "The bus doesn't stop and continues driving, skipping Takano."
    
    m "Hey!!!!"

return
