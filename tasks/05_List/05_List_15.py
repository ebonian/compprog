user_numbers = [int(number) for number in input().split()]

user_numbers = set(user_numbers)

user_numbers = sorted(user_numbers)

print(len(user_numbers))
print(user_numbers[0:10])