import math
from datetime import datetime

bd, bm, by, d, m, y = [int(e) for e in input().split()]

by -= 543
y -= 543


bDate = datetime(by, bm, bd)
date = datetime(y, m, d)

dateDiff = date - bDate
print(dateDiff.days)

p = math.sin((2 * math.pi * dateDiff.days) / (23))
e = math.sin((2 * math.pi * dateDiff.days) / (28))
i = math.sin((2 * math.pi * dateDiff.days) / (33))

print(dateDiff.days, "{:.2f}".format(p), "{:.2f}".format(e), "{:.2f}".format(i))