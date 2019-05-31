import copy
listA = ["John", "Jane"] # list
tupleB = (listA, 1, "two" ) # tuple
print(listA)
print(tupleB)

b=copy.copy(tupleB)# shallow copy
c=copy.deepcopy(tupleB)# deep copy

print("original:", id(tupleB), "copy:", id(tupleB[0]))
print("original:", id(b), "copy:", id(b[0]))
print("original:", id(c), "copy:", id(c[0]))

listA[0]="James"

print(listA)
print(b) #result of copy
print(c) #result of deep copy
