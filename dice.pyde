import random

def setup():
    size(400,400)
    rectMode(CENTER)
    rect(width/2, height/2, 300, 300)

def draw():
    frameRate(60)
            
def mousePressed():
    if (mousePressed and (mouseButton == LEFT)):
        rectMode(CENTER)
        rect(width/2, height/2, 300, 300)
        dice = roll()
        if dice == 1:
            ellipse(width/2, height/2, 50, 50)
        elif dice == 2:
            ellipse(150, 150, 50, 50)
            ellipse(250, 250, 50, 50)
        elif dice == 3:
            ellipse(150, 150, 50, 50)
            ellipse(200, 200, 50, 50)
            ellipse(250, 250, 50, 50)
        elif dice == 4:
            ellipse(150, 150, 50, 50)
            ellipse(250, 250, 50, 50)
            ellipse(150, 250, 50, 50)
            ellipse(250, 150, 50, 50)
        elif dice == 5:
            ellipse(150, 150, 50, 50)
            ellipse(250, 250, 50, 50)
            ellipse(150, 250, 50, 50)
            ellipse(250, 150, 50, 50)
            ellipse(200, 200, 50, 50)
        else:
            ellipse(100, 100, 50, 50)
            ellipse(100, 200, 50, 50)
            ellipse(100, 300, 50, 50)
            ellipse(300, 100, 50, 50)
            ellipse(300, 200, 50, 50)
            ellipse(300, 300, 50, 50)
            
                

def roll():
    a = random.randint(1,6)
    print(a)
    return a
