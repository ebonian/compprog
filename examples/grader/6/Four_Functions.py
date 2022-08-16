def make_int_list(x):
    a=[int(e) for e in x.split()]
    return a

def is_odd(e):
    if e%2==0:
        return False
    else:
        return True

def odd_list(alist):
    lst=[]
    for i in alist:
        if is_odd(i):
            lst.append(i)
    return lst

def sum_square(alist):
    sum=0
    for i in alist:
        sum+=i**2
    return sum

exec(input().strip())