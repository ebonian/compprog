n=int(input())
num={}
for i in range (n):
    major,p=input().split()
    num[major]=int(p)
m=int(input())
data={}
for i in range (m):
    text=input().split()
    id=text[0]
    score=[float(text[1])]
    score+=text[2:]
    data[id]=score
sorted_data=sorted(data.items(),key= lambda x :x[1],reverse=True)
ans=[]
for e in sorted_data:
    for r in e[1][1:]:
        if num[r]!=0:
            ans.append([e[0],r])
            num[r]-=1
            break
ans.sort()
for e in ans:
    print(e[0],e[1])