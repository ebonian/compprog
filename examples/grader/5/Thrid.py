n=int(input())
ans=[]
for i in range(n):
    x,y=[float(e) for e in input().split()]
    chk=x**2+y**2
    a=[chk,i+1,x,y]
    ans+=[a]
ans.sort()
print("#"+str(ans[2][1])+":","("+str(ans[2][2])+", "+str(ans[2][3])+")")