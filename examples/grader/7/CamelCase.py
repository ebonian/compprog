Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text=input()
ans=''
first =True
for i in range (len(text)):
    if "0" <= text[i] <= "9" or text[i] in Alp or text[i] in alp:
        if first:
            if text[i] in Alp:
                ans+=alp[Alp.index(text[i])]
            else:
                ans+=text[i]
            if text[i+1] in alp or text[i+1] in Alp or  "0" <= text[i+1] <= "9" :
                first = True
            else:
                first = False
        else:
            if text[i] in alp and not (text[i-1] in alp or text[i-1] in Alp or  "0" <= text[i-1] <= "9"):
                ans+=Alp[alp.index(text[i])]
            elif text[i] in Alp and not (text[i-1] in alp or text[i-1] in Alp or  "0" <= text[i-1] <= "9"):
                ans+=i
            elif "0" <= text[i] <= "9" or text[i] in Alp or text[i] in alp:
                if text[i] in Alp:
                    ans+=alp[Alp.index(text[i])]
                else:
                    ans+=text[i]
print(ans)