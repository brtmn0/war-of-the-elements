def setup():
    fullScreen()
    global img
    size(1920,1080)
    img = loadImage("kaartenproject.jpg")
    
def draw():
    fullScreen()
    background(0)
    image(img, 0, 0)
    
    
