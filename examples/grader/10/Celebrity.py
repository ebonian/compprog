def knows(R,x,y):
    if x==y: return False
    return y in R[x]

def is_celeb(R,x):
    for e in R:
        if knows(R,x,e): return False
        if not knows(R,e,x) and e!=x: return False
    return True

def find_celeb(R):
    for e in R:
        if is_celeb(R,e):   return e
    return

def read_relations():
    R=dict()
    name=set()
    while True:
        d=input().split()
        if len(d) == 1: break
        name.add(d[0])
        name.add(d[1])
        if d[0] not in R:
            R[d[0]]={d[1]}
        else:
            R[d[0]].add(d[1])
    for e in name - set(R):
        R[e]=set()
    return R

def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)

exec(input().strip())