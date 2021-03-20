# CS521 - A2
# Deependrasingh Shekhawat
# Script for sum of integer

def sumDigits(n):
    total = 0
    str1 = ""
    for i in n:
        if str1:
            str1 += " + "
        str1 += i
        total += int(i)
    str1 += " = "
    print(str1, total)


sumDigits(input("Enter number: "))
