n=int(input())
ans=[]
for i in range(n):
    num=int(input())
    ans+=[num]
b=[int(e) for e in input().split()]
ans+=b
c=0
while c!=-1:
    c=int(input())
    if c!=-1:
        ans+=[c]
aans=[]
for i in range(len(ans)):
    if i%2==0:
        aans+=[ans[i]]
    else:
        aans=[ans[i]]+aans
print(aans)