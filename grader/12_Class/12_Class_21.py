class Complex:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    def __str__(self) -> str:
        if self.b:
            if self.a == 0:
                if (self.b == 1):
                    return 'i'
                elif (self.b == -1):
                    return '-i'
                else:
                    return str(self.b) + 'i'
            elif self.b == 1:
                if (self.a > 0):
                    return '{}+i'.format(self.a)
                else:
                    return '{}-i'.format(self.a)
            elif self.b == -1:
                if (self.a > 0):
                    return '{}-i'.format(self.a)
                else:
                    return '{}+i'.format(self.a)
            else:
                if (self.b > 0):
                    return '{}+{}i'.format(self.a, self.b)
                else:
                    return '{}-{}i'.format(self.a, -self.b)
        else:
            return '{}'.format(self.a)

    def __add__(self, rhs):
        return Complex(self.a + rhs.a, self.b + rhs.b)

    def __mul__(self, rhs):
        return Complex(self.a * rhs.a - self.b * rhs.b, self.a * rhs.b + self.b * rhs.a)

    def __truediv__(self, rhs):
        return Complex((self.a * rhs.a + self.b * rhs.b) / (rhs.a ** 2 + rhs.b ** 2), (- self.a * rhs.b + self.b * rhs.a) / (rhs.a ** 2 + rhs.b ** 2))


t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a, b)
c2 = Complex(c, d)
if t == 1:
    print(c1)
elif t == 2:
    print(c2)
elif t == 3:
    print(c1 + c2)
elif t == 4:
    print(c1 * c2)
else:
    print(c1 / c2)
