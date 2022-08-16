def leap_years(y):
    y-=543
    if y%400==0 or (y%4==0 and y%100!=0):
        return 29
    return 28

def days_of_months(y,m):
    if m in {4,6,9,11}:
        return 30
    elif m==2:
        return leap_years(y)
    return 31

good={}
bad=[]
while True:
    x=input().split()
    if x[0]=='END': break
    id_item=x[0]
    type_delivery=x[1]
    date,month,year=[int(e) for e in x[-3:]]
    if year < 2558: bad.append(' '.join(x)+' --> Invalid year')
    elif month < 1 or month > 12: bad.append(' '.join(x)+' --> Invalid month')
    elif date < 1 or date > days_of_months(year,month): bad.append(' '.join(x)+' --> Invalid date')
    elif type_delivery not in {'E','Q','N','F'}: bad.append(' '.join(x)+' --> Invalid delivery type')
    else: 
        deli_type={'E':1,'Q':3,'N':7,'F':14}
        if date + deli_type[type_delivery] > days_of_months(year,month):
            if month+1>12:
                date += deli_type[type_delivery] - days_of_months(year,month)
                year+=1
                month=1
            else: 
                date = date + deli_type[type_delivery]-days_of_months(year,month)
                month+=1
        else:
            date+= deli_type[type_delivery]
        good[id_item]=[[year,month,date,int(id_item)],str(date)+'/'+str(month)+'/'+str(year)]
num=sorted(good.items(),key= lambda x:x[1][0])
for e in bad:
    print("Error:",e)
for e in num:
    print(e[0]+': delivered on',e[1][1])