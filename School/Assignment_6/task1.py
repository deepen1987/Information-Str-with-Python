# CS521 - A2
# Deependrasingh Shekhawat
# Script for creating a rectangle class

class Rectangle:
    def __init__(self, width=1, height=2):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


new_rec1 = Rectangle(4, 5)

print(f"""The area of rectangle is {new_rec1.get_area()} and
the perimeter of rectangle is {new_rec1.get_perimeter()}""")