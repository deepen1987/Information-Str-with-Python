"""
CS521 - A2
Deependrasingh Shekhawat

Script for calculating Total amount and Gratuity
"""

subtotal = float(input("Please enter subtotal: $"))
gratuity = int(input("Please enter gratuity: %")) / 100

gratuity *= subtotal

total = subtotal + gratuity

print(f"Your Total is ${total} and your total gratuity in ${gratuity}")

