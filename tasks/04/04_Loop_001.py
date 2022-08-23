p = float(input())

k = 1
t = 1

loop = True

while (loop):
  t = t*(365 - (k - 1)) / 365
  if (1 - t >= p):
    loop = False
  else :
    k += 1

print(k)