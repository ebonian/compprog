n=int(input())
menu={}
for i in range(n):
    name, price = input().split()
    menu[name] = float(price)

m = int(input())
notsales = True
outcome = 0
count = {}

for i in range(m):
    name, num = input().split()
    if name in menu:
        notsales = False
        outcome += menu[name] * int(num)
        if name in count:
            count[name] += menu[name]*int(num)
        else:
            count[name] = menu[name]*int(num)

if notsales:
    print("No ice cream sales")
else:
    sort_count = sorted(count.items(), key=lambda x:x[1], reverse=True)
    mx = sort_count[0][1]
    popular = []
    for i in sort_count:
        if mx == i[1]:
            popular.append(i[0])
        else:
            break

    popular.sort()
    popular=", ".join(popular)
    
    print("Total ice cream sales:", outcome)
    print("Top sales:",popular)