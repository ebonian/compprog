# HW01 (Don't delete this line or add any line above this line.)

frames = [float(x) for x in input().split()]

# write your program under this line
def findCenter(x, y, w, h):
    return (x + w / 2, y - h / 2)

def findDistance(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    r1 = findCenter(r1x,r1y,r1w,r1h)
    r2 = findCenter(r2x,r2y,r2w,r2h)
    return ((r1[0] - r2[0]) ** 2 + (r1[1] - r2[1]) ** 2) ** 0.5

def findIntersection(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    dx = min(r1x + r1w, r2x + r2w) - max(r1x, r2x)
    dy = min(r1y, r2y) - max(r1y - r1h, r2y - r2h)
    if (dx>=0) and (dy>=0): return dx*dy
    else: return 0.0

def findUnion(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    return r1w * r1h + r2w * r2h - findIntersection(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h)

def findIou(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h):
    return findIntersection(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h) / findUnion(r1x, r1y, r1w, r1h, r2x, r2y, r2w, r2h)

while True:
    userInput = input().lower()
    command = userInput.split()[0]
    args = [int(x) for x in userInput.split()[1:]]

    if command == "center":
        print(findCenter(
            frames[(args[0] - 1) * 4 + 0], 
            frames[(args[0] - 1) * 4 + 1], 
            frames[(args[0] - 1) * 4 + 2], 
            frames[(args[0] - 1) * 4 + 3]
        ))
    elif command == "distance":
        print(findDistance(
            frames[(args[0] - 1) * 4 + 0], 
            frames[(args[0] - 1) * 4 + 1], 
            frames[(args[0] - 1) * 4 + 2], 
            frames[(args[0] - 1) * 4 + 3],
            frames[(args[1] - 1) * 4 + 0], 
            frames[(args[1] - 1) * 4 + 1], 
            frames[(args[1] - 1) * 4 + 2], 
            frames[(args[1] - 1) * 4 + 3],
        ))
    elif command == "intersection":
        print(findIntersection(
            frames[(args[0] - 1) * 4 + 0], 
            frames[(args[0] - 1) * 4 + 1], 
            frames[(args[0] - 1) * 4 + 2], 
            frames[(args[0] - 1) * 4 + 3],
            frames[(args[1] - 1) * 4 + 0], 
            frames[(args[1] - 1) * 4 + 1], 
            frames[(args[1] - 1) * 4 + 2], 
            frames[(args[1] - 1) * 4 + 3],
        ))
    elif command == "union":
        print(findUnion(
            frames[(args[0] - 1) * 4 + 0], 
            frames[(args[0] - 1) * 4 + 1], 
            frames[(args[0] - 1) * 4 + 2], 
            frames[(args[0] - 1) * 4 + 3],
            frames[(args[1] - 1) * 4 + 0], 
            frames[(args[1] - 1) * 4 + 1], 
            frames[(args[1] - 1) * 4 + 2], 
            frames[(args[1] - 1) * 4 + 3],
        ))
    elif command == "iou":
        print(findIou(
            frames[(args[0] - 1) * 4 + 0], 
            frames[(args[0] - 1) * 4 + 1], 
            frames[(args[0] - 1) * 4 + 2], 
            frames[(args[0] - 1) * 4 + 3],
            frames[(args[1] - 1) * 4 + 0], 
            frames[(args[1] - 1) * 4 + 1], 
            frames[(args[1] - 1) * 4 + 2], 
            frames[(args[1] - 1) * 4 + 3],
        ))
    elif command == "end":
        break