h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
if s2<s1:
  m1+=1
if m2<m1:
  h1+=1
dh=(h2-h1)%24
dm=(m2-m1)%60
ds=(s2-s1)%60
print(str(dh)+":"+str(dm)+":"+str(ds))