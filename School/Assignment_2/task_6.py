# CS521 - A2
# Deependrasingh Shekhawat
# Script for Area between co-ordinates

import math

no_of_sides = int(input("Please enter number of sides for a polygon: "))
side_length = float(input("Please provide length of each side: "))

area = (no_of_sides * pow(side_length, 2)) / (4 * math.tan(math.pi/no_of_sides))

print(f"The are of the polygon is {area}")
