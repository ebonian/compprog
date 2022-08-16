num=int(input())
q=[]
w=[]
c2=0
na=0
total=0
for i in range (num):
    sen=input().split()
    if sen[0]=='reset':
        n=int(sen[1])
    elif sen[0]=='new':
        print("ticket",n)
        q+=[n]+[int(sen[1])]
        w+=[n]
        n+=1
    elif sen[0]=='next':
        print("call",w[c2])
        c2+=1
    elif sen[0]=='order':
        print("qtime",q[(c2-1)*2],int(sen[1])-q[(c2-1)*2+1])
        total+=int(sen[1])-q[(c2-1)*2+1]
        na+=1
    elif sen[0]=='avg_qtime':
        print("avg_qtime",total/na)
