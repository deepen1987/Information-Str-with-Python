S = input().strip()

try:
    print(int(S))
except (ValueError, ArithmeticError):
    print("Bad String")
