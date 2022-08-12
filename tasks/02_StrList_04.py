# take the input of int m and n
m = int(input())
n = int(input())

# convert m to str
m = str(m)

# check if length of digits m >= n
if (len(m) >= n):
  # print the result
  print(m)
else:
  # add 0 to the start of m til m digit length is equal to n
  while (len(m) != n):
    m = "0" + m
  # print the result
  print(m)