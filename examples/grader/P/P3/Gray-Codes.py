n=int(input())
k=int(input())
n_error=False
k_error=False
if n < 0:
    n_error=True
if k > 100 or k < 0:
    k_error=True
if n_error and k_error:
    print('Invalid n and k')
elif n_error:
    print('Invalid n')
elif k_error:
    print('Invalid k')
else:
    out=''
    m=n+1
    for i in range (1,k+1):
        if i==k: m=n
        out+=(str(i) +'-'*m)[:m]
    print(out)
    num=['0','1']
    for i in range (1,n):
        num+=num[::-1]
        len_num=len(num)
        num=['0'+num[i] for i in range(0,len_num//2)]+['1'+num[i] for i in range(len_num//2,len_num)]
    for i in range (0,len(num),k):
        print(','.join(num[i:i+k]))