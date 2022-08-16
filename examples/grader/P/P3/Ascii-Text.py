fname=input().strip()
key=input().strip()
if key not in ['LSTRIP','RSTRIP','STRIP','STRIP_ALL']:
    print('Invalid command')
    exit(0)
out=[]
l_margin=10000
r_margin=-10000
fdata=open(fname,'r')
for line in fdata:
    line=line.strip()
    cl=0
    cr=0
    for e in line:                  #check left margin
        if e=='.':cl+=1
        else: break
    if cl < l_margin: l_margin=cl 
    for e in line[::-1]:            #check right margin
        if e=='.':cr+=1
        else: break
    if -cr > r_margin: r_margin = -cr
    
    out.append(line)
fdata.close()
if key=='LSTRIP':
    for e in out:
        print(e[l_margin:])
elif key=='RSTRIP':
    for e in out:
        print(e[:r_margin])
elif key=='STRIP':
    for e in out:
        print(e[l_margin:r_margin])
elif key=='STRIP_ALL':
    n=len(out)
    chk_dot=[]
    for i in range (len(out)):
        out[i]=out[i][l_margin:r_margin]
        temp=[False]*len(out[i])
        for j in range (len(out[i])):
            if out[i][j] == '.':
                temp[j]=True
        chk_dot.append(temp)
    cut=[]
    for i in range (len(chk_dot[i])):
        sym=True
        for j in range (n):
            sym = sym and chk_dot[j][i]
        cut.append(sym)
    for e in out:
        out_text=''
        for i in range (len(e)):
            if not cut[i]:
                out_text+=e[i]
        print(out_text)
            