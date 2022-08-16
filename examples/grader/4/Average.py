n=True
sum=0
c=0
while(n):
    num=input()
    if num=='q':
        n=False
        if c==0:
            print("No Data")
        else:
            print(round(sum/c,2))
    else:
        num=float(num)
        sum+=num
    c+=1