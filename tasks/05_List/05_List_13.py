first_set = []
second_set = []
third_set = []

first_set_n = int(input())

for i in range(first_set_n):
  user_input = input()
  first_set.append(int(user_input))

second_set = [int(num) for num in input().split()]

while (True):
  user_input = input()

  if user_input != "-1":
    third_set.append(int(user_input))
  else:
    break

numbers_set = first_set + second_set + third_set

numbers_output = []

for i in range(len(numbers_set)):
  if (i % 2 == 0):
    numbers_output = numbers_output + [numbers_set[i]]
  else:
    numbers_output =  [numbers_set[i]] + numbers_output

print(numbers_output)