# [Solution #1]
# use list
# 
# take the input of date month and year
day = int(input())
month = int(input())
year = int(input())

# change from BE to AD year
year -= 543

# assign amount of days for each month
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# check if y is leap year
if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0): days_of_month[1] = 29

# sum up days of month addition with d
days = sum(days_of_month[0:month - 1]) + day

# print the result
print(days)





# [Solution #2]
# use for loop
# 
# d = int(input())
# m = int(input())
# y = int(input())
#
# y -= 543
#
# days = d
#
# for i in range(m):
#   n = 31
#   month = i + 1
#
#   if (month != m):
#     if (month == 4 or month == 6 or month == 9 or month == 11):
#       n = 30
#     else:
#       if (month == 2):
#         n = 28
#       if (month == 2 and y%4==0 and y%100!=0 or y%400==0):
#         n = 29
#
#     days += n
#
# print(days)





# [Solution #3]
# with datetime module
# 
# from datetime import datetime
# days = datetime(y, m, d).timetuple().tm_yday
# print(days)