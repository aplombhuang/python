l = [0,1,2,3,4,5,6,7,8,9]
print(l[::4])
print(l[4::4])
print(l[3::4])
class Animal:
	def __init__(self):
		self.sound="sound"
		print("Animal", self.sound)

		
class Cat(Animal):
	def __init__(self):
		super().__init__()
		self.sound = "Meow"
		print("Cat",self.sound)


 print(Cat())
