def readnext(f):
    line=f.readline()
    if len(line)==0:
        return '',''
    x=line.strip().split()
    return x[0],x[1]
n=input().strip().split()
f1=open(n[0],'r')
f2=open(n[1],'r')
id1,s1=readnext(f1)
id2,s2=readnext(f2)
while id1 !='' and id2 !='':
    if int(id1[-2:]) < int(id2[-2:]):
        print(id1,s1)
        id1,s1=readnext(f1)
    elif int(id1[-2:]) > int(id2[-2:]):
        print(id2,s2)
        id2,s2=readnext(f2)
    else:
        if int(id1)<int(id2):
            print(id1,s1)
            id1,s1=readnext(f1)
        else:
            print(id2,s2)
            id2,s2=readnext(f2)
while id1 != '':
    print(id1,s1)
    id1,s1=readnext(f1)
while id2 != '':
    print(id2,s2)
    id2,s2=readnext(f2)