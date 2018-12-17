def setup():
    Background = loadImage('background.png')
    global Img1
    global Img2
    global Img3
    global Img4
    global vsimg
    Img1 = loadImage("Water.JPG")
    Img2 = loadImage("Air.JPG")
    Img3 = loadImage("Fire.JPG")
    Img4 = loadImage("Earth.JPG")
    vsimg = loadImage("versus.png")
    imageMode(CENTER)
    size(1920, 1080)
    background(Background)
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
def draw():
    frameRate(60)
    
def mousePressed():
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
        battle(card1,card2)

def battle(card1,card2):
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
