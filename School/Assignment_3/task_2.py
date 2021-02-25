# CS521 - A2
# Deependrasingh Shekhawat
# Script for linear Equation

a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))
d = float(input("Please enter a value for d: "))
e = float(input("Please enter a value for e: "))
f = float(input("Please enter a value for f: "))


def lin_equ(verify_output):
    if verify_output == 0:
        print("The equation has no solution")
    else:
        x = ((e * d) - (b * f)) / ((a * d) - (b * c))
        y = ((a * f) - (e * c)) / ((a * d) - (b * c))
        print(f"x is {x} and y is {y}")


valid_equation = (a * d) - (b * c)
lin_equ(valid_equation)
