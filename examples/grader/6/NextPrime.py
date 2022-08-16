def is_prime(n):
    if n <= 1:
        return False
    for k in range(2,int(n**0.5)+1):
        if n%k == 0:
            return False
    return True
def next_prime(N):
    i = N+1
    while not is_prime(i):
        i+=1
    return i
def next_twin_prime(N):
    i = N
    while True :
        k = next_prime(i)
        q = next_prime(k)
        if q-k == 2 :
            c = '('+str(k)+', '+str(q)+')'
            return c
        else :
            i = k

exec(input().strip())