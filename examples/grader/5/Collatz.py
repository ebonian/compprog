n=int(input())
ans=[n]
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=3*n+1
    ans+=[n]
anss=ans[-15:]
for i in range(len(anss)):
    if i!=len(anss)-1:
        print(anss[i],end="->")
    else:
        print(anss[i])