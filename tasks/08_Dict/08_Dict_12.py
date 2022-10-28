names = {}

n_of_name = int(input())

for n in range(n_of_name):
  real_name, nick_name = input().split()
  names[nick_name] = real_name

names_keys = list(names.keys())
names_values = list(names.values())


n_of_finding_name = int(input())

for n in range(n_of_finding_name):
  name = input()
  if (n_of_finding_name < 100):
    if (name in names_keys):
      print(names_values[names_keys.index(name)])
    elif (name in names_values):
      print(names_keys[names_values.index(name)])
    else:
      print("Not found")
  else:
    print("Not found")