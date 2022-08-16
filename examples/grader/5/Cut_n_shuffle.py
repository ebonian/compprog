s=input().split()
n=len(s)
a=n//2
sen=input()
for i in range(len(sen)):
    if sen[i]=='C':
        n1=s[:a]
        n2=s[a:]
        s=n2+n1
    elif sen[i]=='S':
        n1=s[:a]
        n2=s[a:]
        for j in range (a):
            if j==0:
                s=[n1[j]]+[n2[j]]
            else:
                s+=[n1[j]]+[n2[j]]
for i in range (n):
    print(s[i],end=" ")