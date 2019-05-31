Python 3.6.0 (v3.6.0:41df79263a11, Dec 23 2016, 07:18:10) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class Parameter
SyntaxError: invalid syntax
>>> import Math
class Calculator:
	def perimeter(self,x):
		self.x = 2*x*Math.pi
	def area(self,x)
	
SyntaxError: multiple statements found while compiling a single statement
>>> import Math
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    import Math
ModuleNotFoundError: No module named 'Math'
>>> import math
>>> class Calculator:
	def init(self,x):
		self.x = x
	def area(self):
		return self.x*self.x*math.pi
	def perimeter(self):
		return 2*self.x*math.pi

	
>>> r = Calculator(3)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    r = Calculator(3)
TypeError: object() takes no parameters
>>> r = new Calculator(3)
SyntaxError: invalid syntax
>>> import math
>>> class Calculator:
	def __init__(self,x):
		self.x = x
	def area(self):
		return self.x*self.x*math.pi
	def perimeter(self):
		return 2*self.x*math.pi

	
>>> r = Calculator(3)
>>> print("Perimeter of a radius 3 is : %d" %r.perimeter())
Perimeter of a radius 3 is : 18
>>> print("Perimeter of a radius 3 is : %f" %r.perimeter())
Perimeter of a radius 3 is : 18.849556
>>> print("Area of a radius 3 is : %f" %r.area())
Area of a radius 3 is : 28.274334
>>> 
