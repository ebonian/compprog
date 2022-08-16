# [Solution #1]
# use list and sort it (but it should use if to find solution)
# 
# take the input of string of numbers
input_string = input()

# split string of numbers into list of strings
input_list = input_string.split()

# convert list of string to list of numbers
input_list = [float(x) for x in input_list]

# sort the list from least to most
input_list.sort()

# slice out most and least to get the remaining two
input_list = input_list[1:-1]

# calculate average of the remaining two
score = (input_list[0] + input_list[1]) / 2

# round the score to two decimal places
score = round(score, 2)

# print out the solution
print(score)