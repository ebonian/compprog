name=['Robert','William','James','John','Margaret','Edward','Sarah','Andrew','Anthony','Deborah','Dick','Bill','Jim','Jack','Peggy','Ed','Sally','Andy','Tony','Debbie']
n=int(input())
ans=[]
for i in range(n):
    chg=input()
    c=0
    for j in range(20):
        if chg==name[j]:
            c=1
            if j<10:
                ans+=[name[j+10]]
            elif j<20:
                ans+=[name[j-10]]
    if c==0:
        ans+=["Not found"]
for i in range(len(ans)):
    print(ans[i])