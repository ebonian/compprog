def spiral_square(n): # n is a positive odd number
    up=1
    num=[0]*n**2
    start=(n**2)//2
    num[start]=1
    i=0
    c=2
    while i < n//2:
        for j in range (1):
            start+=1
            num[start]=c
            c+=1
        for j in range (i*2+1):
            start-=n
            num[start]=c
            c+=1
        for j in range (i*2+2):
            start-=1
            num[start]=c
            c+=1
        for j in range (i*2+1):
            start+=n
            num[start]=c
            c+=1
        start+=n
        num[start]=c
        c+=1
        for j in range (i*2+2):
            start+=1
            num[start]=c
            c+=1
        i+=1
    new=[]
    for i in range (0,len(num),n):
        new.append(num[i:i+n])
    return new

def print_square(S):
# เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())
