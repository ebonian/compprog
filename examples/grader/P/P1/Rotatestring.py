key=input()
line=int(input())
text=input().strip()
text2=text
n=len(text)
run=True
for i in range (line-1):
    s=input().strip()
    if n != len(s):
        run=False
    text=s+text
    text2+=s
if run:
    if key=='90':
        for i in range(n):
            word=''
            for j in range(i,len(text),n):
                word+=text[j]
            print(word)
    elif key=='flip':
        text=text[::-1]
        for i in range (line):
            print(text[n*i:n*(i+1)])
    elif key=='180':
        text2=text2[::-1]
        for i in range (line):
            print(text2[n*i:n*(i+1)])
else:
    print("Invalid size")