n=int(input())
x=[]
y=[]
for i in range(1,n+1):
    num=input().split( )
    x+=[num[0]]
    y+=[num[1]]
word=input()
if word=="Zig-Zag":
    min=int(x[0])
    max=int(y[0])
    for i in range (1,n+1):
        if i%2==1:
            if min>int(x[i-1]):
                min=int(x[i-1])
            if max<int(y[i-1]):
                max=int(y[i-1])
        else:
            if min>int(y[i-1]):
                min=int(y[i-1])
            if max<int(x[i-1]):
                max=int(x[i-1])
elif word=="Zag-Zig":
    min=int(y[0])
    max=int(x[0])
    for i in range (1,n+1):
        if i%2==1:
            if min>int(y[i-1]):
                min=int(y[i-1])
            if max<int(x[i-1]):
                max=int(x[i-1])
        else:
            if min>int(x[i-1]):
                min=int(x[i-1])
            if max<int(y[i-1]):
                max=int(y[i-1])
print(min,max)