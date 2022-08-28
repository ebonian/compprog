# take a line of string input of user
user_input = input()

# listed number to be check in string
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# assign user_numbers as set so it won't has duplicated value
user_numbers = set()

# loop through user_input by character
for character in user_input:
  # check if each character a digit
  if character.isdigit():
    # if it's number then add it to user_numbers set
    user_numbers.add(character)

# loop through number in user_numbers
for number in user_numbers:
  # then remove string of numbers in numbers list according to user_numbers set
  numbers.remove(number)

# check if list of numbers empty or not
if len(numbers):
  # if not empty, print out the result which is a number that is not in a string of user_input
  print(','.join(numbers))
else:
  # if list of numbers empty, then print "None"
  print("None")