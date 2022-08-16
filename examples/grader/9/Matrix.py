def read_matrix():
    m=[]
    nrows=int(input())
    for k in range(nrows):
        m.append([float(e) for e in input().split()])
    return m

def mult_c(c,A):    
    return [[r*c for r in e] for e in A]

def mult(A,B):
    C=[]
    for i in range(len(A)):
        temp=[]
        for j in range(len(B[0])):
            sum=0
            for k in range(len(A[0])):
                sum+=A[i][k]*B[k][j]
            temp.append(sum)
        C.append(temp)
    return C

exec(input().strip())