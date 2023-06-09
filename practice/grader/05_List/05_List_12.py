# input integer of n for the numbers of name input
n = int(input())

# assign list of input_names ready for append each name from user input
input_names = []

# take the input of name n times
for i in range(n):
  name = input()
  # append each name into input_names
  input_names.append(name)

# assign object of name by assign key as fullname and value as nickname
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

# assign list of name_result for append each names
name_result = []

# loop through list of input_names by each name
for name in input_names:
  # check if the name in a keys of name_table
  if (name in name_table.keys()):
    # if yes then append value of its key into name_result list
    name_result.append(name_table[name])

  # check if name in a values of name_table
  elif (name in name_table.values()):
    # if yes then append the key of that value into name_result list
    name_result.append(list(name_table.keys())
      [list(name_table.values()).index(name)])
  
  # if neither name in keys and values then that name is not founded
  else:
    name_result.append("Not found")

# print out list of name_result line by line
for name in name_result:
  print(name)