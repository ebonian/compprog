mname = ['',"Jan", "Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
def read_date():
    date=input().split()
    date[0]=int(date[0])
    date[1]=mname.index(date[1][:3])
    date[2]=int(date[2])
    return date

def zodiac(d1,m1):
    if d1 >= 22 and m1==3 or d1 <=21 and m1==4 : z1 = "Aries"
    elif d1 >= 22 and m1==4 or d1 <=21 and m1==5 : z1 = "Taurus"
    elif d1 >= 22 and m1==5 or d1 <=21 and m1==6 : z1 = "Gemini"
    elif d1 >= 22 and m1==6 or d1 <=21 and m1==7 : z1 = "Cancer"
    elif d1 >= 22 and m1==7 or d1 <=21 and m1==8 : z1 = "Leo"
    elif d1 >= 22 and m1==8 or d1 <=21 and m1==9 : z1 = "Virgo"
    elif d1 >= 22 and m1==9 or d1 <=21 and m1==10 : z1 = "Libra"
    elif d1 >= 22 and m1==10 or d1 <=21 and m1==11 : z1 = "Scorpio"
    elif d1 >= 22 and m1==11 or d1 <=21 and m1==12 : z1 = "Sagittarius"
    elif d1 >= 22 and m1==12 or d1 <=20 and m1==1 : z1 = "Capricorn"
    elif d1 >= 21 and m1==1 or d1 <=20 and m1==2 : z1 = "Aquarius"
    elif d1 >= 21 and m1==2 or d1 <=21 and m1==3 : z1 = "Pisces"
    return z1

def days_in_feb(y):
    if y%4==0 and y%100!=0 or y%400==0:
        return 29
    else:
        return 28

def days_in_month(m,y):
    day= 31
    if m==4 or m==6 or m==9 or m==11 :
        day= 30
    elif m==2 :
        day= days_in_feb(y)
    return day

def days_in_between(d1,m1,y1,d2,m2,y2):
    lst=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    sum=0
    for i in range(m1,13):
        sum+=lst[i]
        if (y1%4==0 and y1%100!=0 or y1%400==0 )and i == 2:
            sum+=1
    sum-=d1-1
    sum+=(y2-y1-1)*365.25
    for i in range(1,m2):
        sum+=lst[i]
        if y2%4==0 and y2%100!=0 or y2%400==0 and i == 2:
            sum+=1
    sum+=d2-1
    return int(sum)

def main() :
    d1,m1,y1 = read_date()
    d2,m2,y2 = read_date()
    text=zodiac(d1,m1)+' '+zodiac(d2,m2)
    print(text)
    print(days_in_between(d1,m1,y1,d2,m2,y2))

exec(input().strip())
