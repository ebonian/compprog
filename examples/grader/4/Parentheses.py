sen=input()
n=len(sen)
for c in range(0,n):
    if sen[c]=='(':
        sen=sen[:c]+'['+sen[c+1:]
    elif sen[c]=='[':
        sen=sen[:c]+'('+sen[c+1:]
    elif sen[c]==')':
        sen=sen[:c]+']'+sen[c+1:]
    elif sen[c]==']':
        sen=sen[:c]+')'+sen[c+1:]
print(sen)