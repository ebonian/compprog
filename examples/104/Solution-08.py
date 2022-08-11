# Prog-08: Bag-of-words
# Knight N104
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def fhash(x,y):
    a=0
    for i in range(len(x)):
        a+=ord(x[i])*37**i
    return a%y
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
file_name=input('File name = ')
f1=open(file_name,'r',encoding='utf-8')
sw=open('stopwords.txt','r')
swl=[]
for line in sw:
    swl+=line.strip().split()
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
while True:
    use=input('Use feature hashing ? (y,Y,n,N) ')
    if use in'yYnN' and use!='':
        break
    else:
        print('Try again.')
cc,ac,l,wc,a4w=0,0,[],0,[]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
for line in f1:
    cc+=len(line)-int(line[-1]=='\n')
    l.append(line)
    s,re='',''
    for i in line:
        if i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ':
            re+=i.lower()
        else:
            re+=' '
    ac+=len(''.join(re.split()))
    wc+=len(re.split())
    a4w+=[m for m in re.split() if m not in swl]
for i in range(len(l)):
    if l[-1]=='\n':
        l=l[:-1]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
L1=[]
L2=[]
if use in 'yY':
    M=int(input('M = '))
    for i in a4w:
        if fhash(i,M) not in L1:
            L1.append(fhash(i,M))
            L2+=[1]
        else:
            L2[L1.index(fhash(i,M))]+=1
else:
    for i in a4w:
        if i not in L1:
            L1.append(i)
            L2+=[1]
        else:
            L2[L1.index(i)]+=1
BoW=[[L1[i],L2[i]] for i in range(len(L1))]
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
print('-'*19)
print('char count =',cc)
print('alphanumeric count =',ac)
print('line count =',len(l))
print('word count =',wc)
print('BoW =',sorted(BoW))
f1.close()
sw.close()
