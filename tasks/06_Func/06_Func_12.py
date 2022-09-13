def is_prime(n):
  if n<= 1:
    return False

  for k in range(2, int(n**0.5) + 1):
    if n % k == 0:
      return False

  return True


def next_prime(n):
  if (is_prime(n)):
    n += 1

  while (not is_prime(n)):
    n += 1

  return n


def next_twin_prime(n):  
  if (is_prime(n)):
    n += 1
  while (True):

    past = n

    while (not is_prime(past)):
      past += 1


    n = past + 1



    while (not is_prime(n)):
      n += 1

    if (abs(n - past) == 2):
      return past, n

exec(input().strip())