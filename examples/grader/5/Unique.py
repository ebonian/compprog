n=[int(e) for e in input().split()]
n.sort()
chk=n[0]
ans=[n[0]]
c=1
for i in range(1,len(n)):
    if chk!=n[i]:
        c+=1
        chk=n[i]
        if c<=10:
            ans+=[chk]
print(c)
print(ans)