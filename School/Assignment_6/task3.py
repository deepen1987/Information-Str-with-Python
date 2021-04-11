# CS521 - A2
# Deependrasingh Shekhawat
# Script for class for Regular Polygon
import math


class RegPolygon:
    def __init__(self, n=3, side=1.0, x=0.0, y=0.0):
        self.__n = n
        self.__side = side
        self.__x = x
        self.__y = y

    def get_no_of_sides(self):
        return self.__n

    def get_side_len(self):
        return self.__side

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_no_of_sides(self, value):
        self.__n = value

    def set_side_len(self, value):
        self.__side = value

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value

    def get_perimeter(self):
        return round(self.__n * self.__side, 2)

    def get_area(self):
        return round((self.__n * self.__side ** 2) / (4 * math.tan(math.pi / self.__n)), 2)


poly1 = RegPolygon(6, 3.0, 1, 1)

print(f"""This is a regular polygon with no of side as {poly1.get_no_of_sides()}, each side with length  
{poly1.get_side_len()} and the x and y coordinates are ({poly1.get_x()},{poly1.get_y()}). The perimeter for 
this polygon is {poly1.get_perimeter()} and area is {poly1.get_area()}.\n""")

poly1.set_x(2)
poly1.set_y(2)
poly1.set_side_len(4)
poly1.set_no_of_sides(8)

print(f"""This is a regular polygon with no of side as {poly1.get_no_of_sides()}, each side with length  
{poly1.get_side_len()} and the x and y coordinates are ({poly1.get_x()},{poly1.get_y()}). The perimeter for 
this polygon is {poly1.get_perimeter()} and area is {poly1.get_area()}.""")

