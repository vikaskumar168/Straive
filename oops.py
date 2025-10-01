# Define a Class
class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method
    def drive(self):
        print(f"{self.brand} {self.model} is driving...")


# Create Objects
car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

# Access Attributes
print(car1.brand)  # Tesla
print(car2.model)  # Corolla

# Call Method
car1.drive()  # Tesla Model S is driving...











Write a method transfer(self, amount, target_account) to transfer money from one account to another.
Modify SavingsAccount to add interest calculation (e.g., 4% annually).
Add a transaction history feature that logs deposits and withdrawals for each account.
Create a menu-driven program that allows the user to:
Create a new account
Deposit money
Withdraw money
View account details
Exit
Implement an overdraft limit for CurrentAccount where users can withdraw more than their balance up to a limit.
Add a method close_account() to mark an account as inactive.
Create multiple account objects and store them in a list or dictionary. Write code to search an account by account number.
Extend the project so that every account has a unique account number generator.
Implement a Base class Employee (for bank staff) and a Manager class that can approve loans for customers.
How would you make this system scalable if thousands of users were using it? (Hint: think about data storage & design).
