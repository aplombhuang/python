class Dog:
    kind = "canine"
    def __init__ (self, name):
        self.name = name


def funct(self, x):
    print(self.name, x)


Dog.kind = "bear"
Dog.color = "black"

d = Dog("Duffy")
e = Dog("Emo")

e.kind = "cat"
e.size = "small"

print(d.name, "is", d.kind, "of color", d.color)
print(e.name, "is", e.kind, "of size", e.size)
#print(d.size)

Dog.funct = funct;
d.funct("abc")

d.f = funct.__get__(d, d.__class__)
d.f("efg")
#e.f("hij")
print(d.funct.__get__(d))


