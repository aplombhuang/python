Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Animal(self)
SyntaxError: invalid syntax
>>> class Animal(self):
	self.sound = "Sound"
	print("Animal", self.sound)

	
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    class Animal(self):
NameError: name 'self' is not defined
>>> class Cat(Animal)
SyntaxError: invalid syntax
>>> class Animal:
	self.sound="sound"
	print("Animal", self.sound)

	
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    class Animal:
  File "<pyshell#11>", line 2, in Animal
    self.sound="sound"
NameError: name 'self' is not defined
>>> class Animal:
	def __init__(self):
		self.sound="sound"
		print("Animal", self.sound)

		
>>> class Cat(Animal):
	def super().__init__():
		
SyntaxError: invalid syntax
>>> class Cat(Animal):
	def__init__(self):
		
SyntaxError: invalid syntax
>>> class Cat(Animal):
	def __init__(self)
	
SyntaxError: invalid syntax
>>> class Cat(Animal):
	def __init__(self):
		super().__init__()
		self.sound = "Meow"
		print("Cat",self.sound)

		
>>> Cat
<class '__main__.Cat'>
>>> print(Cat)
<class '__main__.Cat'>
>>> Cat.print()
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    Cat.print()
AttributeError: type object 'Cat' has no attribute 'print'
>>> print(Cat())
Animal sound
Cat Meow
<__main__.Cat object at 0x05FAD2D0>
>>> print(Cat)
<class '__main__.Cat'>
>>> 
