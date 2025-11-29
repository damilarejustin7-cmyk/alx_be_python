# Simple bank account implementation using Object-Oriented Programming (OOP) paradigm

class InsufficientFundsError(Exception):
    """Custom exception raised for withdrawals exceeding the available balance."""
    pass

class BankAccount:
    def __init__(self, initial_balance=0.0):
        """Initializes the account with a starting balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.balance = initial_balance 

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")

        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            raise InsufficientFundsError("Cannot withdraw: Insufficient funds.")

    def display_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")
