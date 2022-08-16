def is_odd(n):
    return n%2==1   

def has_odds(x):
    for e in x:
        if is_odd(e): return True
    return False

def all_odds(x):
    for e in x:
        if not is_odd(e): return False
    return True

def no_odds(x):
    for e in x:
        if is_odd(e): return False
    return True

def get_odds(x):
    ans=[]
    for e in x:
        if is_odd(e): ans.append(e)
    return ans

def zip_odds(a,b):
    a1=get_odds(a)
    b1=get_odds(b)
    n1=len(a1)
    n2=len(b1)
    new=[]
    for i in range(min(n1,n2)):
        new.append(a1[i])
        new.append(b1[i])
    if n1>n2:
        new+=a1[n2:]
    elif n1<n2:
        new+=b1[n1:]
    return new

exec(input().strip())