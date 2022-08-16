zoo={}
animallist = []
text=input().split(', ')
while text[0]!='q':
    if text[1] not in animallist: animallist.append(text[1])
    if text[1] not in zoo:
        zoo[text[1]]=[text[0]]
    else:
        zoo[text[1]].append(text[0])
    text=input().split(', ')
for e in animallist:
    print(e+':',', '.join(zoo[e]))
    