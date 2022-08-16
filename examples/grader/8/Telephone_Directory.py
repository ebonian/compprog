n=int(input())
book={}
for i in range (n):
    n,sn,tel=input().split()
    name=n+' '+sn
    book[name]=tel
    book[tel]=name
m=int(input())
for i in range (m):
    find=input()
    if find in book:
        print(find,'-->',book[find])
    else:
        print(find,'--> Not found')