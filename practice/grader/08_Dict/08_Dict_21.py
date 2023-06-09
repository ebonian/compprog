count = {}
user_input = input().lower()

for i in user_input:
    if 'a' <= i <= 'z':
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
            
result = []

for i in count:
    result.append([-count[i],i])

result.sort()

for i in range(len(result)):
    print(result[i][1], '->', -result[i][0])