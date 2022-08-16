n=int(input())
item_number={}
inbidding={}
allitem=[]
everyone=[]
i=0
while i<n:
    text = input().split()
    key = text[0] # should be 'B' or 'W'
    bidder = text[1] # bidder
    item = text[2] # item number
    if key == 'B': 
        i+=1
        price = int(text[3]) # should be int of price
        if bidder not in everyone:
            everyone.append(bidder)
        if item not in item_number:
            item_number[item]=[(price,bidder)]
            inbidding[item]=[bidder]
            allitem.append(item)
        else:
            if bidder in inbidding[item] :
                idx = inbidding[item].index(bidder)
                inbidding[item].remove(bidder)
                item_number[item].pop(idx)
            inbidding[item].append(bidder)
            item_number[item].append((price,bidder))
    elif key == 'W':
        i+=1
        if item in item_number:
            if bidder in inbidding[item]:
                idx = inbidding[item].index(bidder)
                inbidding[item].remove(bidder)
                if len(inbidding[item])==0:
                    inbidding.pop(item)
                item_number[item].pop(idx)
                if len(item_number[item])==0:
                    item_number.pop(item)
                    allitem.remove(item)
        else:
            i-=1
winner={}
allitem.sort()
for e in allitem:
    temp=[]
    item_number[e].sort(reverse = True)
    chk=item_number[e][0][0]
    for money,person in item_number[e]:
        if money == chk:
            temp.append((inbidding[e].index(person),person,money))
    print(temp,chk,e,item_number[e])
    temp.sort()
    first,man,using=temp[0]
    if man not in winner:
        winner[man]=[using,e]
    else:
        winner[man][0]+=using
        winner[man][1]+=' '+e
    '''
    if item_number[e][0][1] not in winner:
        winner[item_number[e][0][1]]=[item_number[e][0][0],e]
    else:
        winner[item_number[e][0][1]][0]+=item_number[e][0][0]
        winner[item_number[e][0][1]][1]+=' '+e
    '''
everyone.sort()
for e in everyone:
    if e in winner:
        print(e+': $'+str(winner[e][0]),'->',winner[e][1])
    else:
        print(e+': $0')
