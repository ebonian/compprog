user_input = input()

user_input = [i for i in user_input]

for i in range(len(user_input)):
  index = i
  character = user_input[index]
  if (character == "["): user_input[i] = "("
  if (character == "]"): user_input[i] = ")"
  if (character == "("): user_input[i] = "["
  if (character == ")"): user_input[i] = "]"

print(''.join(user_input))