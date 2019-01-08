
import random
import time

Player1 = []
Player2 = []
Player3 = []
Player4 = []
Plays = 1

def setup():
    Background = loadImage('BackgroundKS.png')
    global Player1
    global Player2
    global Player3
    global Player4
    imageMode(CENTER)
    fullScreen()
    background(Background)  

def draw():
    Background = loadImage('BackgroundKS.png')
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
        Img1 = loadImage("Water.png")
        Img2 = loadImage("Air.png")
        Img3 = loadImage("Fire.png")
        Img4 = loadImage("Earth.png")
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
            Img = loadImage("Water.png")
            image(Img, (width/2), (height/2))
            # time.sleep(5)
            # background(255,255,255)
            return 1
        elif x == 2:
            Img = loadImage("Air.png")
            image(Img, (width/2), (height/2))
            # time.sleep(5)
            # background(255,255,255)
            return 2
        elif x==3:
            Img = loadImage("Fire.png")
            image(Img, (width/2), (height/2))
            # time.sleep(5)
            # background(255,255,255)
            return 3
        else:
            Img = loadImage("Earth.png")
            image(Img, (width/2), (height/2))
            # time.sleep(5)
            # background(255,255,255)
            return 4
    
    global Plays
    global Player1
    global Player2
    global Player3
    global Player4
    myFont = createFont("A Grazing Mace", 10)
    textFont(myFont)
    textSize(64)
    fill(0,0,0)
    textMode(CENTER)
    Text = str(Plays)
    text(Text,1100,170)
    if mousePressed and 1280<mouseX<1480 and 910<mouseY<1040:
        background(Background)
        GivePlayersCard(Plays)    
       
    #def mouseReleased():
        #background(Background)
        
    #if mouseReleased and 800<mouseX<1280 and 0<mouseY<1080:
        #background(Background)
        #str(Plays)
    
    # global Background
    if mousePressed and 430<mouseX<640 and 910<mouseY<1040:
        time.sleep(0.3)
        background(Background)
        str(Plays)
        if Plays == 1:
            # Plays +=1
            Player1.append(randomImage())
            # print('Player1: ', Player1)
        elif Plays == 2:
            # Plays +=1
            Player2.append(randomImage())
            # print('Player2: ', Player2)
        elif Plays == 3: 
            # Plays +=1
            Player3.append(randomImage())
            # print('Player3: ', Player3)
        elif Plays == 4:
            # Plays = 1
            Player4.append(randomImage())
            # print('Player4: ', Player4)   
        # print(' ')
    
    if mousePressed and Plays <4 and 1650<mouseX<1830 and 80<mouseY<180:
        time.sleep(0.3)
        Plays +=1
        background(Background)
        
    if mousePressed and Plays >1 and 1400<mouseX<1600 and 80<mouseY<180 :
        time.sleep(0.3)
        Plays -=1
        background(Background)
    
    # if keyCode == LEFT:
    # if keyCode == RIGHT:
    
