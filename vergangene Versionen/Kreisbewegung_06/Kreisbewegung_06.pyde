w=1000
h=1000

xc=w/2
yc=h/2

d1=200
d2=400
d3=450

x1=w/2+d2/2
y1=h/2+d2/2



alpha=[]
print(alpha)

for i in range (1,361):
    alpha.append(2*PI/360*i)
print(alpha)
print(len(alpha))
#print(2*PI/360*1)
#print(2*PI/360*360)


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
        circle(w/2+d2/2*cos(i),h/2+d2/2*sin(i),20)
        
        #circle(x1*cos(i),y1*sin(i),20)
        
        ##Test, welcher zum Schluss zum Resultat geführt hat!
        #circle(w/2+d2/2*cos(2*PI/360*270),h/2+d2/2*sin(2*PI/360*270),20)
        
        ##einzelne Tests
        #circle(w/2+d2/2*cos(0),h/2+d2/2*sin(0),20)
        #circle(w/2+d2/2*cos(PI/2),h/2+d2/2*sin(PI/2),30)
        #circle(w/2+d2/2*cos(PI),h/2+d2/2*sin(PI),40)
        #circle(w/2+d2/2*cos(3*PI/2),h/2+d2/2*sin(3*PI/2),50)
    


    
    
    
    
    
