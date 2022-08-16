import math

[a, b, c] = input().split(",")

ib = b
b = b if b else "0"

n = int(b+c) - int(b)
d = int(''.join(map(str,([9] * len(c)) + [0] * len(ib))))
n = d * int(a) + n

divisor = math.gcd(n, d)

print("%d / %d" % (n//divisor, d//divisor))