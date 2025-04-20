
bank_data = {}

def create_account():
    name = input("Enter your name: ")
    account_number = input("Enter a new account number: ")

    if account_number in bank_data:
        print("Account number already exists. Try again.")
        return

    bank_data[account_number] = {"name": name, "balance": 0}
    print(f"Account created for {name} with account number {account_number}.")

def deposit():
    account_number = input("Enter your account number: ")

    if account_number in bank_data:
        amount = float(input("Enter amount to deposit: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        bank_data[account_number]["balance"] += amount
        print(f"Amount deposited. New balance: {bank_data[account_number]['balance']}")
    else:
        print("Account not found.")

def withdraw():
    account_number = input("Enter your account number: ")

    if account_number in bank_data:
        amount = float(input("Enter amount to withdraw: "))
        if amount <= 0:
            print("Amount must be greater than zero.")
            return
        if amount > bank_data[account_number]["balance"]:
            print("Insufficient balance.")
        else:
            bank_data[account_number]["balance"] -= amount
            print(f"Amount withdrawn. New balance: {bank_data[account_number]['balance']}")
    else:
        print("Account not found.")

def check_balance():
    account_number = input("Enter your account number: ")

    if account_number in bank_data:
        print(f"Account holder: {bank_data[account_number]['name']}")
        print(f"Current balance: {bank_data[account_number]['balance']}")
    else:
        print("Account not found.")

def main():
    while True:
        print("\n--- Welcome to Simple Bank ---")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using Simple Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
