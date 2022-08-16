def max(x):
    max=x[0]
    for i in x[1:]:
        if i > max:
            max=i
    return max

def min(x):
    min=x[0]
    for i in x[1:]:
        if i < min:
            min=i
    return min

def mean(x):
    sum=0
    for i in x:
        sum+=i
    return sum/len(x)

name,y=input().split()
fin = open (name,"r")
score=[]
y=y[-2:]
for line in fin:
    id,scores=line.split()
    if id[:2]==y:
        score.append(float(scores))
if score==[]:
    print("No data")
else:
    print(min(score),max(score),mean(score))