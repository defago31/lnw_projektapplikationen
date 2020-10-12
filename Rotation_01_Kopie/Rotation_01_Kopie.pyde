#Definition Grösse Ausgabefenster 
w=1200
h=1200

#Definition Mittelpunkt
xcenter=w/2
ycenter=h/2


##Abstände Sonne bis Planeten
##Sonne-Merkur: 58 Millionen km
rotdaymerkur=88.0
##Sonne-Venus: 108 Millionen km
rotdayvenus=225.0
##Sonne-Erde: 147 Millionen km
rotdayerde=365.0
##Sonne-Mars: 228 Millionen km
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
#r0=0.9*h/2/228*0.7
r0=50
d0=2*r0


#Merkur
r1=0.9*h/2/228*58
rotmerkur=0.0

#Venus
r2=0.9*h/2/228*108
rotvenus=0.0

#Erde
r3=0.9*h/2/228*147
roterde=0.0
#Mond
rotmond=0.0

#Mars
r4=0.9*h/2/228*228
rotmars=0.0


def setup():
    
    size(w,h)
    frameRate(60)
    

def draw():
    
    #print(frameRate)
    
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
    
    background(0,0,0)
    
    #Sternenhimmel
    for i in range(4):
        xstar=random(0,w)
        ystar=random(0,h)
        fill(255,255,255)
        ellipse(xstar,ystar,4,4)
    
    #Sonne
    fill(255,255,0)
    circle(w/2,h/2,d0)
    
    pushMatrix()
    translate(xcenter,ycenter)
    #Merkur
    fill(150,150,150)
    rotate(radians(rotmerkur))
    circle(r1*cos(radians(0)),r2*sin(radians(0)),10)
    popMatrix()
    
    pushMatrix()
    translate(xcenter,ycenter)
    #Venus
    fill(137,207,240)
    rotate(radians(rotvenus))
    circle(r2*cos(radians(0)),r2*sin(radians(0)),20)
    popMatrix()

    pushMatrix()
    translate(xcenter,ycenter)
    #Erde und Mond
    fill(0,0,255)
    rotate(radians(roterde))
    circle(r3*cos(radians(0)),r3*sin(radians(0)),25)
    translate(r3*cos(radians(0)),r3*sin(radians(0)))
    rotate(radians(rotmond))
    fill(150,150,150)
    circle(25,r3*sin(radians(0)),10)
    popMatrix()

    pushMatrix()
    translate(xcenter,ycenter)
    #Mars
    fill(250,0,0)
    rotate(radians(rotmars))
    circle(r4*cos(radians(0)),r4*sin(radians(0)),20)
    popMatrix()
    
    rotmerkur+=rotdaymerkur/rotdayerde
    rotvenus+=rotdayvenus/rotdayerde
    roterde+=rotdayerde/rotdayerde
    rotmond+=1.5
    rotmars+=rotdaymars/rotdayerde
    


    

    
    

    
    
    
    
    
    
    

    

    

        

        
        
        
    


    
    
    
    
    
