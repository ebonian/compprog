import math

n_points = int(input())

points = []
distances = []
obj = {}

for n in range(n_points):
  points.append(input().split(" "))

# calculate distance
for i in range(len(points)):
  x, y = points[i]

  distance = math.sqrt(math.pow(float(x) - 0, 2) + math.pow(float(y) - 0, 2))

  obj[i + 1] = distance

  distances.append(distance)

third_distance = sorted(distances)[2]
distance_index = list(obj.keys())[list(obj.values()).index(third_distance)]

print("#%d: (%s)" % (distance_index, ', '.join(points[distance_index - 1])))