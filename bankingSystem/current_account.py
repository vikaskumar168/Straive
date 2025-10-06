from account import Account

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
        self.logger.log(f"Withdraw: ₹{amount}")
