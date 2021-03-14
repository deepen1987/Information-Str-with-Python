# CS521 - A2
# Deependrasingh Shekhawat
# Script for Distinct numbers

numbers = list(map(int, input("Enter ten numbers :").split(" ")))
distinctNumbers = []

print("The distinct numbers are: ", end="")
for item in numbers:
    if item not in distinctNumbers:
        distinctNumbers.append(item)
        print(f"{item}", end=" ")
