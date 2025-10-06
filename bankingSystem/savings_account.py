from account import Account

class SavingsAccount(Account):
    def __init__(self, name, initial_balance=0, interest_rate=0.04):
        super().__init__(name, initial_balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        if not self.is_active:
            return
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.logger.log(f"Interest Applied: ₹{interest:.2f}")
