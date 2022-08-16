def factor(N):  
    i=2
    ans=[]
    while N!=1:
        c=0
        while N%i==0:
            c+=1
            N//=i
        if c!=0: ans.append([i,c])
        i+=1
    return ans

exec(input().strip())