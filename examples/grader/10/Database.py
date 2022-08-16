f1=input()
f2=input()
f3=input()
course=open(f1,'r')
teacher=open(f2,'r')
data=open(f3,'r')
pair_c={}
pair_t={}
for e in course:
    a,b=e.strip().split(',')
    pair_c[a]=b
for e in teacher:
    a,b=e.strip().split(',')
    pair_t[a]=b
for e in data:
    a,b=e.strip().split(',')
    if a not in pair_c or b not in pair_t: print('record error')
    else:
        print(pair_c[a]+','+pair_t[b])