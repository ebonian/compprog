user_input = input()

previos_character = user_input[0]

counts = 0

result = []

for i in range(len(user_input)):
  if user_input[i] == previos_character:
    counts += 1
    
  else:
    result.append(previos_character + " " + str(counts))
    previos_character = user_input[i]
    counts = 1

result.append(previos_character + " " + str(counts))

result = ' '.join(result)

print(result)