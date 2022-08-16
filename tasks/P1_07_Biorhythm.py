import math

mDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

bd, bm, by, d, m, y = [int(e) for e in input().split()]

by -= 543
y -= 543

# check if by is leap year
if (by%4==0 and by%100!=0 or by%400==0):
  mDay[1] = 29

red = mDay[bm - 1] - bd + 1 + sum(mDay[bm:])

# reset
mDay[1] = 28

black = 365 * (y - by - 1)

# check if y is leap year
if (y%4==0 and y%100!=0 or y%400==0):
  mDay[1] = 29

blue = sum(mDay[:m - 1]) + d - 1

# reset
mDay[1] = 28

dateDiff = red + black + blue

p = math.sin((2 * math.pi * dateDiff) / (23))
e = math.sin((2 * math.pi * dateDiff) / (28))
i = math.sin((2 * math.pi * dateDiff) / (33))

print(dateDiff, "{:.2f}".format(p), "{:.2f}".format(e), "{:.2f}".format(i))