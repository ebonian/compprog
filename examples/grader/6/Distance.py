import math as m
def distance1(x1,y1,x2,y2):
    dx=x2-x1
    dy=y2-y1
    return m.sqrt(dx**2+dy**2)

def distance2(p1,p2):
    dx=p2[0]-p1[0]
    dy=p2[1]-p1[1]
    return m.sqrt(dx**2+dy**2)

def distance3(c1,c2):
    x=distance2(c1,c2)
    r=c1[2]+c2[2]
    bl=x<=r
    return x,bl

def perimeter(point):
    sum=0
    for i in range (len(point)):
        if i<len(point)-1:
            sum+=distance2(point[i],point[i+1])
        else:
            sum+=distance2(point[i],point[0])
    return sum

exec(input().strip())