n=int(input())
union=set()
intersect=set()
for i in range (n):
    s=set(int(e) for e in input().split())
    if i==0:
        union=s
        intersect=s
    else:        
        union=union | s
        intersect=intersect & s
print(len(union))
print(len(intersect))
