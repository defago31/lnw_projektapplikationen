#Definition Grösse Ausgabefenster 
w=1200
h=1200

#Definition Mittelpunkt
xcenter=w/2
ycenter=h/2

##Abstände Sonne bis Planeten
##Rotation um die Sonne der verschiedenen Planeten

#Merkur
distancesonnemerkur=58.0
rotdaymerkur=88.0

#Venus
distancesonnevenus=108.0
rotdayvenus=225.0

#Erde
distancesonneerde=147.0
rotdayerde=365.0

#Mond
rotdaymond=4000.0

#Mars
distancesonnemars=228.0
rotdaymars=687.0


##Sonne-Jupiter: 778 Millionen km
##Umlaufzeit: 12 y
##Sonne-Saturn: 1430 Millionen km
##Umlaufzeit: 29 y
##Sonne-Uranus: 2800 Millionen km
##Umlaufzeit: 84 y
##Sonne-Neptun: 4650 Millionen km
##Umlaufzeit: 165 y


#Sonne
r0=40
d0=2*r0

#Merkur
r1=0.6*h/2/distancesonneerde*distancesonnemerkur
rotmerkur=0.0

#Venus
r2=0.6*h/2/distancesonneerde*distancesonnevenus
rotvenus=0.0

#Erde
r3=0.6*h/2/distancesonneerde*distancesonneerde
roterde=0.0
#Mond
rotmond=0.0

#Mars
r4=0.6*h/2/distancesonneerde*distancesonnemars
rotmars=0.0


def setup():
    
    size(w,h)
    frameRate(60)
    

def draw():
    
    print(frameRate)
    
    global rotmerkur
    global rotdaymerkur
    global rotvenus
    global rotdayvenus
    global roterde
    global rotdayerde
    global rotmond
    global rotdaymond
    global rotmars
    global rotdaymars
    
    global xcenter
    global ycenter
    
    
    background(0,0,0)
    

    
    #Sternenhimmel
    for i in range(4):
        xstar=random(0,w)
        ystar=random(0,h)
        fill(255,255,255)
        circle(xstar,ystar,4)
    

    #Umlaufbahnen
    pushMatrix()
    translate(xcenter,ycenter)
    stroke(255,255,255)
    fill(0)
    circle(0,0,2*r4)
    circle(0,0,2*r3)
    circle(0,0,2*r2)
    circle(0,0,2*r1)
    popMatrix()
    
    
    
    #Infotafeln auf Umlaufbahn
    rectMode(CORNER)
    fill(80)
      
    
    #Quadrat Farbwechsel auf Umlaufbahn Merkur
    rect(xcenter+r1-5,ycenter-5,10,10)
    if mouseX>=xcenter+r1-5 and mouseX<=xcenter+r1-5+10 and mouseY>=ycenter-5 and mouseY<=ycenter-5+10 and mousePressed==True:
        fill(255,50,50)
        rect(xcenter+r1-5,ycenter-5,10,10)
        fill(255)
        textSize(40)
        text("Merkur, kleinster Planet",50,100)
        #print("yes")
    else:
        fill(80)
        rect(xcenter+r1-5,ycenter-5,10,10)
        textSize(20)
        text("Infos? Klicke und halte die Maus auf dem Rechteck.",w/4,200)
        #print("no")
    
    #Quadrat Farbwechsel auf Umlaufbahn Venus    
    rect(xcenter+r2-10,ycenter-10,20,20)
    if mouseX>=xcenter+r2-10 and mouseX<=xcenter+r2-10+20 and mouseY>=ycenter-10 and mouseY<=ycenter-10+20 and mousePressed==True:
        fill(0,250,50)
        rect(xcenter+r2-10,ycenter-10,20,20)
        fill(255)
        textSize(40)
        text("Venus, naechster Nachbar der Erde",50,100)
        #print("yes")
    else:
        fill(80)
        rect(xcenter+r2-10,ycenter-10,20,20)
        textSize(20)
        text("Infos? Klicke und halte die Maus auf dem Rechteck.",w/4,200)
        #print("no")

    #Quadrat Farbwechsel auf Umlaufbahn Erde
    rect(xcenter+r3-15,ycenter-15,30,30)
    if mouseX>=xcenter+r3-15 and mouseX<=xcenter+r3-13+30 and mouseY>=ycenter-15 and mouseY<=ycenter-15+30 and mousePressed==True:
        fill(0,250,50)
        rect(xcenter+r3-15,ycenter-15,30,30)
        fill(255)
        textSize(40)
        text("Erde/Mond, unsere Heimat",50,100)
        #print("yes")
    else:
        fill(80)
        rect(xcenter+r3-15,ycenter-15,30,30)
        textSize(20)
        text("Infos? Klicke und halte die Maus auf dem Rechteck.",w/4,200)
        #print("no")
    
    #Quadrat Farbwechsel auf Umlaufbahn Mars
    rect(xcenter+r4-20,ycenter-20,40,40)
    if mouseX>=xcenter+r4-20 and mouseX<=xcenter+r4-20+40 and mouseY>=ycenter-20 and mouseY<=ycenter-20+40 and mousePressed==True:
        fill(0,50,250)
        rect(xcenter+r4-20,ycenter-20,40,40)
        fill(255)
        textSize(40)
        text("Mars, zweitkleinster Planet",50,100)
        #print("yes")
    else:
        fill(80)
        rect(xcenter+r4-20,ycenter-20,40,40)
        textSize(20)
        text("Infos? Klicke und halte die Maus auf dem Rechteck.",w/4,200)
        #print("no")

    
    #Sonne
    fill(255,255,0)
    circle(w/2,h/2,d0)
    
    #Merkur
    pushMatrix()
    translate(xcenter,ycenter)
    fill(150,150,150)
    rotate(radians(rotmerkur))
    circle(r1*cos(radians(0)),r2*sin(radians(0)),10)
    popMatrix()
    
    #Venus
    pushMatrix()
    translate(xcenter,ycenter)
    fill(137,207,240)
    rotate(radians(rotvenus))
    circle(r2*cos(radians(0)),r2*sin(radians(0)),20)
    popMatrix()

    #Erde und Mond
    pushMatrix()
    translate(xcenter,ycenter)
    fill(0,0,255)
    rotate(radians(roterde))
    circle(r3*cos(radians(0)),r3*sin(radians(0)),25)
    translate(r3*cos(radians(0)),r3*sin(radians(0)))
    rotate(radians(rotmond))
    fill(150,150,150)
    circle(25,r3*sin(radians(0)),10)
    popMatrix()

    #Mars
    pushMatrix()
    translate(xcenter,ycenter)
    fill(250,0,0)
    rotate(radians(rotmars))
    circle(r4*cos(radians(0)),r4*sin(radians(0)),20)
    popMatrix()
    
    #Definition Rotationsgeschwindigkeit in Abhängigkeit zur Rotationsgeschwindigkeit der Erde
    rotmerkur+=rotdaymerkur/rotdayerde
    rotvenus+=rotdayvenus/rotdayerde
    roterde+=rotdayerde/rotdayerde
    rotmond+=rotdaymond/rotdayerde
    rotmars+=rotdaymars/rotdayerde
    




    

    
    

    
    
    
    
    
    
    

    

    

        

        
        
        
    


    
    
    
    
    
