# CS521 - A2
# Deependrasingh Shekhawat
# Script for pentagonal numbers

def getPentagonalNumber(n):
    return n * (3 * n - 1) / 2


count = 0
for i in range(1, 101):
    print(round(getPentagonalNumber(i)), end=" ")
    count += 1
    if count == 10:
        print()
        count = 0
