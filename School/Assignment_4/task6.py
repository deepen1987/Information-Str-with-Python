# CS521 - A2
# Deependrasingh Shekhawat
# Script for Count Keywords

import os.path

keywords = {'and', 'as', 'assert', 'break', 'class', 'continue', 'def',
            'elif', 'else', 'except', 'False', 'finally', 'for', 'from', 'global',
            'if', 'import', 'is', 'in', 'lambda', 'None', 'nonlocal', 'not', 'or',
            'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield'}

fileName = input("Enter a Python Source code filename: ").strip()

if os.path.isfile(fileName):
    with open(fileName, 'r') as f:
        file = f.read().split()
    print(f"The keyword in {fileName} are", end=" ")

    total = 0
    keywordArray = []
    for i in file:
        if i in keywords:
            total += 1
            keywordArray.append(i)

    for i in list(set(keywordArray)):
        print(f"'{i}'", end=" ")

    print(f",total count of keywords is {total}")

else:
    print(f"File {fileName} does not exist")
