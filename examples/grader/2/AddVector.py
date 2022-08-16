u=input()
u= u[1:-1]
a=u.split(", ")
if a[-1][-1]==']':
    a[-1][-1]=a[-1][:-1]
v=input()
v=v[1:-1]
b=v.split(", ")
if b[-1][-1]==']':
    b[-1]=b[-1][:-1]
a=[float(a[0])]+[float(a[1])]+[float(a[2])]
b=[float(b[0])]+[float(b[1])]+[float(b[2])]
c=[a[0]+b[0]]+[a[1]+b[1]]+[a[2]+b[2]]
print(a,"+",b,"=",c)