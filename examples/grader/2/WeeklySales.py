receive=input()
num=receive.split()
for c in range(0,len(num)):
    if c==0:
        money=int(num[c])
    else:
        money+=int(num[c])
print(money)