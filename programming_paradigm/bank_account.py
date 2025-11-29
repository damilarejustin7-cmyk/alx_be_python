# Simple bank account implementation using Object-Oriented Programming (OOP) paradigm

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Wthdrew: ${amount:.2f}")  # Added print statement for withdrawal
            return True
        else:
            print("Insufficient funds.")      # Added print statement for insufficient funds
            return False

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
