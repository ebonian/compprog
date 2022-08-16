n=input().split()
n=[float(n[0])]+[float(n[1])]+[float(n[2])]+[float(n[3])]
ma=n[0]
mn=n[0]
if ma<n[1]:
    ma=n[1]
if ma<n[2]:
    ma=n[2]
if ma<n[3]:
    ma=n[3]
if mn>n[1]:
    mn=n[1]
if mn>n[2]:
    mn=n[2]
if mn>n[3]:
    mn=n[3]
print(round((n[0]+n[1]+n[2]+n[3]-mn-ma)/2,2))