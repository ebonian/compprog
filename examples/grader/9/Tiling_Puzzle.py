def row_number(t,e):
    for i in range(len(t)):
        if e in t[i]:
            return i

def flatten(t):
    return [e for r in t for e in r if e!=0]

def inversions(x):
    c=0
    for i in range(len(x)-1):
        for j in range(i+1,len(x)):
            if x[i]>x[j]: c+=1
    return c

def solvable(t):
    nrows=len(t)
    if nrows%2==1:
        return inversions(flatten(t))%2==0
    else:
        if inversions(flatten(t))%2==1:
            return row_number(t,0)%2==0
        else:
            return row_number(t,0)%2==1

exec(input().strip())