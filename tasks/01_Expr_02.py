import math

# define func
def calculateRootX1(a: float, b: float, c: float) -> float:
  result = (-b - math.sqrt((b**2) - (4 * a * c))) / (2 * a)
  result = round(result, 3)
  return result

def calculateRootX2(a: float, b: float, c: float) -> float:
  result = (-b + math.sqrt((b**2) - (4 * a * c))) / (2 * a)
  result = round(result, 3)
  return result

# take the input of a, b, c
a = float(input())
b = float(input())
c = float(input())

# take the result
print(calculateRootX1(a,b,c), calculateRootX2(a,b,c))