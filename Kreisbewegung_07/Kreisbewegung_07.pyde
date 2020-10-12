w=1000
h=1000

xc=w/2
yc=h/2

d1=200
d2=400
d3=500

alpha=[]
print(alpha)

for i in range (1,361):
    alpha.append(2*PI/360*i)


def setup():
    
    size(w,h)
    background(255,255,255)


def draw():
    
    fill(255,255,255)
    #stroke(55,55,55)
    circle(w/2,h/2,d2)
    
    line(xc-200,yc,xc+200,yc)
    line(xc,yc+200,xc,yc-200)
    
    for i in alpha:
        
        
        #print(alpha)
        fill(255,1,1)
        #background(255,255,255)
        
        circle(w/2+d1/2*cos(i),h/2+d1/2*sin(i),20)
        
        circle(w/2+d2/2*cos(i),h/2+d2/2*sin(i),20)
        
        circle(w/2+d3/2*cos(i),h/2+d3/2*sin(i),20)
        
        
        
        
    


    
    
    
    
    
