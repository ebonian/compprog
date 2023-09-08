# take the float input of p
p = float(input())

# follow the flowchart
k = 1
t = 1

while (True):
  t = t*(365 - (k - 1)) / 365
  
  if (1 - t >= p):
    break

  else :
    k += 1

# print the result
print(k)