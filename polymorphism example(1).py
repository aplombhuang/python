class Employee:
    def __init__(self,rate):
        self.rate=rate
        
    def printSalaryPerMonth(self):
        print(str(self.rate))

class HourlyEmployee(Employee):
    def __init__(self, rate):
        super().__init__(rate)
        
    def printSalaryPerMonth(self):
        print(str(self.rate*20*8))

class SalariedEmployee(Employee):
    def __init__(self, rate):
        super().__init__(rate)
        
    def printSalaryPerMonth(self):
        print(str(self.rate/12))

def PrintWage(emp):
    emp.printSalaryPerMonth()
        
f=HourlyEmployee(10)
g=SalariedEmployee(50000)

f.printSalaryPerMonth()  
g.printSalaryPerMonth()

PrintWage(f)

