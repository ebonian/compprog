n=int(input())
for i in range(n):
    text=input()
    for j in range(len(text)):
        if text[j] != '.': break
    j=(j+1)//2
    print(text[j:])