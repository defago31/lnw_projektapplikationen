w=displayWidth
h=displayHeight

r1=200
r2=300
r3=450

def setup():
    global w
    global h
    
    size(w,h)
    background(255,255,255)
    
def draw():
    global w
    global h
    
    #fill(35,35,35)
    #stroke(55,55,55)
    circle(w/2,h/2,r2)
    #fill(200,45,66)
    #stroke(55,55,55)
    circle(w/2,h/2,r1)
