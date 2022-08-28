# assisgn each set of input into list
first_set = []
second_set = []
third_set = []

# take the interger input of n
first_set_n = int(input())

# take the input of first set by n times
for i in range(first_set_n):
  # take each input
  user_input = input()
  # then append input to first_set list
  first_set.append(int(user_input))

# take the input of second set then split it into list
second_set = [int(num) for num in input().split()]

# take the input of third set
while (True):
  # take each input
  user_input = input()

  # check if the input is not "-1"
  if user_input != "-1":
    # if yes the append input into third_set list
    third_set.append(int(user_input))
  else:
    # if input is "-1" then break out while loop which is not take anymore input
    break

# merge each set into list of numbers_set
numbers_set = first_set + second_set + third_set

# assign list of numbers_output for the result
numbers_output = []

# loop through list of numbers_set of its index
for i in range(len(numbers_set)):
  # check if its index is even
  if (i % 2 == 0):
    # if yes, add number of numbers_set to the end of numbers_output
    numbers_output = numbers_output + [numbers_set[i]]
  else:
    # if no then add number of number_set to the beginning of numbers_output
    numbers_output =  [numbers_set[i]] + numbers_output

# print out the result of numbers_output
print(numbers_output)