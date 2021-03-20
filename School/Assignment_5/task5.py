# CS521 - A2
# Deependrasingh Shekhawat
# Script for GCD

def gcd(m, n):
    if m % n == 0:
        print(f"gcd(m, n) is {n}")
    else:
        gcd(n, m % n)


first, second = map(int, input("Enter 2 numbers: ").split(" "))

gcd(first, second)
