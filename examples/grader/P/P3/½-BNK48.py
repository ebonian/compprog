idol_votes={}
ota_count={}
kami_ota={}
all_idol=set()
text=input().split()
while text[0] not in ['1','2','3']:
    ota,idol,amount=text
    all_idol.add(idol)
    if ota not in kami_ota:
        kami_ota[ota] = {}
    if idol not in kami_ota[ota]:
        kami_ota[ota][idol] = int(amount)
    else:
        kami_ota[ota][idol] += int(amount)
    if idol not in idol_votes:
        idol_votes[idol] = int(amount)
        ota_count[idol] = {ota}
    else:
        idol_votes[idol] += int(amount)
        ota_count[idol].add(ota)
    text=input().split()
if text[0] == '1':
    temp=sorted(idol_votes.items(),key=lambda x: x[1],reverse= True)
    win=[]
    for e in temp:
        win.append((-e[1],e[0]))
    win.sort()
    winner=win[0][1]+', '+win[1][1]+', '+win[2][1]
    #print(win)
    print(winner)
elif text[0] == '2':
    win=[]
    for e in ota_count:
        win.append([-len(ota_count[e]),e])
    win.sort()
    winner=win[0][1]+', '+win[1][1]+', '+win[2][1]
    print(winner)
elif text[0] == '3':
    count_kami={}
    for e in all_idol:
        count_kami[e]=0
    for e in kami_ota:
        temp=sorted(kami_ota[e].items(),key=lambda x: x[1],reverse= True)
        temp2=[]
        for f in temp:
            temp2.append((-f[1],f[0]))
        temp2.sort()
        count_kami[temp2[0][1]]+=1
    temp=sorted(count_kami.items(),key=lambda x:x[1],reverse= True)
    win=[]
    for e in temp:
        win.append((-e[1],e[0]))
    win.sort()
    winner=win[0][1]+', '+win[1][1]+', '+win[2][1]
    #print(win)
    print(winner)