# take the input of u and v vectors
u = input()
v = input()

U = []
V = []

u = u.replace("[", "").replace("]", "").replace(",", "").split(" ")
v = v.replace("[", "").replace("]", "").replace(",", "").split(" ")

for uValue, vValue in zip(u, v):
  U.append(float(uValue))
  V.append(float(vValue))

print(U)
print(V)

# define function of summing 3d vector
def sumVector(u: list[float], v:list[float]) -> list[float]:
  sum = []
  
  for uValue, vValue in zip(u,v):
    sum.append(float(uValue + vValue))
  
  return sum

print("%s + %s = %s" % (U, V, sumVector(U, V)))