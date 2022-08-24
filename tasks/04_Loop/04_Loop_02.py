# take the float input of a
a = float(input())

# assisgn L, U variable as given in desc
L = 0
U = a

while (True):
  # the middle point of [L, U]
  x = (L + U)/ 2

  # if 10^x is close to a enough then print the result and break out the loop
  if (abs(a - 10 ** x) <= 10 ** -10 * max(a, 10 ** x)):
    print(round(x, 6))
    break

  # if 10^x more than a then replace U value with x and loop it over again
  if (10 ** x > a):
    U = x

  # if 10^x less than a then replace L value with x and loop it over again
  elif (10 ** x < a):
    L = x