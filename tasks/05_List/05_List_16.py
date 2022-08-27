user_number = int(input())

steps = []

while (True):
  steps.append(str(user_number))

  if (user_number != 1):
    if (user_number % 2 == 0):
      user_number //= 2
    else:
      user_number = 3 * user_number + 1
  else:
    break

print('->'.join(steps[-15:]))