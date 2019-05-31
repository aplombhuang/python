print("list")	 
l=['d','c','b','a']
for char in l:
    print(char)

print("tuple")	     
t=('d','c','b','a')
for char in t:
    print(char)

print("range")
for idx in range(len(t)):
    print(t[idx])

print("slice")
for char in l[1:4:2]:
    print(char)	
