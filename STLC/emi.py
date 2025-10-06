class InsufficientBalanceError(Exception):
    pass

class Account:
    def __init__(self, owner, balance=0, annual_rate=0.05):
        self.owner = owner
        self.balance = balance
        self.annual_rate = annual_rate
        self.history = []  # Track transactions

        self._log_transaction("init", balance)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount
        self._log_transaction("deposit", amount)
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")
        self.balance -= amount
        self._log_transaction("withdraw", -amount)
        return self.balance

    def transfer(self, target_account, amount):
        if amount <= 0:
            raise ValueError("Transfer amount must be positive")
        if amount > self.balance:
            raise InsufficientBalanceError("Not enough balance")
        self.withdraw(amount)
        target_account.deposit(amount)
        self._log_transaction("transfer_out", -amount)
        target_account._log_transaction("transfer_in", amount)

    def calculate_annual_interest(self):
        return round(self.balance * self.annual_rate, 2)

    def calculate_compound_interest(self, years, compounding_frequency=1):
        P = self.balance
        r = self.annual_rate
        n = compounding_frequency
        t = years
        A = P * ((1 + r / n) ** (n * t))
        return round(A, 2)

    def _log_transaction(self, tx_type, amount):
        self.history.append({
            "type": tx_type,
            "amount": amount,
            "balance": self.balance
        })
