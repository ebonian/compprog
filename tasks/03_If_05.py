# take the input of int
i = int(input())

# check int for each condition start with + - or 0
if (i == 0):
  print("zero")
  print("even")

# if positive
elif (i > 0):
  print("positive")

  # check is it even or odd
  if (i % 2 == 0):
    print("even")
  else:
    print("odd")

# if negative
else:
  print("negative")

  # check is it even or odd
  if (i % 2 == 0):
    print("even")
  else:
    print("odd")