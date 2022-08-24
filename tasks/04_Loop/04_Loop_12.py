n = int(input())

x_column = []
y_column = []

for i in range(n):
    x, y = input().split(" ")

    x_column.append(int(x))
    y_column.append(int(y))
      
method = input()

red_list = []
blue_list = []

for i in range(len(x_column)):
  if (method == "Zig-Zag"):
    if (i % 2 == 0):
      red_list.append(x_column[i])
      blue_list.append(y_column[i])

    else:
      red_list.append(y_column[i])
      blue_list.append(x_column[i])

  elif (method == "Zag-Zig"):
    if (i % 2 == 0):
      red_list.append(y_column[i])
      blue_list.append(x_column[i])
      
    else:
      red_list.append(x_column[i])
      blue_list.append(y_column[i])

print(min(red_list), max(blue_list))