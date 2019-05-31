import math
class Circle():

    def __init__(self, radius):
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getArea(self):
        return math.pi * self.__radius**2

    def getPerimeter(self):
        return 2 * math.pi * self.__radius
    


    
