# CS521 - A2
# Deependrasingh Shekhawat
# Script for class for ATM

class Account:
    def __init__(self, id=0, balance=100.0):
        self.__id = id
        self.__balance = balance

    def get_id(self):
        return self.__id

    def get_balance(self):
        return self.__balance

    def withdraw(self, amt):
        self.__balance = self.__balance - amt

    def deposit(self, amt):
        self.__balance = self.__balance + amt


arr = []
for i in range(10):
    a = Account(i)
    arr.append(a)

while True:
    user_in = int(input("\nEnter an account id: "))
    for item in arr:
        if user_in == item.get_id():
            while True:
                print("""\nMain Menu
1: check balance
2: withdraw
3: deposit
4: exit\n""")
                menu = int(input("Enter a Choice: "))
                if menu == 1:
                    print(f"\nThe balance is ${item.get_balance()}")
                if menu == 2:
                    item.withdraw(float(input("\nEnter an amount to withdraw: $")))
                if menu == 3:
                    item.deposit(float(input("\nEnter an amount to deposit: $")))
                if menu == 4:
                    break
