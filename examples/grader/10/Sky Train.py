direction={}
while True:
    text=input().split()
    if len(text)==1: break
    if text[0] not in direction:
        direction[text[0]]={text[1]}
    else:
        direction[text[0]].add(text[1])
    if text[1] not in direction:
        direction[text[1]]={text[0]}
    else:
        direction[text[1]].add(text[0])
if text[0] in direction:
    ans=direction[text[0]]
    for e in direction[text[0]]:
        ans=ans | direction[e]
    ans=list(ans)
    ans.sort()
    for e in ans:
        print(e)
else:
    print(text[0])