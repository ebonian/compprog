import math

def findFraction(decimal: float, point: int, repeat: int):
  X = decimal
  nX = decimal * math.pow(10, repeat)

  X = math.floor(X * 10 ** point) / 10 ** point
  nX = math.floor(nX * 10 ** point) / 10 ** point
  n = nX - X
  d = math.pow(10, repeat) - 1

  numerator = n
  denominator = d

  numerator *= math.pow(10, len(str(n).split(".")[1]))
  denominator *= math.pow(10, len(str(n).split(".")[1]))

  return [numerator, denominator]

def findGCD(n, d):
  n = int(n)
  d = int(d)
  res = math.gcd(n, d)
  return res

decimal = input()
decimalList = decimal.split(",")
decimal = float(decimalList[0] + "." + decimalList[1] + decimalList[2] + decimalList[2])

decimal = findFraction(decimal, len(decimalList[1]), len(decimalList[2]))
devisor = findGCD(decimal[0], decimal[1])

numerator = decimal[0] / devisor
denominator = decimal[1] / devisor

print("%d / %d" % (int(numerator), int(denominator)))
