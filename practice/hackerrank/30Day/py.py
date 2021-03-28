sc = [10,45,65]

total = (lambda x,y: x+y, sc)
print(total)

a = 20


def b():
    global a
    a = 25


print(a)
b()
print(a)