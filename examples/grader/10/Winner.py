n=int(input())
win=set()
lose=set()
for i in range (n):
    a,b=input().split()
    win.add(a)
    lose.add(b)
print(sorted(win-lose))