x=10

def doubleIt(y):
    x=2*y
    return x

def doubleItToX(y):
    global x
    x=2*y
    return x

print(doubleIt(2))
print(x) # prints 10

print(doubleItToX(2))
print(x) # prints 4
