class Complex:
    def __init__(self,a,b):
        self.real = a
        self.complex = b

    def __str__(self):
        out=''
        have = False
        if self.real != 0: 
            out += str(self.real)
            have =True
        if self.complex != 0 and abs(self.complex) != 1:
            if self.complex > 0: out += '+'+str(self.complex)+'i'
            else: out += str(self.complex)+'i'
        elif self.complex == 1: out += '+'+'i'
        elif self.complex == -1: out += '-'+'i'
        if not have and out == '': out = '0'
        elif not have and out[0] != '-': out=out[1:]
        return out

    def __add__(self,rhs):
        a = self.real + rhs.real
        b = self.complex + rhs.complex
        return Complex(a,b)

    def __mul__(self,rhs):
        a = self.real*rhs.real - self.complex*rhs.complex
        b = self.real*rhs.complex + self.complex*rhs.real
        return Complex(a,b)
    
    def __truediv__(self,rhs):
        d = rhs.real**2 + rhs. complex**2
        a = self.real*rhs.real + self.complex*rhs.complex
        b = -self.real*rhs.complex + self.complex*rhs.real
        return Complex(a/d,b/d)

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)