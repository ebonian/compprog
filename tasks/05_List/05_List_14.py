numbers = [int(num) for num in input().split()]

count = 0

for i in range(1, len(numbers) - 1):
  if (numbers[i - 1] < numbers[i] > numbers[i + 1]):
    count += 1

print(count)