import math
W=float(input())
H=float(input())
print(math.sqrt(W*H)/60)
print(0.024265*W**0.5378*H**0.3964)
print(0.0333*W**(0.6157-0.0188*math.log(W,10))*H**0.3)