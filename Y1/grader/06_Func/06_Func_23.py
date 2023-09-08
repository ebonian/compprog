def make_int_list(x):
  x = x.split()
  x = [int(n) for n in x]

  return x

def is_odd(e):
  if (e % 2 == 0):
    return False
  else:
    return True

def odd_list(alist):
  odd_list = []

  for number in alist:
    if (number % 2 != 0):
      odd_list.append(number)

  return odd_list

def sum_square(alist):
  for i in range(len(alist)):
    alist[i] = alist[i] * alist[i]

  return sum(alist)

# print(sum_square([1, 1, 2 ,3]))

exec(input().strip())