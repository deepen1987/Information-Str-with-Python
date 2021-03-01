# CS521 - A2
# Deependrasingh Shekhawat
# Script for verify SSN

ssn = input("Please enter you SSN in ddd-dd-dddd format: ")
valid = ssn.replace('-', '').isdigit() and len(ssn) == 11

if not valid:
    print("Invalid SSN1")
elif (ssn[3] == '-' and ssn[6] == '-') and valid:
    print("Valid SSN")
else:
    print("Invalid SSN2")
