def convex_polygon_area(p):
    a=sorted(p)
    start=a[0]
    up=[]
    down=[]
    for e in a:
        if e!=start:
            if start[1]<e[1]:
                up.append(e)
            else:
                down.append(e)
    merge=[start]+down+up[::-1]+[start]
    n=len(merge)
    area=0
    for i in range(n):
        area+=merge[i][0]*merge[(i+1)%n][1]-merge[i][1]*merge[(i+1)%n][0]
    return  area/2

def is_heterogram(s):
    x=''
    for e in s.lower():
        if 'a' <= e <='z':
            x+=e
    return len(set(x))==len(x)

def replace_ignorecase(s, a, b):
    temp=s.lower()
    ans=''
    i=0
    while i <len(temp):
        if i >len(temp)-len(a):
            ans+=s[i]
            i+=1
        elif temp[i:i+len(a)]==a.lower():
            i+=len(a)
            ans+=b
        else:
            ans+=s[i]
            i+=1
    return ans

def top3(votes):
    ans=[(-votes[a],a) for a in votes]
    ans.sort()
    return [b for a,b in ans][:3]

for i in range(2):
    exec(input().strip())