import math

# take the input of birthdate and date for calculation
bd, bm, by, d, m, y = [int(e) for e in input().split()]

# change from BE to AD year
by -= 543
y -= 543

# assign amount of days for each month
days_of_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# define function to check leap year
def isLeapYear(year: int) -> bool:
  if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0): return True
  else: return False

# check if by is leap year
if (isLeapYear(by)): days_of_month[1] = 29

# calculate the red period
red_period = days_of_month[bm - 1] - bd + 1 + sum(days_of_month[bm:])

# reset feb days
days_of_month[1] = 28

# calculate the black period
black_period = 365 * (y - by - 1)

# check if y is leap year
if (isLeapYear(y)): days_of_month[1] = 29

# calculate the blue period
blue_period = sum(days_of_month[:m - 1]) + d - 1

# reset feb days
days_of_month[1] = 28

# sum all period to get the number of days since birth
days_difference = red_period + black_period + blue_period

# calculate each biorhythm
physical = math.sin((2 * math.pi * days_difference) / (23))
emotional = math.sin((2 * math.pi * days_difference) / (28))
intellectual = math.sin((2 * math.pi * days_difference) / (33))

# print out the solution
print(days_difference, "{:.2f}".format(physical), "{:.2f}".format(emotional), "{:.2f}".format(intellectual))