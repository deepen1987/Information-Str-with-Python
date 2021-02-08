def find(num1, num2):

    return num1 * 3 == num2


for i in range(10000, 100000):
    if find(int(("1" + str(i))), int((str(i) + "1"))):
        print(int(("1" + str(i))), int((str(i) + "1")))