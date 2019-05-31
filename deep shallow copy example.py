import copy
class City:
    def __init__(self,name):
        self.name=name

class University:
    def __init__(self,name,city):
        self.name=name;self.city=city

rva=City("Richmond")
vcu=University("VCU",rva)

print(id(vcu), id(vcu.name), id(vcu.city), id(vcu.city.name))
spawnU=vcu
print(id(spawnU), id(spawnU.name), id(spawnU.city), id(spawnU.city.name))
spawnU=copy.copy(vcu)
print(id(spawnU), id(spawnU.name), id(spawnU.city), id(spawnU.city.name))
spawnU=copy.deepcopy(vcu)
print(id(spawnU), id(spawnU.name), id(spawnU.city), id(spawnU.city.name))
