import json

# take the input of u and v vectors
u = str(input())
v = str(input())

# covert list string to list of float
u = [float(x) for x in json.loads(u)]
v = [float(x) for x in json.loads(v)]

# define function of summing 3d vector
def vectorSum(u: list[float], v:list[float]) -> list[float]:
  sum = []
  
  for uValue, vValue in zip(u,v):
    sum.append(uValue + vValue)
  
  return sum

# print the result
print("%s + %s = %s" % (u, v, vectorSum(u,v)))