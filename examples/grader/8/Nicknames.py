n=int(input())
album={}
for i in range (n):
    name,nick=input().split()
    album[name]=nick
    album[nick]=name
m=int(input())
for i in range (m):
    ask=input()
    if ask in album:
        print(album[ask])
    else:
        print("Not found")
