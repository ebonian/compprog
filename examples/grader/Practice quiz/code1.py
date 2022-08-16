n=int(input("Number of customer: "))
order=[]
pizza={'P01': 265.3,'P02':246.9,'P03':256.9,'P04':272.5,'P05':309.3}
for i in range (1,n+1):
    print('Customer: ',i)
    text=input().split(',')
    name=text[0]
    orders=text[1:]
    total_cal=0
    for i in range (0,len(orders),2):
        menu=orders[i]
        amount=orders[i+1]
        cal=pizza[menu]*int(amount)
        total_cal+=cal
    if total_cal%1 != 0:
        total_cal = total_cal//1+1
    order.append((name,int(total_cal)))
temp=sorted(order,key=lambda x: x[1])
after1=[[e[1],e[0]] for e in temp]
after1.sort()
after=[(e[1],e[0]) for e in after1]
print('Before ascending sort')
print(order)
print('After ascending sort')
print(after)