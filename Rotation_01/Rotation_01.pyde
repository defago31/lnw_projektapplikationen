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
a1=0

#Venus
r2=0.9*h/2/228*108
a2=0

#Erde
r3=0.9*h/2/228*147
a3=0

#Mars
r4=0.9*h/2/228*228
a4=0


def setup():
    
    size(w,h)
    frameRate(60)
    

def draw():
    
    global a1
    global a2
    global a3
    global a4
    
    background(0,0,0)
    
    for i in range(5):
        xstar=random(0,w)
        ystar=random(0,h)
        fill(255,255,255)
        ellipse(xstar,ystar,5,5)
    
    #Sonne
    fill(255,255,0)
    circle(w/2,h/2,d0)
    
    pushMatrix()
    
    fill(255,0,0)
    translate(xcenter,ycenter)
    
    rotate(radians(a1))
    a1+=1
    circle(r1*cos(radians(0)),r2*sin(radians(0)),10)

    
    fill(0,255,0)
    rotate(radians(a2))
    a2+=1
    circle(r2*cos(radians(0)),r2*sin(radians(0)),20)

    
    fill(0,0,255)
    rotate(radians(a3))
    a3+=2
    circle(r3*cos(radians(0)),r3*sin(radians(0)),25)

    
    fill(0,0,150)
    rotate(radians(a4))
    a4+=0
    circle(r4*cos(radians(0)),r4*sin(radians(0)),20)

    
    popMatrix()
    

    
    

    
    
    
    
    
    
    

    

    

        

        
        
        
    


    
    
    
    
    
