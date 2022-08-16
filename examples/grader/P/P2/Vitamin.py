n=int(input())
basket={}
fruit=[]
for i in range (n):
    item=input().split()
    basket[item[0]]=item[1:]
    fruit.append(item[0])
key=input().split()

if key[0] == 'show':
    for e in fruit:
        print(e,' '.join(basket[e]))
elif key[0] == 'get':
    if key[1] in basket:
        print(key[1],' '.join(basket[key[1]]))
    else:
        print(key[1],'not found')
elif key[0] == 'avg':
    i=int(key[1])-1
    print(round(sum([float(basket[e][i]) for e in basket])/n,4))
elif key[0] == 'max':
    i=int(key[1])-1
    a=[[-float(basket[e][i]),e] for e in basket]
    a.sort()
    print(a[0][1],-a[0][0])
elif key[0] == 'sort':
    i=int(key[1])-1
    a=[[float(basket[e][i]),e] for e in basket]
    a.sort()
    print(' '.join([e[1] for e in a]))