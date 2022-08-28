# take the input then split it and convert to list of integer
user_numbers = [int(number) for number in input().split()]

# convert input of user_numbers to set so it can't has duplicated value
user_numbers = set(user_numbers)

# sort set of user_numbers ascending by integer value
user_numbers = sorted(user_numbers)

# print out the result of length of user_numbers
print(len(user_numbers))
# print out the result of value in user_numbers but only for first 10 values
print(user_numbers[0:10])