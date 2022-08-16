Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n=input()
while n!='end':
    for i in range (len(n)):
        if n[i] in Alp:
            ind=(Alp.index(n[i])+13)%26
            n=n[:i]+Alp[ind]+n[i+1:]
        elif n[i] in alp:
            ind=(alp.index(n[i])+13)%26
            n=n[:i]+alp[ind]+n[i+1:]
    print(n)
    n=input()