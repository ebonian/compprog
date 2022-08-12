# assign all the months to months list
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

# take the input of day month and year in number and split into list
date = str(input()).split("/")

# assign each day month and year from date list
d = int(date[0])
m = int(date[1])
y = int(date[2])

# print the result
print("%s %d, %d" % (months[m - 1], d, y))
