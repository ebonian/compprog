import math
n=input().split(",") #0จำนวนเต็ม 1ทศนิยมไม่ซ้ำ 2 ทศนิยมซ้ำ
ad=n[1]+n[2] # เลขหลังทศนิยมทั้งหมด
n[1]+='0'
bottom=10**len(ad)-10**(len(n[1])-1) #ตัวส่วน
head=int(n[0])*bottom+int(ad)-int(n[1])//10 #ตัวเศษ
dv=math.gcd(head,bottom) 
print(head//dv,"/",bottom//dv)