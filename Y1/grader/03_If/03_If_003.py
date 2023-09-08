# take the input of a b c d
a, b, c, d = [int(e) for e in input().split()]

# check for each condition by the flowchart
if (a > b):
  a, b = b, a
  
  if (d < a):
    c = c + a

  else:
    if (c > d):
      c = c - a

  b = a + c + d

else:
  if (c > a >= b):
    d = d + a
  
  if (d > c):
    b = b + 2

  else:
    b = 2 * b

# print the solution
print(a, b ,c ,d)