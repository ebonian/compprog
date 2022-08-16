n=int(input())
member=input().split()
table=[member[i:i+n] for i in range (0,len(member),n)]
for i in range (n-1):
    for j in range (n-1):
        number=set()
        mem=[]
        for row in range (i,i+2):
            for col in range (j,j+2):
                if table[row][col] == 'x': 
                    mem.append((row,col))
                else: number.add(int(table[row][col]))
        add=sum(number)//len(number)
        for x,y in mem:
            table[x][y]=str(add)
for i in range(n):
    print(' '.join(table[i]))