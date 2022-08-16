psum=0
ssum=0
difsum=0
for i in range (9):
    par,stroke,use=[int(e) for e in input().split()]
    if use:
        dif=min(par+2,stroke)
        difsum+=dif
    psum+=par
    ssum+=stroke
adv=0.8*(1.5*difsum-psum)
if adv>=0:
    adv=int(adv)
else:
    adv=int(adv-1)
ans=ssum-adv
print(ssum)
print(adv)
print(ans)