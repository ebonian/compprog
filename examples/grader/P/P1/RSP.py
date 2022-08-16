m=int(input())
boo=True
winner=""
s1,s2,c=0,0,0
while(boo):
    play=input().split()
    c+=1
    if c==3*m:
        boo=False
        winner="Tie"
    if play[0]=="R" and play[1]=="S":
        s1+=1
        if s1==m:
            boo=False
            winner="Player 1 wins"
    elif play[0]=="S" and play[1]=="P":
        s1+=1
        if s1==m:
            boo=False
            winner="Player 1 wins"
    elif play[0]=="P" and play[1]=="R":
        s1+=1
        if s1==m:
            boo=False
            winner="Player 1 wins"
    elif play[0]=="R" and play[1]=="P":
        s2+=1
        if s2==m:
            boo=False
            winner="Player 2 wins"
    elif play[0]=="P" and play[1]=="S":
        s2+=1
        if s2==m:
            boo=False
            winner="Player 2 wins"
    elif play[0]=="S" and play[1]=="R":
        s2+=1
        if s2==m:
            boo=False
            winner="Player 2 wins"
print(s1,s2)
print(winner)    
