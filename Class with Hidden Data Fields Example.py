class Dog:
    
    def __init__ (self, name):
        self.__name = name
        self.__kind = "canine"

    def getKind(self):
        return(self.__kind)

    def getName(self):
        return(self.__name)

    def setKind(self, kind):
        self.__kind = kind


d = Dog("Duffy")
e = Dog("Emo")
e.setKind("bear")

print(d.getName(), "is", d.getKind())
print(e.getName(), "is", e.getKind())
#print(d.name)




