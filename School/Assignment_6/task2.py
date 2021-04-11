# CS521 - A2
# Deependrasingh Shekhawat
# Script for class for Account with private members

class Account:
    def __init__(self, id=0, balance=100.0, annual_interest_rate=0.0):
        self.__id = id
        self.__balance = balance
        self.__annualInterestRate = annual_interest_rate

    def get_id(self):
        return self.__id

    def set_id(self, value):
        self.__id = value

    def get_balance(self):
        return self.__balance

    def set_balance(self, value):
        self.__balance = value

    def get_annual_interest_rate(self):
        return self.__annualInterestRate

    def set_annual_interest_rate(self, value):
        self.__annualInterestRate = value

    def get_monthly_interest_rate(self):
        return round((self.__annualInterestRate / 12), 2)

    def get_monthly_interest(self):
        return round(self.__balance * (self.__annualInterestRate / 12) / 100, 2)

    def withdraw(self, amt):
        self.__balance = self.__balance - amt

    def deposit(self, amt):
        self.__balance = self.__balance + amt


A = Account(23, 200, 24)

print(f"id:{A.get_id()}, balance: ${A.get_balance()} and Annual interest rate: {A.get_annual_interest_rate()}%")
A.deposit(250)

A.withdraw(50)
print(f"""The monthly interest rate is {A.get_monthly_interest_rate()}%. 
And the monthly interest will be ${A.get_monthly_interest()}\n""")

A.set_id(7)
A.set_annual_interest_rate(34)
A.set_balance(5000)
print(f"id:{A.get_id()}, balance: ${A.get_balance()} and Annual interest rate: {A.get_annual_interest_rate()}%")

print(f"""The monthly interest rate is {A.get_monthly_interest_rate()}%. 
And the monthly interest will be ${A.get_monthly_interest()}""")
