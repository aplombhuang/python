x="xglobal"
y="yglobal"

def funct1():
    x="x_in_1"
    print("1:", x, y)

def funct2():
    y="y_in_2"
    print("2:", x, y)
    funct1()
    print("2:", x, y)    

print("g:", x, y)
funct2()
print("g:", x, y)
