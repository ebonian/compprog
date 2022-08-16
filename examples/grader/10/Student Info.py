n=int(input())
data={}
note=[]
found=False
for i in range (n):
    name,group,gen,major=input().split()
    data[name]=[group,gen,major]
    note.append(name)
search=set(input().split())
note.sort()
for e in note:
    if search <= set(data[e]):
        found=True
        print(e,' '.join(data[e]))
if not found:
    print('Not Found')
