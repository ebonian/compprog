import math as mt
bd, bm, by, d, m, y = [int(e) for e in input().split()]
dim=[31,28,31,30,31,30,31,31,30,31,30,31]
sum=0
by-=543
y-=543
for i in range(bm-1,12):
    sum+=dim[i]
    if ((by%4==0 and by%100!=0) or by%400==0) and i==1:
        sum+=1
chk1=sum
sum= sum-bd+1
chk2=sum
sum+=(365*(y-by-1))
chk3=sum
for i in range(0,m-1):
    sum+=dim[i]
    if ((y%4==0 and y%100!=0) or y%400==0) and i==1:
        sum+=1
chk4=sum
sum+=d-1
chk5=sum
print(str(sum)+" {:.2f}".format(mt.sin((2*mt.pi*sum)/23))+" {:.2f}".format(mt.sin((2*mt.pi*sum)/28))+" {:.2f}".format(mt.sin((2*mt.pi*sum)/33)))
