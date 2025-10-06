class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def view_profile(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")

class Manager(Employee):
    def approve_loan(self, account, amount):
        if account.is_active:
            print(f"Loan of ₹{amount} approved for {account.name} (Account: {account.account_number})")
        else:
            print("Cannot approve loan for inactive account.")
