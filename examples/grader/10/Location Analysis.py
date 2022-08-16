n=int(input())
data={}
ans=[]
for i in range(n):
    id,place=input().split(':')
    ans.append(id)
    data[id]=set(place.split(','))
search=input()
for a,b in data.items():
    if len(data[search] & b) == 0 or a==search:
        ans.remove(a)
if len(ans) == 0:
    print('Not Found')
else:
    for e in ans:
        print(e)