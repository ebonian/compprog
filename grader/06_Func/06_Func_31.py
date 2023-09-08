month_name = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
zodiac_name = ["Capricorn", "Aquarius", "Pisces", "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo", "Libra", "Scorpio", "Sagittarius"]

def read_date():
  day, month, year = input().split()

  day = int(day)
  month = month_name.index(month[:3]) + 1
  year = int(year)

  return [day, month, year]

def zodiac(d, m):
  for i in range(1, 13):
    if (d >= (21 if m == 1 or m == 2 else 22) and m == i):
      return zodiac_name[i]
    elif (d <= (20 if m == 1 or m == 2 else 21) and m == i):
      return zodiac_name[i - 1]

def days_in_feb(y):
  days_in_feb = 28

  if (y % 400 == 0 or y % 100 != 0 and y % 4 == 0):
    days_in_feb = 29

  return days_in_feb

def days_in_month(m, y):
  days_in_month = 31

  if (m == 4 or m == 6 or m == 9 or m == 11):
    days_in_month = 30
  elif (m == 2):
    days_in_month = days_in_feb(y)

  return days_in_month

def days_in_between(d1, m1, y1, d2, m2, y2):
  days = 0

  for i in range(2, 13):
    if (m1 < i):
      days += days_in_month(i, y1)
  
  for i in range(1, 12):
    if (m2 > i):
      days += days_in_month(i, y2)

  days += (days_in_month(m1, y1) - d1 + 1) + int((y2 - y1 - 1) * 365.25) + (d2 - 1)

  return days

def main():
  d1, m1, y1 = read_date()
  d2, m2, y2 = read_date()

  print(zodiac(d1, m1), zodiac(d2, m2))
  print(days_in_between(d1, m1, y1, d2, m2, y2))

exec(input().strip())