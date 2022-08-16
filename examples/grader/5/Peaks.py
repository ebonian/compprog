n=[float(e) for e in input().split()]
c=0
for i in range(1,len(n)-1):
    if n[i]>n[i-1] and n[i]>n[i+1]:
        c+=1
print(c)