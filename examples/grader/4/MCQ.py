key=input()
ans=input()
c=0
if len(key)!=len(ans):
    print("Incomplete answer")
else:
    for n in range (0,len(key)):
        if key[n]==ans[n]:
            c+=1
    print(c)