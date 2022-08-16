class piggybank:
    def __init__(self):
        self.coins = {}
        self.amount = 0
    # มีตัวแปร self.coins เก็บ dict เริ่มต้นให้ว่าง ๆ
    # มี key เป็นมูลค่าเหรียญ และ value เป็นจ านวนเหรียญ
    def add(self, v, n):
        if self.amount + n > 100: return False
        else:
            self.amount += n
            v = float(v)
            if v not in self.coins:
                self.coins[v] = 0
            self.coins[v] += n
            return True
    # ถ้าเพิ่มจ านวนเหรียญในกระปุกอีก n เหรียญแล้วเกิน 100
    # จะไม่ให้เพิ่ม ให้คืน False แทนว่า เพิ่มไม่ส าเร็จ
    # แปลง v เป็น float ก่อน (เพิ่ม 5 กับ 5.0 จะได้เหมือนกัน)
    # ถ้ากระปุกไม่เคยมีเหรียญ v ท า self.coins[v]= 0
    # ท าค าสั่ง self.coins[v] += n
    # คืน True แทนว่าเพิ่มส าเร็จ
    def __float__(self):
        if len(self.coins) == 0: return 0.0 
        money = sum([e*self.coins[e] for e in self.coins])
        return money
    # นำค่าของเหรียญคูณกับจ านวนเหรียญ ของเหรียญทุกแบบ
    # ต้องคืนจ านวนแบบ float เท่านั้น อยากคืนศูนย์ ก็ต้อง 0.0
    def __str__(self):
        if len(self.coins) == 0: return '{}'
        sort_coins=sorted(self.coins.items())
        temp=''
        for coin,amount in sort_coins:
            temp += str(coin)+':'+str(amount)+', '
        temp=temp[:-2]
        return '{'+temp+'}'
    # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
    # โดยให้เรียงเหรียญตามมูลค่าจากน้อยไปมาก
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
