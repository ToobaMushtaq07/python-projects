import math
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

radius = float(input("Enter the radius of the circle: "))
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

circle = Circle(radius)
rectangle = Rectangle(length, width)

print("\nArea of Circle =", round(circle.area(), 2))
print("Area of Rectangle =", rectangle.area())
