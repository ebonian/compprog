class piggybank:
    def __init__(self):
        self.one = 0
        self.two = 0
        self.five = 0
        self.ten = 0
    # มีตัวแปร 4 ตัวเก็บจำนวนเหรียญของเหรียญแต่ละแบบ
    def add1(self, n):
        self.one += n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญบาท
    def add2(self, n):
        self.two += n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสองบาท
    def add5(self, n):
        self.five += n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญห้าบาท
    def add10(self, n):
        self.ten += n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสิบบาท
    def __int__(self):
        money = self.one + self.two*2 + self.five*5 + self.ten*10
        return money
    # คืนมูลค่ารวม = ค่าของเหรียญคูณกับจ านวนเหรียญ
    def __lt__(self, rhs):
        return int(self) < int(rhs)
    # เปรียบเทียบจ านวนเงินใน self กับจ านวนเงินใน rhs
    def __str__(self):
        return '{1:'+str(self.one)+', 2:'+str(self.two)+', 5:'+str(self.five)+', 10:'+str(self.ten)+'}'
    # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)