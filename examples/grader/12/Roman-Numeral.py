class roman :
    def __init__(self, r):
        self.thou = 0
        self.hund = 0
        self.ten = 0
        self.unit = 0
        have_D = False
        for i in range (len(r)):
            if r[i] == 'M':
                if i == 0 :
                    self.thou +=1
                elif r[i-1] =='M':
                    self.thou += 1
                elif r[i-1] == 'C':
                    self.hund += 8
            elif r[i] == 'D':
                if i == 0:
                    self.hund += 5
                elif r[i-1] == 'C':
                    self.hund += 3
                else: self.hund += 5
            elif r[i] == 'L':
                if i==0:
                    self.ten += 5
                elif r[i-1] == 'X':
                    self.ten += 3
                else: self.ten += 5
            elif r[i] == 'C':
                if i == 0:
                    self.hund += 1
                elif r[i-1] == 'X':
                    self.ten += 8
                else:
                    self.hund += 1
            elif r[i] == 'X':
                if i == 0:
                    self.ten +=1
                elif r[i-1] == 'I':
                    self.unit += 8
                else:
                    self.ten += 1
            elif r[i] == 'V':
                if i == 0:
                    self.unit += 5
                elif r[i-1] == 'I':
                    self.unit += 3
                else:
                    self.unit += 5
            elif r[i] == 'I':
                self.unit += 1

    def __lt__(self, rhs):
        return int(self) < int(rhs)

    def __str__(self):
        hundred = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
        ten = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
        unit = ['','I','II','III','IV','V','VI','VII','VIII','IX']
        return self.thou*'M'+hundred[self.hund]+ten[self.ten]+unit[self.unit]

    def __int__(self):
        return self.thou*1000 + self.hund*100 + self.ten*10 + self.unit

    def __add__(self, rhs):
        new=roman('')
        new.unit = self.unit + rhs.unit
        new.ten = self.ten + rhs.ten
        new.hund = self.hund + rhs.hund
        new.thou = self.thou + rhs.thou
        if new.unit >= 10:
            new.unit -= 10
            new.ten += 1
        if new.ten >= 10:
            new.ten -= 10
            new.hund += 1
        if new.hund >= 10:
            new.hund -= 10
            new.thou += 1
        return new
        
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))