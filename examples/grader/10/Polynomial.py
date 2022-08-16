def add_poly(p1, p2):
    num={}
    exp=[]
    for n,e in p1:
        if e not in num:
            num[e]=n
            exp.append(e)
        else:
            num[e]+=n
    for n,e in p2:
        if e not in num:
            num[e]=n
            exp.append(e)
        else:
            num[e]+=n
    ans=[]
    exp.sort(reverse=True)
    for e in exp:
        if num[e] !=0:
            ans.append((num[e],e))
    return ans

def mult_poly(p1, p2):
    temp={}
    exp=[]
    for n,e in p1:
        for n1,e1 in p2:
            if e+e1 not in temp:
                temp[e+e1]=n*n1
                exp.append(e+e1)
            else:
                temp[e+e1]+=n*n1
    ans=[]
    exp.sort(reverse=True)
    for r in exp:   
        if temp[r] != 0:
            ans.append((temp[r],r))
    return ans

for i in range(3):
    exec(input().strip())