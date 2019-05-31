items = input("try this").strip().split()

i = 0

j = int((len(items))/2)

num1 = [0 for i in range(j)]

num2 = [0 for i in range(j)]

for i in range(j):
        num1[i] = eval(items[2 * i])
        num2[i] = eval(items[2*i +1])



length = sorted(num1)

width = sorted(num2)

string1 = str(length[0])

string2 = str(width[0])

print(length)

print(width)

string = string1 + string2

print(string1)

print(string2)

print(string)

x = input()

