date=input()
bdate=date.split("/")
d=bdate[0]
m=int(bdate[1])
y=bdate[2]
lst=["January","February","March","April","May","June","July","August","September","October","November","December"]
print(lst[m-1],d+",",y)