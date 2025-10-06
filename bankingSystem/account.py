import datetime
import uuid

class Account:
    def __init__(self, name, initial_balance=0):
        self.account_number = str(uuid.uuid4())[:8]
        self.name = name
        self.balance = initial_balance
        self.is_active = True
        self.transactions = []

    def deposit(self, amount):
        if not self.is_active:
            print("Account is closed.")
            return
        self.balance += amount
        self.transactions.append((datetime.datetime.now(), f"Deposit: ₹{amount}"))

    def withdraw(self, amount):
        if not self.is_active:
            print("Account is closed.")
            return
        if amount > self.balance:
            print("Insufficient funds.")
            return
        self.balance -= amount
        self.transactions.append((datetime.datetime.now(), f"Withdraw: ₹{amount}"))

    def transfer(self, amount, target_account):
        if not self.is_active or not target_account.is_active:
            print("One of the accounts is inactive.")
            return
        if amount > self.balance:
            print("Insufficient funds for transfer.")
            return
        self.withdraw(amount)
        target_account.deposit(amount)
        self.transactions.append((datetime.datetime.now(), f"Transfer to {target_account.account_number}: ₹{amount}"))
        target_account.transactions.append((datetime.datetime.now(), f"Transfer from {self.account_number}: ₹{amount}"))

    def close_account(self):
        self.is_active = False
        print(f"Account {self.account_number} closed.")

    def view_details(self):
        print(f"\nAccount Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")
        print(f"Status: {'Active' if self.is_active else 'Closed'}")
        print("Transaction History:")
        for t in self.transactions:
            print(f"  {t[0]} - {t[1]}")

class SavingsAccount(Account):
    def __init__(self, name, initial_balance=0, interest_rate=0.04):
        super().__init__(name, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if not self.is_active:
            return
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transactions.append((datetime.datetime.now(), f"Interest Applied: ₹{interest:.2f}"))

class CurrentAccount(Account):
    def __init__(self, name, initial_balance=0, overdraft_limit=5000):
        super().__init__(name, initial_balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if not self.is_active:
            print("Account is closed.")
            return
        if amount > self.balance + self.overdraft_limit:
            print("Overdraft limit exceeded.")
            return
        self.balance -= amount
        self.transactions.append((datetime.datetime.now(), f"Withdraw: ₹{amount}"))
