i = int(input())

if (i == 0):
  print("zero")
  print("even")
elif (i > 0):
  print("positive")

  if (i % 2 == 0):
    print("even")
  else:
    print("odd")
else:
  print("negative")
  if (i % 2 == 0):
    print("even")
  else:
    print("odd")