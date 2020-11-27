x1=20
y1=600
x2=600
y2=20
c=222

def setup():
    #Programmstart (Initialisierung)
    size(620,620)
    background(255,255,255)
    frameRate(24)

def draw():
    global x1
    global y1
    global x2
    global y2
    global c
    
    if x1<600:
        x1=x1+10
        x2=x2-10
        c=c-1
        stroke(c,c,c)
        line(x1,y1,x2,y2)

        
    
