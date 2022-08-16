key=input()
if key=="str2RLE":
    sen=input()
    check=sen[0]
    c=0
    ans=''
    for i in range(0,len(sen)):
        if sen[i]!=check:
            ans+=check+" "+str(c)+" "
            check=sen[i]
            c=1
        else:
            c+=1
    print(ans+check,c)
elif key=="RLE2str":
    sen=input().split()
    new=''
    for i in range(0,len(sen),2):
        new+=sen[i]*int(sen[i+1])
    print(new)
else:
    print("Error")
