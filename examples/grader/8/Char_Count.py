count={}
text=input().lower()
for i in text:
    if 'a' <= i <= 'z':
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
ans=[]
for i in count:
    ans.append([-count[i],i])
ans.sort()
for i in range (len(ans)):
    print(ans[i][1],'->',-ans[i][0])