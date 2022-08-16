text=input()
idx=int(input())
score=[0]*11
sm=0
game=1
count=0
for i in range (len(text)):
    if game!= 10:
        if text[i]=='X':
            count+=2
            score[game]+=10
            for j in range(1,3):
                if text[i+j]=='X':
                    score[game]+=10
                elif text[i+j]=='/':
                    score[game]+=(10-int(text[i+j-1]))
                else:
                    score[game]+=int(text[i+j])
        elif text[i]=='/':
            count+=1
            score[game]+= (10-int(text[i-1]))
            if text[i+1]=='X':
                score[game]+=10
            else:
                score[game]+=int(text[i+1])
        else:
            score[game]+=int(text[i])
            count+=1
    else:
        if text[i]=='X':
            score[game]+=10
        elif text[i]=='/':
            score[game]+=(10-int(text[i-1]))
        else:
            score[game]+=int(text[i])
    if count==2:
        game+=1
        count=0
for e in score:
    sm+=e
if 1<=idx<=10:
    print(score[idx])
else:
    print(sm)