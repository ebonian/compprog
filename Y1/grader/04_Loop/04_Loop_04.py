# take the string input
user_input = input()

# convert user_input string to list of string
user_input = list(user_input)

# loop through user_input by index
for i in range(len(user_input)):
  # take the character from list of user_input by index
  character = user_input[i]
  
  # check if character is [, ], (, ) then replace it
  if (character == "["): user_input[i] = "("
  if (character == "]"): user_input[i] = ")"
  if (character == "("): user_input[i] = "["
  if (character == ")"): user_input[i] = "]"

# join the list of user input into string
result = ''.join(user_input)

print(result)