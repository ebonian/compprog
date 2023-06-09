import math

# define func to calculate lower bound and upper bound
def calculateLowerBound(n: int) -> float:
  result = math.sqrt(2*math.pi) * n**(n+1/2) * math.e**(-n + 1/(12*n+1))
  return result

def calculateUpperBound(n: int) -> float:
  result = math.sqrt(2*math.pi) * n**(n+1/2) * math.e**(-n + 1/(12*n))
  return result

# take the input of n
n = int(input())

# print the result
print(calculateLowerBound(n))
print(calculateUpperBound(n))