import datetime
import uuid
from interfaces import IAccount

class TransactionLogger:
    def __init__(self):
        self.transactions = []

    def log(self, message):
        self.transactions.append((datetime.datetime.now(), message))

    def show(self):
        for t in self.transactions:
            print(f"  {t[0]} - {t[1]}")

class Account(IAccount):
    def __init__(self, name, initial_balance=0):
        self.account_number = str(uuid.uuid4())[:8]
        self.name = name
        self.balance = initial_balance
        self.is_active = True
        self.logger = TransactionLogger()

    def deposit(self, amount):
        if not self.is_active:
            print("Account is closed.")
            return
        self.balance += amount
        self.logger.log(f"Deposit: ₹{amount}")

    def withdraw(self, amount):
        if not self.is_active:
            print("Account is closed.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.logger.log(f"Withdraw: ₹{amount}")

    def transfer(self, amount, target_account: IAccount):
        if not self.is_active or not target_account.is_active:
            print("One of the accounts is inactive.")
            return
        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return
        self.withdraw(amount)
        target_account.deposit(amount)
        self.logger.log(f"Transfer to {target_account.account_number}: ₹{amount}")
        target_account.logger.log(f"Transfer from {self.account_number}: ₹{amount}")

    def close_account(self):
        self.is_active = False
        print(f"Account {self.account_number} closed.")

    def view_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")
        print(f"Status: {'Active' if self.is_active else 'Closed'}")
        print("Transaction History:")
        self.logger.show()
