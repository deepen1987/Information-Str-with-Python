# abc = [1, 4, 5, 6]
#
# stack = []
# for item in abc:
#     stack.append(item)
# print(stack)
#
# stack.pop(-1)
#
# print(stack)
#
# # list comprehension
#
# price = [kbc for kbc in abc if kbc > 4]
# print(price)
#
# kimat = dict(x=1, y=2)
#
# for key, value in kimat.items():
#     print(key, value)
#
# a = {x * 4 for x in range(5)}
# print(f"created a set using comprehension {a}")
#
# b = {y: y * 4 for y in range(5)}
# print(f"created a dict using comprehension {b}")

a = [1, 2]
b = (1, 4)
c = dict(x=6, y=8)
d = (3, 5, 7)
e = {9, 8, 2}
print(a)
print(b)
print(c)
print(d)
print(e)
q = [*a]
w = (*b, *d)
print(q)
print(w)
