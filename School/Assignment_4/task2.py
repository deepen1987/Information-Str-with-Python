# CS521 - A2
# Deependrasingh Shekhawat
# Script for Count Integers

integerAll = sorted(list(
    map(int, input("Enter integer between 1 and 100: ").split(" "))))

countDir = {}

for i in integerAll:
    if countDir.get(i):
        countDir[i] = countDir[i] + 1
    else:
        countDir[i] = 1

for key in countDir:
    if countDir[key] > 1:
        print(f"{key} occurs {countDir[key]} times")
    else:
        print(f"{key} occurs {countDir[key]} time")
