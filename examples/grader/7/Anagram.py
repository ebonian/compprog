dig1=[0]*26
dig2=[0]*26
Alp=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
t1=input()
t2=input()
anagram = True
for i in t1:
    if i in alp:
        dig1[alp.index(i)]+=1
    elif i in Alp:
        dig1[Alp.index(i)]+=1
for i in t2:
    if i in alp:
        dig2[alp.index(i)]+=1
    elif i in Alp:
        dig2[Alp.index(i)]+=1
for i in range (26):
    if dig1[i] != dig2[i]:
        anagram = False
        break
if anagram:
    print("YES")
else:
    print("NO")