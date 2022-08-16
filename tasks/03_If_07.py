import math

# take the input of int
integer = int(input())

# calculate digits of int
digits = math.floor(math.log10(abs(integer)))

# check for each digit and print out the result
if (digits == 0 or digits == 1 or digits == 2): print(integer)
elif (digits == 3):
  print(str(round(integer * math.pow(10, -3), 1)) + "K")
elif (digits == 4):
  print(str(round(integer * math.pow(10, -3))) + "K")
elif (digits == 5):
  print(str(round(integer * math.pow(10, -3))) + "K")
elif (digits == 6):
  print(str(round(integer * math.pow(10, -6), 1)) + "M")
elif (digits == 7):
  print(str(round(integer * math.pow(10, -6))) + "M")
elif (digits == 8):
  print(str(round(integer * math.pow(10, -6))) + "M")
elif (digits == 9):
  print(str(round(integer * math.pow(10, -9), 1)) + "B")
else:
  print(str(round(integer * math.pow(10, -9))) + "B")