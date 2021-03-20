# CS521 - A2
# Deependrasingh Shekhawat
# Script for sorted numbers

def displaySortedNumbers(num1, num2, num3):
    num = [num1, num2, num3]
    num.sort()
    print(f"The sorted numbers are ", end="")
    for i in num:
        print(i, end=" ")


first, second, third = map(int, input("Enter three numbers: ").split(" "))

displaySortedNumbers(first, second, third)
