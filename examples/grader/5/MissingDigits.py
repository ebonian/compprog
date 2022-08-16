n=input()
ans=''
dg=['0','1','2','3','4','5','6','7','8','9']
chk=[0]*10
for i in range(len(n)):
    for j in range(len(dg)):
        if n[i]==dg[j]:
            chk[j]=1
if 0 not in chk:
    print("None")
else:
    for i in range(0,10):
        if chk[i]==0:
            if len(ans)==0:
                ans+=dg[i]
            else:
                ans+=","+dg[i]
    print(ans)
        