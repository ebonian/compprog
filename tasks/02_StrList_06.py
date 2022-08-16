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

# define function of summing 3d vector
def sumVector(u, v):
  sum = []
  
  for uValue, vValue in zip(u,v):
    sum.append(float(uValue + vValue))
  
  return sum

print("%s + %s = %s" % (U, V, sumVector(U, V)))
