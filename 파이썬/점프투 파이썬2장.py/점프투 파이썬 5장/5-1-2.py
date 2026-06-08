class calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class upgradecalculator(calculator):
    def ninus(self,val):
        self.valu -= val


cal = upgradecalculator()
cal.add(10)
cal.minus(7)

print(cal.value)

