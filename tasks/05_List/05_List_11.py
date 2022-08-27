user_input = input()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

user_numbers = set()

for char in user_input:
  if char.isdigit():
    user_numbers.add(char)

for num in user_numbers:
  numbers.remove(num)

if len(numbers):
  print(','.join(numbers))
else:
  print("None")