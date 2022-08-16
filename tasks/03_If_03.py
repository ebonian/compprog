input_string = input()
l = input_string.split()
l = [float(x) for x in l]
l.sort()
l = l[1:-1]

a = (l[0] + l[1]) / 2
print(round(a, 2))