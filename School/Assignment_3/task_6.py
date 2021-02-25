# CS521 - A2
# Deependrasingh Shekhawat
# Script for performing file operations

import os

file_name = input("Enter a filename with extension: ")
current_string = input("Enter the string to be removed: ")

with open(file_name, 'r') as f:
    file = f.read()
    file = file.replace(current_string.capitalize(), '')
    file = file.replace(current_string.lower(), '')
    file = file.replace(current_string.upper(), '')
with open(file_name, 'w') as f:
    f.write(file)
    print("Done")
