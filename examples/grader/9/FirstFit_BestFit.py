def first_fit(L, e):
    for r in L:
        if sum(r)+e <= 100:
            r.append(e)
            return
    L.append([e])
    return

def best_fit(L, e):
    best=0
    mn=100
    for i in range(len(L)):
        if mn >= 100-sum(L[i]) >= e:
            mn=100-sum(L[i])
            best=i
    if mn==100: L.append([e])
    else:L[best].append(e)
    return

def partition_FF(D):
    new=[]
    for e in D:
        first_fit(new, e)
    return new

def partition_BF(D):
    new=[]
    for e in D:
        best_fit(new, e)
    return new

exec(input().strip())