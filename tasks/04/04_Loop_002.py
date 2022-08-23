d = input().split(" ")

d = [int(x) for x in d]

p = d[-1]
i = -1
j = 0
n = len(d)

while 1:
  if (j < n - 1):
    if (d[j] <= p):
      i += 1
      d[i], d[j] = d[j], d[i]
    j += 1
  else:
    break

d[i], d[-1] = d[-1], d[i]

print(d, i)