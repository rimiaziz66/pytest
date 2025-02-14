import math

class Shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius **2
        return area

    def perimeter(self):
        peri = 2*math.pi*self.radius
        return peri




