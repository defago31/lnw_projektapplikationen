###Deklaration globaler Variablen

#kopf_x=300
#kopf_y=300

##Breite und Höhe des Bildschirms
#w=displayWidth
#h=displayHeight
w=1200
h=1200




##*import von Funktionen aus anderen Dateien (from "Datei" import "Funktion")
#from zusatz import kreuz




def setup():
    ##Programmstart (Initialisierung)
    #print("Programmstart")
    
    ##(Breite,Höhe)
    global w
    global h
    size(w,h)
    #size(1000,1000)
    
    textSize(24)
    fill(255,128,0)
    
    ##(rot,blau,grün --> rbg)
    #background(200,200,200)
    



def draw():
    ##laufendes Programm (Betriebsmodus)
    #print("im Betrieb")
    background(200,200,200)
    #fill(38,50,56)
    #text(frameRate,100,100)
    #text(frameCount,100,150)
    
    ##globale Variablen importieren
    #global kopf_x
    #global kopf_y
    
    
    ###Figuren und Formen
    
    ##ellipse(x,y,Breite,Höhe)
    #ellipse(200,200,300,200)
    #ellipse(mouseX,mouseY,30,30)
    ##Smiley
    #ellipse(kopf_x,kopf_y,200,200)
    #ellipse(kopf_x-30,kopf_y-30,20,20)
    #ellipse(kopf_x+30,kopf_y-30,20,20)
    #line(kopf_x-20,kopf_y+30,kopf_x+20,kopf_y+30)
    
    ##line(x1,y1,x2,y2)
    #line(100,100,200,200)
    #line(200,200,mouseX,mouseY)
    
    ##circle(x,y,durchmesser)
    #circle(200,200,100)
    
    ##triangle(x1,y1,x2,y2,x3,y3)
    #triangle(10,10,100,100,300,300)
    
    ##rect(x,y,breite,höhe)
    #rect(100,100,50,200)
    
    
    ###Eigenschaften von Formen
    
    ##Hintergrundfarbe(r,g,b)
    #background(30,40,50)
    
    ##Füllfarbe(r,g,b)
    #fill(30,40,50)
    
    ##Konturfarbe
    #stroke(40,35,40)
    
    ##Konturstärke in px(px)
    #strokeWeight(34)
    
    ##keine Füllung()
    #noFill()
    
    ##keine Kontur
    #noStroke()
    
    ##Modus, von wo aus Rechtecke gezeichnet werden; Werte: CORNER, CENTER
    #fill(194,24,91)
    #rectMode(CENTER)
    #rect(500,500,500,500)
    #fill(55,255,55)
    #rectMode(CORNER)
    #rect(500,500,500,500)
    
    ##eigene Formen (Polygone)
    #fill(0,121,107)
    #beginShape()
    #vertex(400,100)
    #vertex(500,200)
    #vertex(600,200)
    #vertex(800,900)
    #vertex(100,200)
    #endShape(CLOSE)
    
    
    ###Texte einblenden...
    #xPos=130
    #yPos=300
    #textSize(64)

    ##Schatten
    #fill(38,50,56)
    #text("Hello World",xPos-4,yPos-4)
    
    ##Haupttext
    #fill(236,63,122)
    #text("Hello World",xPos,yPos)
    
    
    ###Mauspositionen und Mausereignisse
    #mouseX (aktuelle Position)
    #mouseY (aktuelle Position)
    #pmouseX (vorherige Position)
    #pmouseY (vorherige Position)
    ##Linie die der Maus folgt
    #line(pmouseX,pmouseY,mouseX,mouseY)
    
    ##Mausklick abfangen
    ##Wenn Maus gedrückt ist, dann Linie zeichnen... (links, rechts, mitte)
    #if mousePressed==True:
        #if mouseButton==LEFT:
            #stroke(0,0,0)
        #if mouseButton==RIGHT:
            #stroke(255,0,0)
        #if mouseButton==CENTER:
            #stroke(0,0,255)
        #line(pmouseX,pmouseY,mouseX,mouseY)
    
    ##Feld soll leuchten, wenn drauf geklickt wird...
    p1=50
    p2=50
    rect(p1,p2,200,50)
    if mouseX>=p1 and mouseX<=p1+200 and mouseY>=p2 and mouseY<=p2+50 and mousePressed==True:
        fill(255,0,0)
    else:
        fill(60,60,60)
    
    ##Ereignisfunktion bei Mausklick...
    #text("Maustaste klicken",10,30)
#def mousePressed():
        #fill(180,180,180)
        #text("press",mouseX,mouseY)
#def mouseReleased():
        #fill(255,128,0)
        #text("release",mouseX-2,mouseY-2)
    
    ##weitere Mausfunktionen:
#def mousePressed():
#def mouseRelease():
#def mouseClick():
#def mouseMove():
#def mouseDragged():
