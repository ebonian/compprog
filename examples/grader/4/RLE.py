sen=input()
mem=sen[0]
c=0
ans=''
for i in range (0,len(sen)):
    if sen[i]!=mem:
        ans+=mem+" "+str(c)+" "
        mem=sen[i]
        c=1
    else:
        c+=1
ans+=mem+" "+str(c)
print(ans)