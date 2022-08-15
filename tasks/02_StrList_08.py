import math

def findFraction(decimal: float, point: int, repeat: int):
  X = decimal
  nX = decimal * math.pow(10, repeat)

  X = math.floor(X * math.pow(10, point)) / math.pow(10, point)
  nX = math.floor(nX * math.pow(10, point)) / math.pow(10, point)
  n = nX - X
  d = math.pow(10, repeat) - 1
  numerator = round(n, point)
  denominator = d

  numerator *= math.pow(10, len(str(n).split(".")[1]))
  denominator *= math.pow(10, len(str(n).split(".")[1]))

  return [numerator, denominator]

def findGCD(n, d) -> int:
  n = int(n)
  d = int(d)
  res = math.gcd(n, d)
  return res

def main():
  decimal = input()
  decimalList = decimal.split(",")
  decimal = float(decimalList[0] + "." + decimalList[1] + decimalList[2] + decimalList[2])
  decimal = abs(decimal)

  decimal = findFraction(decimal, len(decimalList[1]), len(decimalList[2]))
  numerator = decimal[0]
  denominator = decimal[1]

  divisor = findGCD(numerator, denominator)

  print("%d / %d" % (int(numerator / divisor), int(denominator / divisor)))

main()