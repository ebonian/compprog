class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "("+str(self.x)+", "+str(self.y)+")"


class Rect:
    def __init__(self, p1, p2) -> None:
        self.lowerleft = p1
        self.upperright = p2

    def area(self):
        return (self.upperright.x-self.lowerleft.x)*(self.upperright.y-self.lowerleft.y)

    def contains(self, p):
        return (self.lowerleft.x <= p.x <= self.upperright.x) and (self.lowerleft.y <= p.y <= self.upperright.y)


x1, y1, x2, y2 = [int(e) for e in input().split()]
lowerleft = Point(x1, y1)
upperright = Point(x2, y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x, y = [int(e) for e in input().split()]
    p = Point(x, y)
    print(rect.contains(p))

"""
2 2 10 10
4
0 0
2 4
3 5
10 1
"""
