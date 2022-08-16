n=input()
m=len(n)
if m>=10:
    alp='B'
    num=n[:-10]
    if int(n[-9])>=5 and m!=10:
        num+=str(int(n[-10])+1)
    else:
        num+=n[-10]
        num+='.'
        if int((n[-8]))>=5 and m==10:
            num+=str(int(n[-9])+1)
        elif m==10:
            num+=n[-9]
        else:
            num=num[:-1]
elif m>=7:
    alp='M'
    num=n[:-7]
    if int(n[-6])>=5 and m!=7:
        num+=str(int(n[-7])+1)
    else:
        num+=n[-7]
        num+='.'
        if int((n[-5]))>=5 and m==7:
            num+=str(int(n[-6])+1)
        elif m==7:
            num+=n[-6]
        else:
            num=num[:-1]
elif m>=4:
    alp='K'
    num=n[:-4]
    if int(n[-3])>=5:
        num+=str(int(n[-4])+1)
    else:
        num+=n[-4]
        num+='.'
        if int((n[-2]))>=5 and m==4:
            num+=str(int(n[-3])+1)
        elif m==4:
            num+=n[-3]
        else:
            num=num[:-1]
else:
    num=n
    alp=''
print(num+alp)