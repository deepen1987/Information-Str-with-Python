"""
CS521 - A2
Deependrasingh Shekhawat

Script for Area of a pentagon
"""
import math

r = float(input("Please enter length from the centre to a vertex: "))


s = (2 * r) * (math.sin(math.pi / 5))

area = ((3 * math.sqrt(3)) / 2) * s ** 2

print(f"The area of the pentagon is {str(round(area, 2))}")
