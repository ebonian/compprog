import math

def distance1(x1, y1, x2, y2):
  distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

  return distance

def distance2(p1, p2):
  x2 = p2[0]
  x1 = p1[0]
  y2 = p2[1]
  y1 = p1[1]

  distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

  return distance

def distance3(c1, c2):
  x2 = c2[0]
  x1 = c1[0]
  y2 = c2[1]
  y1 = c1[1]

  center_distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

  total_radius = c1[2] + c2[2]

  is_overlap = center_distance <= total_radius

  return center_distance, is_overlap

def perimeter(points):
  total_distance = 0

  for i in range(len(points)):
    x2 = points[i - 1][0]
    x1 = points[i][0]
    y2 = points[i - 1][1]
    y1 = points[i][1]

    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

    total_distance += distance

  return total_distance

# print(perimeter([[0.0, 0], [0, 2], [2, 2], [2, 0]]))

exec(input().strip())