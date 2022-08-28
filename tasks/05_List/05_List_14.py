# take the input then split it and convert to list of integer
numbers = [int(num) for num in input().split()]

# assign count value
count = 0

# loop through numbers by its index but except the first and last index
for i in range(1, len(numbers) - 1):
  # check if its number of numbers is greater than left side and right side of its index
  if (numbers[i - 1] < numbers[i] > numbers[i + 1]):
    # if yes then increase count by 1
    count += 1

# print the result of final counts
print(count)