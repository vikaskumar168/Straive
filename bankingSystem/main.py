from account import SavingsAccount
from bank import Bank

def main():
    bank = Bank()

    while True:
        print("\nBanking Option")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Account Details")
        print("5. Apply Interest (Savings Only)")
        print("6. Transfer Money")
        print("7. Close Account")
        print("8. List All Accounts")
        print("9. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            acc_type = input("Enter account type (savings/current): ").lower()
            balance = float(input("Enter initial deposit: "))
            bank.create_account(acc_type, name, balance)

        elif choice == "2":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                account.view_details()
            else:
                print("Account not found.")

        elif choice == "5":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if isinstance(account, SavingsAccount):
                account.apply_interest()
                print("Interest applied.")
            else:
                print("Not a savings account.")

        elif choice == "6":
            src = input("Enter your account number: ")
            dest = input("Enter target account number: ")
            amount = float(input("Enter amount to transfer: "))
            src_acc = bank.find_account(src)
            dest_acc = bank.find_account(dest)
            if src_acc and dest_acc:
                src_acc.transfer(amount, dest_acc)
            else:
                print("One or both accounts not found.")

        elif choice == "7":
            acc_num = input("Enter account number: ")
            account = bank.find_account(acc_num)
            if account:
                account.close_account()
            else:
                print("Account not found.")

        elif choice == "8":
            bank.list_all_accounts()

        elif choice == "9":
            print("Thank you for using the Vbank.")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
