boo=True
c=1
while(boo):
    num=input()
    if num=="Zig-Zag" or num =="Zag-Zig":
        boo=False
    else:
        num=num.split()
        x=int(num[0])
        y=int(num[1])
        if c==1:
            max2=x #max (Zag-Zig)
            max1=y #max (Zig-Zag)
            min2=y #min (Zag-Zig)
            min1=x #min (Zig-Zag)
        else:
            if c%2==0:
                if max1<x:
                    max1=x
                if max2<y:
                    max2=y
                if min1>y:
                    min1=y
                if min2>x:
                    min2=x
            elif c%2==1:
                if max1<y:
                    max1=y
                if max2<x:
                    max2=x
                if min1>x:
                    min1=x
                if min2>y:
                    min2=y
    c+=1   
if  num=="Zig-Zag":
    print(min1,max1)
elif num =="Zag-Zig":
    print(min2,max2)