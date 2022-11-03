d = input().split(" ")

# convert list of string to list of int
d = [int(x) for x in d]

p = d[-1]
i = -1
j = 0
n = len(d)

while (True):
  if (d[j] <= p):
    i += 1
    d[i], d[j] = d[j], d[i]

  j+=1

  if (j>=n):
    break

print(d)