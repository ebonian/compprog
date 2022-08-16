n=int(input())
book={}
for i in range (n):
    name=input()
    text=input()
    book[name]=text
while True:
    find=input()
    if find =='-1': break
    score_book=[]
    for e in book:
        chk=book[e].split()
        temp=set(chk)
        a=chk.count(find)
        b=len(chk)
        c=len(temp)
        score=a/(b*c)
        score_book.append([-score,e])
    score_book.sort()
    if score_book[0][0] != 0:
        print(score_book[0][1])
    else:
        print('NOT FOUND')
