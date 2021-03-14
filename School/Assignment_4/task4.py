# CS521 - A2
# Deependrasingh Shekhawat
# Script for Sum of Matrix columns

def sumColumn(m, columnIndex):
    for i in range(columnIndex):
        total = 0
        for j in range(3):
            total += m[j][i]
        print(f"Sum of the elements for column {i} is {total}")


user = input(
    "Do you want to create a matrix press Y or use pre-defined matrix press N :").lower()

if user == "y":
    matrix3x4 = []
    for i in range(3):
        matrix3x4.append(list(
            map(int, input(f"Enter a 3-by-4 matrix row for row {i}: ").split(" "))))
else:
    matrix3x4 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

sumColumn(matrix3x4, len(matrix3x4[0]))
