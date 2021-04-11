# CS521 - A2
# Deependrasingh Shekhawat
# Script for class for Triangle
import math


class GeometricObject:
    pass


class Triangle(GeometricObject):
    def __init__(self, side1=1.0, side2=1.0, side3=1.0):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def get_side1(self):
        return self.side1

    def get_side2(self):
        return self.side2

    def get_side3(self):
        return self.side3

    def get_area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return round(math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2)

    def get_perimeter(self):
        return round(self.side1 + self.side2 + self.side3, 2)

    def __str__(self):
        return "Triangle: side1 = " + str(self.side1) + " side2 = " + str(self.side2) + " side3 = " + str(self.side3)


tri = Triangle(3, 4, 6)
print(tri.__str__())

print(f"Side1: {tri.get_side1()} Side2: {tri.get_side2()} Side3: {tri.get_side3()}")
print(f"Area of triangle is {tri.get_area()} and perimeter is {tri.get_perimeter()}")
