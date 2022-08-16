d=int(input())
m=int(input())
y=int(input())
y-=543
ans=d
for c in range (1,m):
    if c==1 or c==3 or c==5 or c==7 or c==8 or c==10 or c==12:
        ans+=31
    elif c==4 or c==6 or c==9 or c==11:
        ans+=30
    else:
        if y%4==0 and y%100!=0:
            ans+=29
        elif y%400==0:
            ans+=29
        else:
            ans+=28
print(ans)