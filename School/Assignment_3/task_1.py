# CS521 - A2
# Deependrasingh Shekhawat
# Script for Quadratic Equation
import math

a = float(input("Please enter value for a: "))
b = float(input("Please enter value for b: "))
c = float(input("Please enter value for c: "))


def roots(root_num):
    if root_num > 0:
        r1 = (-b + math.sqrt(b**2 - 4 * a * c))/2 * a
        if r1.is_integer():
            r1 = int(r1)
            print(r1)
        r2 = (-b - math.sqrt(b**2 - 4 * a * c))/2 * a
        if r2.is_integer():
            r2 = int(r2)
        print(f"The roots are {round(r1, 6)} and {round(r2, 5)}")
    elif root_num == 0:
        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        if r1.is_integer():
            r1 = int(r1)
        print(f"The root is {round(r1, 5)}")

    else:
        print("The equation has no real roots")


discriminant = b**2 - 4 * a * c

roots(discriminant)



