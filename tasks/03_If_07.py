import math

i = int(input())

digits = math.floor(math.log10(abs(i)))

if (digits == 0 or digits == 1 or digits == 2):
  print(i)
elif (digits == 3):
  print(str(round(i * math.pow(10, -3), 1)) + "K")
elif (digits == 4):
  print(str(round(i * math.pow(10, -3))) + "K")
elif (digits == 5):
  print(str(round(i * math.pow(10, -3))) + "K")
elif (digits == 6):
  print(str(round(i * math.pow(10, -6), 1)) + "M")
elif (digits == 7):
  print(str(round(i * math.pow(10, -6))) + "M")
elif (digits == 8):
  print(str(round(i * math.pow(10, -6))) + "M")
elif (digits == 9):
  print(str(round(i * math.pow(10, -9), 1)) + "B")
else:
  print(str(round(i * math.pow(10, -9))) + "B")