# take the input line by line of a b c d and e
a = input()
b = input()
c = input()
d = input()
e = input()

# follow the flowchart and check for each condition
if (a > b):
  a, b = b, a

if (c > d):
  c, d = d, c

if (a > c):
  b, d = d, b
  c = a

a = e

if (a > b):
  a, b = b ,a

if (c > a):
  b, d = d, b
  a = c

# print out the result
if (a > d):
  print(d)
else:
  print(a)