text1=input()
text2=input()
c_word1={}
c_word2={}
alp=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
rev1=[]
rev2=[]
for e in alp:
    c_word1[e]=0
    c_word2[e]=0
for e in text1.lower():
    if 'a' <= e <= 'z':
        c_word1[e]+=1
for e in text2.lower():
    if 'a' <= e <= 'z':
        c_word2[e]+=1
for e in alp:
    diff=c_word1[e]-c_word2[e]
    if diff>0:
        if diff==1:
            rev1.append(str(diff)+' '+e)
        else:
            rev1.append(str(diff)+' '+e+"'s")
    elif diff<0:
        diff*=-1
        if diff==1:
            rev2.append(str(diff)+' '+e)
        else:
            rev2.append(str(diff)+' '+e+"'s")
print(text1)
if len(rev1)==0:
    print(' - None')
else:
    for e in rev1:
        print(' - remove',e)
print(text2)
if len(rev2)==0:
    print(' - None')
else:
    for e in rev2:
        print(' - remove',e)