f1 = open("output.txt").readlines()
f2 = open("expected.txt").readlines()

f1 = [x.replace("\n", "") for x in f1]
f2 = [x.replace("\n", "") for x in f2]

c = 0

for a, b in zip(f1, f2):
    if (a == b):
        c += 1
    else:
        print(a)
        print(b)


print(c)
