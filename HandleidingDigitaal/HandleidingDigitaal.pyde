x=1
def setup():
    global x
    size(1920,1080)
    
    #backgroundimage
    global img4
    img4 = loadImage('background.png')
    
    #nextbutton
    global img
    img = loadImage('next.png')
    
    #backbutton
    global img1
    img1 = loadImage('back.png')
    
    #gevechtstabel
    global img2
    img2 = loadImage('gevechtstabel.png')
    
    #elementtabel
    global img3
    img3 = loadImage('elementtabel.png')
    
def first():
    background(255)
    fill(0)
    
    #backgroundimage
    background(img4)

    #titel 
    textSize(80)
    text ("War Of The Elements",100,100)
    
    #kopjes
    textSize(30) 
    text ("Informatie over het spel",100,200)
    text ("Het spelbord bestaat uit:",100,310)
    text ("Wat betekenen de tegels op het bord:",100,520)
    text('Hoe speel je het spel:',100,790)
   
    #subkopjes
    textSize(25)
    text 
    text ("De iconen zijn zo verdeeld:",115,585)
    
    #text
    textSize(18) 
    text ("Het spel bevat minimaal 3 spelers en maximaal 4 spelers",130,230)
    text (" Het bord\n Pionnen (16x)\n Dobbelsteen\n Element kaarten (32x)\n Bad-/goodluck kaarten (20x)",130,340)
    text ("De tegels zonder icoon er in zijn battlefields daar kan gevochten worden.",130,550)
    text ("Kaart icoon: Trek 1 element kaart. Pas als je er op stil staat. Op dit icoon mag er ook gevochten worden\nSchild icoon: Je bent veilig zolang je er op staat. Op dit icoon mag er dus niet gevochten worden.\nGele ster: Trek een goodluck kaart als je hierop stil staat. Op dit icoon mag er ook gevochten worden.\nRode ster: Trek een badluck kaart als je hierop stil staat. Op dit icoon mag er ook gevochten worden.\nAls je op de regenboog tegel land heb je gewonnen. Deze bevind zich midden op  het bord.",130,610)
    text (' Elk speler heeft zijn eigen thuisbasis. Daar begin je met spelen van het spel. Iedereen heeft 4 pionnen\n in zijn eigen thuis basis. Elke speler begint met 4 willekeurig getrokken elementkaarten. Op het moment dat er\n gedobbeld word mag je zelf kiezen of je met de klok mee of tegen de klok in gaat. Zodra je elkaar\n passeert betekend het dat er een gevecht ontstaat. Zolang je op een tegel staat die het toestaat.\n  Zodra je in een gevecht komt. Zetten beide spelers ongeopend op tafel. Na dat alle 2 de kaarten op tafel zijn,\n worden de kaarten tegelijkertijd geopend. Dan wordt gekeken wie heeft gewonnen (zie kopje Wie wint in\n een battle ). Daarna leg je de gebruikte kaarten op een aparte stapel, en pak je opnieuw kaarten als je niet\n minimaal 3 kaarten in je hand hebt. Waardoor je dus minimaal 3 kaarten in je hand hebt. Als je gewonnen hebt',130,820)
    
    #nextbutton
    global img
    image(img,1800,530)

def Second():
    background(255)
    fill(0)
    
    #backgroundimage
    background(img4)
    
    #kopje
    textSize(30)
    text ('Wie wint een battle:',100,420)
    
    #subkopje
    textSize(25)
    text ('Wanneer mag je de goodluck and badluck kaarten gebruiken:',115,280)
    
    #text
    textSize(18)
    text (' spring je een ring naar binnen, en je blijft in hetzelfde ring tot je weer opnieuw iemand verslaat.\n Als je verloren hebt dan geldt het volgende: als je op de buitenste ring verliest, dan ga je terug naar thuisbasis,\n anders als je niet in de buitenste ring bent spring je een ring naar buiten, op de dichtstbijzijnde schild.\n Tot je opnieuw weer een battle hebt en wint of verliest. Op het moment dat je op de binnenste ring bent(de gekleurde tegel heb je gewonnen).',130,150)
    text ('Je mag de de goodluck kaarten gebruiken in je eigen beurt. Of als je net in een gevecht komt.\nBadluck kaarten daarin tegen moeten direct worden gebruikt.',130,310)

    #backbutton
    global img1
    image(img1,40,530)
    
    #gevechtstabel
    global img2
    image(img2,740,460)
    
    #elementtabel
    global img3
    image(img3,140,460)
        
def draw():
    clear()
    global x
    if x == 1:
        first()
    else:
        clear()
        setup()
        Second()
     
        
    if mouseButton == LEFT and 1800<mouseX<1850 and 525<mouseY<575:
        x+=1
    elif ((keyPressed) and (key == ENTER)):
        x+=1
    elif mouseButton== LEFT and 20<mouseX<80 and 525<mouseY<575:
        x=1
    elif ((keyPressed) and (key == BACKSPACE)):
        x=1
        
    print(x)
        
