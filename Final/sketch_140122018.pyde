
import random
import time

Player1 = []
Player2 = []
Player3 = []
Player4 = []
Plays = 1


def setup():
    Background = loadImage('background.png')
    global Player1
    global Player2
    global Player3
    global Player4
    imageMode(CENTER)
    size(1920, 1080)
    # fullScreen()
    background(Background)  # Ilias kan je onze BG zetten, 


def draw():
    global Player1
    global Player2
    global Player3
    global Player4
    global Plays
    textSize(64)
    textMode(CORNERS)
    fill(0,0,0)
    Text = 'Player: ' + str(Plays)
    text(Text, (width/2)-200, (height/2)-450)
    if mouseButton == RIGHT:
        GivePlayersCard(Plays)
    

def mouseClicked():
    Background = loadImage('background.png')
    global Player1
    global Player2
    global Player3
    global Player4
    global Plays
    # global Background
    if mouseButton == LEFT:
        if Plays == 1:
            background(Background)  # Ilias kan je onze BG zetten, 
            # Plays +=1
            Player1.append(randomImage())
            # print('Player1: ', Player1)
        elif Plays == 2:
            background(Background)  # Ilias kan je onze BG zetten, 
            # Plays +=1
            Player2.append(randomImage())
            # print('Player2: ', Player2)
        elif Plays == 3: 
            background(Background)  # Ilias kan je onze BG zetten, 
            # Plays +=1
            Player3.append(randomImage())
            # print('Player3: ', Player3)
        elif Plays == 4:
            background(Background)  # Ilias kan je onze BG zetten, 
            # Plays = 1
            Player4.append(randomImage())
            # print('Player4: ', Player4)   
        # print(' ')

def keyPressed():
    Background = loadImage('background.png')
    # global Background
    global Plays
    if key == 65535:
        if Plays>=4:
            Plays=1
        else:    
            Plays+=1
    # if keyCode == LEFT:
    # if keyCode == RIGHT:

    background(Background)

    
def GivePlayersCard(x):
    if x == 1:
        Water = Player1.count(1)
        Air = Player1.count(2)
        Fire = Player1.count(3)
        Earth = Player1.count(4)
    elif x == 2:
        Water = Player2.count(1)
        Air = Player2.count(2)
        Fire = Player2.count(3)
        Earth = Player2.count(4)
    elif x == 3:
        Water = Player3.count(1)
        Air = Player3.count(2)
        Fire = Player3.count(3)
        Earth = Player3.count(4)
    elif x == 4:
        Water = Player4.count(1)
        Air = Player4.count(2)
        Fire = Player4.count(3)
        Earth = Player4.count(4)        
    print(Water, Air, Fire, Earth)
    Img1 = loadImage("Water.JPG")
    Img2 = loadImage("Air.JPG")
    Img3 = loadImage("Fire.JPG")
    Img4 = loadImage("Earth.JPG")
    image(Img1, ((width/2)-615), (height/2))
    image(Img2, ((width/2)-205), (height/2))
    image(Img3, ((width/2)+205), (height/2))
    image(Img4, ((width/2)+615), (height/2))
    WaterText = str(Water) + 'x'
    AirText = str(Air) + 'x'
    FireText = str(Fire) + 'x'
    EarthText = str(Earth) + 'x'
    textSize(64)
    fill(0)
    text(WaterText, ((width/2)-650), (height/2)+375)
    text(AirText, ((width/2)-240), (height/2)+375)
    text(FireText, ((width/2)+200), (height/2)+375)
    text(EarthText, ((width/2)+605), (height/2)+375)
        
        
        
def randomImage():
    x = random.randint(1,4)
    # print(x)
    if x == 1:
        Img = loadImage("Water.JPG")
        image(Img, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 1
    elif x == 2:
        Img = loadImage("Air.JPG")
        image(Img, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 2
    elif x==3:
        Img = loadImage("Fire.JPG")
        image(Img, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 3
    else:
        Img = loadImage("Earth.JPG")
        image(Img, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 4
