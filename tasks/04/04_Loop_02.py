a = float(input())

L = 0
U = a

while 1:
  x = (L + U)/ 2

  if (abs(a - 10 ** x) <= 10 ** -10 * max(a, 10 ** x)):
    print(round(x, 6))
    break

  if (10 ** x > a):
    U = x

  elif (10 ** x < a):
    L = x