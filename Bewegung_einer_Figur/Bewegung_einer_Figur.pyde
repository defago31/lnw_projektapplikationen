x=100
y=100

def setup():
    size(640,480)
    
def draw():
    
    global x
    global y
    
    background(255,255,255)
    ellipse(x,y,50,50)
    x=x+1
    y=y+1
