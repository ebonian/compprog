from datetime import datetime

d = int(input())
m = int(input())
y = int(input())

day_of_year = datetime(y-543, m, d).timetuple().tm_yday
print(day_of_year)