# class Count:
#
#     def __init__(self, count=0):
#         self.__count = count
#
#
# a = Count(2)
# b = Count(2)
# print(id(a) == id(b), end=' ')
#
# c = 'hello'
# d = 'hello'
# print(id(c) == id(d))

#

# i = 1
#
# while True:
#
#     if i % 5 == 0:
#         break
#
#     print(i, end=" ")
#
#     i += 1

#

# L1 = [1, 2, 3, 4]
#
# L2 = L1
#
# L3 = L1.copy()
#
# L4 = list(L1)
#
# L1[0] = [5]
#
# print(L1, L2, L3, L4)

#

# T1 = (1)
#
# T2 = (3, 4)
#
# T1 += 5
#
# print(T1)
#
# print(T1 + T2)

#

# def foo(x):
#     x = ['def', 'abc']
#
#     return id(x)
#
#
# q = ['abc', 'def']
#
# print(id(q) == foo(q))

#

# line = "What will have so will"
#
# L = line.split('a')
#
# for i in L:
#     print(i, end=' ')

#

# i = 0
#
#
# def change(i):
#     i = i + 1
#
#     return i
#
#
# change(1)
#
# print(i)

# temp = dict()
#
# temp['key1'] = {'key1': 44, 'key2': 566}
#
# temp['key2'] = [1, 2, 3, 4]
#
# for (key, values) in temp.items():
#     print(values, end="")

#

# for i in range(2)[::-1]:
#     print(i, end=" ")

#

# set1 = {1, 2, 3}
#
# set2 = set1.copy()
#
# set2.add(4)
#
# print(set1)


#

# a = True
# b = False
# c = False
#
# if a or b and c:
#
#     print("Tea")
#
# else:
#
#     print("Coffee")

#

# a = [(a, b) for a in range(3) for b in range(a)]
# print(a)

#

# x = 1
# y = 2
# z = 3
#
#
# def FMA(x, y):
#     z = multiply(x, y)
#
#     x = x + z
#
#     return x
#
#
# def multiply(x, y):
#     x = x * y
#
#     return x
#
#
# z = FMA(1, 1)
#
# print(x, y, z)

#

# data = [2, 3, 9]
#
# temp = [[x for x in[data]] for x in range(3)]
#
# print (temp)

#

L1 = []

L1.append([1, [2, 3, 4], 5])

L1.extend((7, 8, 9))

print(L1[0][1][1] + L1[2])
