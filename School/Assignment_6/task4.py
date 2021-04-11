# CS521 - A2
# Deependrasingh Shekhawat
# Script for class for Linear Equation

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def get_a(self):
        return self.__a

    def get_b(self):
        return self.__b

    def get_c(self):
        return self.__c

    def get_d(self):
        return self.__d

    def get_e(self):
        return self.__e

    def get_f(self):
        return self.__f

    def is_solvable(self):
        if (self.__a * self.__d) - (self.__b * self.__c) != 0:
            return True
        else:
            return False

    def get_x(self):
        return ((self.__e * self.__d) - (self.__b * self.__f)) / ((self.__a * self.__d) - (self.__b * self.__c))

    def get_y(self):
        return ((self.__a * self.__f) - (self.__e * self.__c)) / ((self.__a * self.__d) - (self.__b * self.__c))


arr = list(map(int, input("Enter Values for a,b,c,d,e and f: ").split(" ")))

lineq = LinearEquation(arr[0], arr[1], arr[2], arr[3], arr[4], arr[5])

print(f"""a:{lineq.get_a()}
b:{lineq.get_b()}
c:{lineq.get_c()}
d:{lineq.get_d()}
e:{lineq.get_e()}
f:{lineq.get_f()}\n""")

if lineq.is_solvable():
    print(f"The equation is solvable: {lineq.is_solvable()}")
    print(f"x: {lineq.get_x()} and y:{lineq.get_y()}")
else:
    print("The equation has no solution")
