fname=input().strip()
k=int(input())
ruler=''
for i in range(k//10):
    ruler += '-'*9 + str(i+1)
ruler+='-'*(k%10)
print(ruler)
fdata=open(fname,'r')
out=''
c=0
for line in fdata:
    word=line.strip().split('.')
    for e in word:
        if c+len(e)<=k:
            out+=e+'.'
            c+=len(e)+1
        elif len(e)>k:
            out=out.strip('.')+'\n'+e+'\n'
            c=0
        elif e!='':
            out=out.strip('.')+'\n'+e+'.'
            c=len(e)+1
print(out.strip('.').strip())