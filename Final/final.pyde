
import random
import time

Player1 = []
Player2 = []
Player3 = []
Player4 = []
Plays = 1
battle = 0


def setup():
    global Img1
    global Img2
    global Img3
    global Img4
    global vsimg
    Background = loadImage('background.png')
    Img1 = loadImage("Water.JPG")
    Img2 = loadImage("Air.JPG")
    Img3 = loadImage("Fire.JPG")
    Img4 = loadImage("Earth.JPG")
    vsimg = loadImage("versus.png")
    global Player1
    global Player2
    global Player3
    global Player4
    imageMode(CENTER)
    size(1920, 1080)
    # fullScreen()
    background(Background)  # Ilias kan je onze BG zetten, 
    print(battle)


def draw():
    global Player1
    global Player2
    global Player3
    global Player4
    global Plays
    global Battlemode
    if battle == 0:
        textSize(64)
        textMode(CORNERS)
        fill(0,0,0)
        Text = 'Player: ' + str(Plays)
        text(Text, (width/2)-200, (height/2)-450)
    elif battle == 1:
        if (mousePressed and (mouseButton == LEFT)):
            if (mouseX >= 320 and mouseY >= 750 and mouseX <= 520 and mouseY <= 1050):
                global card1
                card1 = 1
                
            if (mouseX >= 520 and mouseY >= 750 and mouseX <= 720 and mouseY <= 1050):
                global card1
                card1 = 2
                
            if (mouseX >= 720 and mouseY >= 750 and mouseX <= 920 and mouseY <=1050):
                global card1
                card1 = 3
                
            if (mouseX >= 920 and mouseY >= 750 and mouseX <= 1120 and mouseY <= 1050):
                global card1
                card1 = 4
                
            if (mouseX >= 320 and mouseY >= 50 and mouseX <= 520 and mouseY <= 350):
                global card2
                card2 = 1
                
            if (mouseX >= 520 and mouseY >= 50 and mouseX <= 720 and mouseY <= 350):
                global card2
                card2 = 2
                
            if (mouseX >= 720 and mouseY >= 50 and mouseX <= 920 and mouseY <= 350):
                global card2
                card2 = 3
                
            if (mouseX >= 920 and mouseY >= 50 and mouseX <= 1120 and mouseY <= 350):
                global card2
                card2 = 4
        
        if (mousePressed and (mouseButton == RIGHT)):
            print(card1, card2)
            battleset(card1,card2)
    

def mouseClicked():
    if battle == 0:
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
                
        if mouseButton == RIGHT:
                GivePlayersCard(Plays)
            
        
def keyPressed():
    Background = loadImage('background.png')
    # global Background
    global Plays
    global battle
    if key == 65535:
        if Plays>=4:
            Plays=1
        else:    
            Plays+=1
    # if keyCode == LEFT:
    # if keyCode == RIGHT:

    background(Background)
    if key == 'b':
        battle = 1
        print(battle)
        image(Img1, 420, 900, 200, 300)
        image(Img2, 620, 900, 200, 300)
        image(Img3, 820, 900, 200, 300)
        image(Img4, 1020, 900, 200, 300)
        image(Img1, 420, 200, 200, 300)
        image(Img2, 620, 200, 200, 300)
        image(Img3, 820, 200, 200, 300)
        image(Img4, 1020, 200, 200, 300)
        image(vsimg, 960, 540)
        textSize(18)
        fill(0,0,0)
        text("Left click on the bottom cards for player 1, left click on the top cards for player 2. press right click and the winning card will be desplayed", 0, 18)
        text("player 2", 232, 200)
        text("player 1", 232, 900)
        textSize(30)
        text("winning card", 1600, 200)
        
    if key == 'q':
        battle = 0
    
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
        image(Img1, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 1
    elif x == 2:
        image(Img2, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 2
    elif x==3:
        image(Img3, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 3
    else:
        image(Img4, (width/2), (height/2))
        # time.sleep(5)
        # background(255,255,255)
        return 4

def battleset(card1,card2):
    if card1 != 0 and card2 != 0:
        condition = (card1 == 1 and card2 == 3) or (card1 == 3 and card2 == 2) or (card1 == 2 and card2 == 4) or (card1 == 4 and card2 == 1)
        condition2 = (card2 == 1 and card1 == 3) or (card2 == 3 and card1 == 2) or (card2 == 2 and card1 == 4) or (card2 == 4 and card1 == 1)
        if condition == True:
            if card1 == 1:
                image(Img1, 1700, 540)
            if card1 == 2:
                image(Img2, 1700, 540)
            if card1 == 3:
                image(Img3, 1700, 540)
            if card1 == 4:
                image(Img4, 1700, 540)
        if condition2 == True:
            if card2 == 1:
                image(Img1, 1700, 540)
            if card2 == 2:
                image(Img2, 1700, 540)
            if card2 == 3:
                image(Img3, 1700, 540)
            if card2 == 4:
                image(Img4, 1700, 540)
        if condition == False and condition2 == False:
            print("no victory")
