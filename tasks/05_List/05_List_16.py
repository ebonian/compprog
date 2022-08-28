# take the interger input
user_number = int(input())

# assign list of steps for append each step from calculation
steps = []

# calculation process
while (True):
  # start by convert its number to string and append it to list of steps
  steps.append(str(user_number))

  # check if user_number not equal to 1
  if (user_number != 1):
    # if user_number not equal to 1 then check if its number even or not
    if (user_number % 2 == 0):
      # if yes then divided by two without decimal
      user_number //= 2

    else:
      # if no then times it by 3 and add by 1
      user_number = 3 * user_number + 1

  else:
    # if user_number is equal to 1 then end the calculation by break out the loop
    break

# print out the result
print('->'.join(steps[-15:]))