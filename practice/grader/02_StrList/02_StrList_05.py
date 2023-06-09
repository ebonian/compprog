# take the input of sale
sales = str(input())

# convert to list of sales
sales = sales.split(" ")

# remove empty string from sales list
while("" in sales) :
    sales.remove("")

# convert sales list of string to list of int
sales = [int(x) for x in sales]

# assign initial value of sum
total = 0

# loop through sales list and increase total by sales value
for val in sales:
  total += val

# print the sum of sales
print(total)