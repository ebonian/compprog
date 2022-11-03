n_of_input = int(input())

book = {}

for i in range(n_of_input):
    name, surname, tel = input().split()
    name = name + ' ' + surname
    book[name] = tel
    book[tel] = name

m = int(input())

for i in range(m):
    find = input()

    if find in book:
        print(find, '-->', book[find])
    else:
        print(find, '--> Not found')
