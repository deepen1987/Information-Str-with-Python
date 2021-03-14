# Defining Classes
#
# class MyPoint:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __eq__(self):
#         return self.x == self.x and self.y == self.y

#     @classmethod
#     def note(cls):
#         pass

#     def draw(self):
#         print(f"Point ({self.x},{self.y})")

# Inheritance
# point = MyPoint(1, 2)
# print(type(point))

# MyPoint.note()

# class Animal:
#     def __init__(self):
#         self.age = 1

# class Mammal(Animal):
#     def __init__(self):
#         self.weight = 2


# Abstract Class and Methods
from abc import ABC, abstractmethod


class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


class TextBox(UIControl):
    def draw(self):
        print("textbox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


def draw(control):
    control.draw()
# Using this method we can textbox or drowdownlist methods to it and at runtime it executes it. This is example of polymorphism as the same method is acting differently for different object call.


ddl = DropDownList()
draw(ddl)


draw(ddl)
