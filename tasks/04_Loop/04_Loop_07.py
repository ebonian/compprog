a = float(input())

initial_a = a

L = 0
n = 0

while True:
  if a == 0:
    break

  else:
    a //= 10
    n += 1

U = n

while True:
  x = (L + U)/ 2

  if (abs(initial_a - 10 ** x) <= 10 ** -10 * max(initial_a, 10 ** x)):
    print(round(x, 6))
    break

  if (10 ** x > initial_a):
    U = x

  elif (10 ** x < initial_a):
    L = x