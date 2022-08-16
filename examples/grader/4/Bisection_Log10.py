a=float(input())
floor=0
loof=a
boo=True
while(boo):
    x=(floor+loof)/2
    if abs(a-10**x)<=10**(-10)*max(10**x,a):
        print(round(x,6))
        boo=False
    if 10**x>a:
        loof=x
    elif 10**x<a:
        floor=x