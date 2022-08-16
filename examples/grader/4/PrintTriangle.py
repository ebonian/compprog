n=int(input())
for c in range(1,n+1):
    if c==n:
        print('*'*(2*n-1))
    elif c==1:
        print(' '*(n-1)+'*'+' '*(n-1))
    else:
        print(' '*(n-c)+'*'+' '*(2*(c-1)-1)+'*')