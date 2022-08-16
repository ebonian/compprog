# take the input of weight
w = int(input())

# check weight for each condition and print out the result
if (w <= 100):
  print(18)
elif (100 < w <= 250):
  print(22)
elif (250 < w <= 500):
  print(28)
elif (500 < w <= 1000):
  print(38)
elif (1000 < w <= 2000):
  print(58)
else:
  print("Reject")