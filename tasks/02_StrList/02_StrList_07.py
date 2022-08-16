code = input()
a = code[3::7]
b = code[7::5]
c = str(int(a) + int(b) + 10000)
thousands = (int(c) % 10000) // 1000
hundreds = (int(c) % 1000) // 100
tens = (int(c) % 100) // 10
d = str(thousands) + str(hundreds) + str(tens)
e = 1
for n in d:
  e += int(n)
e = int(str(e)[-1])
letters = "ABCDEFGHIJ"
f = letters[e - 1]
g = d + f
print(g)