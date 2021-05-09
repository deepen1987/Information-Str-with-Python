# x = 1
#
# def f1():
#
#     global x
#
#     x = x + 2
#
#     print(x)
#
# f1()
#
# print(x)

#

# def a():
#     pass
#
# print(a())

#

# def xfunction(n):
#
#     if n == 1:
#
#         return 1;
#
#     else:
#
#         return n + xfunction(n - 1)
#
# print(xfunction(4))

#

# def f1(x = 1, y = 2):
#
#     x = x + y
#
#     y += 1
#
#     print(x, y)
#
# f1()

#

# def f2(n, result):
#
#     if n == 0:
#
#         return 0
#
#     else:
#
#         return f2(n - 1, n + result)
#
# print(f2(2, 0))

#

# def nPrint(message, n):
#
#     while n > 0:
#
#         print(message)
#
#         n -= 1
#
# nPrint("a",4)

#

# x = 1
#
# def f1():
#
#     y = x + 2
#
#     print(y)
#
#
# f1()
#
# print(x)

#

# def factorial(n):
#
#     return n * factorial(n - 1)
#
# print(factorial(3))

#

def xfunction(n):

    if n == 1:

        return 1

    else:

        return n + xfunction(n - 1)