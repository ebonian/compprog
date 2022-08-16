key=input()
sen=input()
n=len(key)
count=0
k1='"'
k2='('
k3=')'
k4=','
k5='.'
k6="'"
k7=' '
for c in range (0,len(sen)-n+1):
    check=sen[c:c+n]
    if c!=0 and (c+n)!=len(sen):
        c1=sen[c-1]
        c2=sen[c+n]
        if check == key and (c1==k1 or c1==k2 or c1==k3 or c1==k4 or c1==k5 or c1==k6 or c1==k7) and (c2==k1 or c2==k2 or c2==k3 or c2==k4 or c2==k5 or c2==k6 or c2==k7):
            count+=1
    elif c==0:
        c2=sen[c+n]
        if check == key and (c2==k1 or c2==k2 or c2==k3 or c2==k4 or c2==k5 or c2==k6 or c2==k7):
            count+=1
    elif (c+n)==len(sen):
        c1=sen[c-1]
        if check == key and (c1==k1 or c1==k2 or c1==k3 or c1==k4 or c1==k5 or c1==k6 or c1==k7):
            count+=1
print(count)