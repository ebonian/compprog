score={'X':0,'R':1,'Y':2,'G':3,'W':4,'B':5,'P':6,'K':7}
p1=0
p2=0
playing = True
while playing:
    play=input()
    if play[1]=='K': playing = False
    if play[0]=='1':
        p1+=score[play[1]]
        if play[1]=='R':
            p1+=score[play[2]]
    elif play[0]=='2':
        p2+=score[play[1]]
        if play[1]=='R':
            p2+=score[play[2]]
print(p1,p2)
if p1>p2:
    print('Player 1 wins')
elif p1<p2:
    print('Player 2 wins')
else:
    print('Tie')
