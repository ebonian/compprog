a=float(input())
num=a
floor=0
n=0
boo=True
while(boo):
    if a==0:
        boo=False
    else:
        a//=10
        n+=1
loof=n
boo=True
while(boo):
    x=(floor+loof)/2
    if abs(num-10**x)<=10**(-10)*max(10**x,num):
        print(round(x,6))
        boo=False
    if 10**x>num:
        loof=x
    elif 10**x<num:
        floor=x