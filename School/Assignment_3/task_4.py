# CS521 - A2
# Deependrasingh Shekhawat
# Script for Kg to Lbs

print(f"Kilograms\tPounds")
for kg in range(1, 200):
    if kg % 2 != 0:
        print(f"{kg}\t\t\t{round(kg * 2.2, 2)}")

