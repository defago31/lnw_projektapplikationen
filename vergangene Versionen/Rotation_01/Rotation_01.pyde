#Definition Grösse Ausgabefenster 
w=1000
h=1000

#Definition Mittelpunkt
xcenter=w/2
ycenter=h/2


##Abstände Sonne bis Planeten
##Sonne-Merkur: 58 Millionen km
##Umlaufzeit: 88 d
##Sonne-Venus: 108 Millionen km
##Umlaufzeit: 225 d
##Sonne-Erde: 147 Millionen km
##Umlaufzeit: 365 d
##Sonne-Mars: 228 Millionen km
##Umlaufzeit: 687 d

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
rotmerkur=0

#Venus
r2=0.9*h/2/228*108
rotvenus=0

#Erde
r3=0.9*h/2/228*147
roterde=0
#Mond
rotmond=0

#Mars
r4=0.9*h/2/228*228
rotmars=0


def setup():
    
    size(w,h)
    frameRate(60)
    

def draw():
    
    global rotmerkur
    global rotvenus
    global roterde
    global rotmond
    global rotmars
    
    background(0,0,0)
    
    #Sternenhimmel
    for i in range(5):
        xstar=random(0,w)
        ystar=random(0,h)
        fill(255,255,255)
        ellipse(xstar,ystar,5,5)
    
    #Sonne
    fill(255,255,0)
    circle(w/2,h/2,d0)
    
    pushMatrix()
    translate(xcenter,ycenter)
    
    #Merkur
    fill(255,0,0)
    rotate(radians(rotmerkur))
    circle(r1*cos(radians(0)),r2*sin(radians(0)),10)

    #Venus
    fill(0,255,0)
    rotate(radians(rotvenus))
    circle(r2*cos(radians(0)),r2*sin(radians(0)),20)

    #Erde und Mond
    fill(0,0,255)
    rotate(radians(roterde))
    circle(r3*cos(radians(0)),r3*sin(radians(0)),25)
    
    pushMatrix()
    translate(r3*cos(radians(0)),r3*sin(radians(0)))
    rotate(radians(rotmond))
    fill(255)
    circle(25,r3*sin(radians(0)),10)
    popMatrix()

    #Mars
    fill(0,0,150)
    rotate(radians(rotmars))
    circle(r4*cos(radians(0)),r4*sin(radians(0)),20)

    
    popMatrix()
    
    rotmerkur+=1
    rotvenus+=2
    roterde+=1
    rotmond+=2
    rotmars-=1
    

    
    

    
    
    
    
    
    
    

    

    

        

        
        
        
    


    
    
    
    
    
