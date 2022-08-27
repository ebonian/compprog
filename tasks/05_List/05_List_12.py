n = int(input())

input_names = []

for i in range(n):
  name = input()
  input_names.append(name)


name_table = {
  "Robert": "Dick",
  "William": "Bill",
  "James": "Jim",
  "John": "Jack",
  "Margaret": "Peggy",
  "Edward": "Ed",
  "Sarah": "Sally",
  "Andrew": "Andy",
  "Anthony": "Tony",
  "Deborah": "Debbie"
}

name_result = []

for name in input_names:
  if (name in name_table.keys()):
    name_result.append(name_table[name])
  elif (name in name_table.values()):
    name_result.append(list(name_table.keys())
      [list(name_table.values()).index(name)])
  else:
    name_result.append("Not found")

for name in name_result:
  print(name)