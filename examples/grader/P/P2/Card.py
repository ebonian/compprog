def keys(pairs):
    card_num=('','A','2','3','4','5','6','7','8','9','T','J','Q','K')
    color_num=('','C','D','H','S')
    card1=pairs[:2]
    card2=pairs[2:]
    pow1=card_num.index(card1[0])
    pow2=card_num.index(card2[0])
    if pow1==pow2:
        return color_num.index(card1[1])-color_num.index(card2[1])
    else:
        return pow1-pow2

deck=input()
ans=''
for i in range (0,len(deck)-3,2):
    temp=keys(deck[i:i+4])
    if temp<=0:
        ans+=str(temp)
    else:
        ans+='+'+str(temp)
print(ans)