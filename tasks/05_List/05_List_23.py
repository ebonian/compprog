# import math module
import math

# take the interger input of n for the numbers of points
n_points = int(input())

# assign list of point and list of distance for append from input
points = []
distances = []

# assign distance_dict dictionary for store the distance for each point
distance_dict = {}

# loop through n_points to take the input of points n_points times
for n in range(n_points):
  # take the input and split it into list then append its list to points list
  points.append(input().split(" "))

# calculate distance start by loop through list of points by its index
for i in range(len(points)):
  # extract point position by x and y from list of points according to the index
  x, y = points[i]

  # convert point x and y to float from string
  x, y = float(x), float(y)

  # calculate the distance
  distance = math.sqrt(math.pow(x - 0, 2) + math.pow(y - 0, 2))

  # assign the distance into dictionary of distance_dict by the key of its index + 1
  distance_dict[i + 1] = distance

  # append distance to list of distances
  distances.append(distance)

# slice the third distance from list of distances by sort it and select the value by the index of 2
third_distance = sorted(distances)[2]

# assign distance_index by take the key from the thrid distance value from distance_dict
distance_index = list(distance_dict.keys())[list(distance_dict.values()).index(third_distance)]

# print out the result of third-closest point index and position
print("#%d: (%s)" % (distance_index, ', '.join(points[distance_index - 1])))