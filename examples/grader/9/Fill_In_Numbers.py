def pattern1(nrows,ncols):
    return [[j+ncols*i for j in range(1,ncols+1)] for i in range(nrows)]

def pattern2(nrows,ncols):
    return [[i+nrows*(j-1)+1 for j in range(1,ncols+1)] for i in range(nrows)]

def pattern3(N):
    c=1
    ans=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            if j<i: temp.append(0)
            else:
                temp.append(c)
                c+=1
        ans.append(temp)
    return ans

def pattern4(N):
    c=1
    ans=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            if j<i: temp.append(0)
            elif i==0:
                temp.append((c*(c+1))//2)
                c+=1
            else:
                temp.append(ans[i-1][j-1]+j)                
        ans.append(temp)
    return ans

def pattern5(N):
    c=N
    ans=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            if j<i: temp.append(0)
            elif i==0:
                if j!=0:
                    temp.append(temp[j-1]+c)
                    c-=1
                else: temp.append(1)                
            else:
                temp.append(ans[i-1][j-1]+1)                
        ans.append(temp)
    return ans

def pattern6(N):
    c=N
    ans=[]
    for i in range(N):
        temp=[]
        for j in range(N):
            if j<i: temp.append(0)
            elif i==0:
                if j==0:
                    temp.append(1)
                elif j%2==0:
                    temp.append(temp[j-1]+1)
                else:
                    temp.append(temp[j-1]+(2*(N-j)))                
            else:
                if j%2==1:
                    if i%2==1: temp.append(ans[i-1][j-1]+1)
                    else: temp.append(ans[i-1][j-1]-1)
                else:
                    if i%2==0: temp.append(ans[i-1][j-1]+1)
                    else: temp.append(ans[i-1][j-1]-1)              
        ans.append(temp)
    return ans

exec(input().strip())