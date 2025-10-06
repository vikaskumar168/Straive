from account import SavingsAccount, CurrentAccount

class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_type, name, initial_balance):
        if account_type == "savings":
            account = SavingsAccount(name, initial_balance)
        elif account_type == "current":
            account = CurrentAccount(name, initial_balance)
        else:
            print("Invalid account type.")
            return None
        self.accounts[account.account_number] = account
        print(f"Account created successfully. Account Number: {account.account_number}")
        return account

    def find_account(self, account_number):
        return self.accounts.get(account_number)

    def list_all_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return

        print("\n{:<12} {:<20} {:<12} {:<10}".format("Account No", "Name", "Balance", "Status"))
        for acc_num, account in self.accounts.items():
            print("{:<12} {:<20} ₹{:<10.2f} {:<10}".format(
                acc_num, account.name, account.balance, "Active" if account.is_active else "Closed"
            ))
