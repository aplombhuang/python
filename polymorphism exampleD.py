class HourlyEmployee():
    def __init__(self, rate):
        self.rate = rate
        
    def printSalaryPerMonth(self):
        print(str(self.rate*20*8))

class SalariedEmployee():
    def __init__(self, rate):
        self.rate = rate
        
    def printSalaryPerMonth(self):
        print(str(self.rate/12))

def PrintWage(emp):
    emp.printSalaryPerMonth()
        
f=HourlyEmployee(10)
g=SalariedEmployee(60000)

f.printSalaryPerMonth()  
g.printSalaryPerMonth()

PrintWage(f)

