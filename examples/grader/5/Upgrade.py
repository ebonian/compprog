chk='okay'
num=[]
grade=[]
grades=['F','D','D+','C','C+','B','B+','A']
while chk!='q':
    s=input().split()
    chk=s[0]
    if chk!='q':
        num+=[s[0]]
        grade+=[s[1]]
a=input().split()
c=0
for i in range (len(a)):
    for j in range(len(num)):
        if a[i]==num[j]:
            for k in range(7):
                if grade[j]==grades[k] and c==0:
                    c=1
                    grade[j]=grades[k+1]
    c=0
for i in range (len(num)):
    print(num[i],grade[i])