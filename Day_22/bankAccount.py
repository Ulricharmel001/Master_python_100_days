# Bank account simulation
class BankAccount:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
# Deposit
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")
# withdrawal feature
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the current balance.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Account Holder: {self.account_holder}, Balance: ${self.balance}"

    def show_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: ${self.balance}")

    # main program

account = {}

def create_account():
    name = input("Enter account holder's name: ").strip()
    initial_deposit = float(input("Enter initial deposit amount: "))
    account_number = len(account) + 1  # Simple account number generation
    new_account = BankAccount(account_number, name, initial_deposit)
    account[account_number] = new_account
    print(f"Account created successfully! Account Number: {account_number}")



def access_account():
    account_number = int(input("Enter your account number: "))
    if account_number in account:
        acc = account[account_number]
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Show Account Info")
            print("5 Transfer Fund")
            print("6. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                acc.deposit(amount)
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                acc.withdraw(amount)
            elif choice == '3':
                print(f"Current Balance: ${acc.get_balance()}")
            elif choice == '4':
                acc.show_account_info()
            elif choice == '5':
                transfer_funds()
            elif choice == '6':
                break
            else:
                print("Invalid option. Please try again.")
    else:
        print("Account not found.")

# challenge task : inter account transfer feature

def transfer_funds():
    from_account_number = int(input("Enter your account number: "))
    to_account_number = int(input("Enter the recipient's account number: "))
    amount = float(input("Enter the amount to transfer: "))

    if from_account_number in account and to_account_number in account:
        from_account = account[from_account_number]
        to_account = account[to_account_number]

        if 0 < amount <= from_account.get_balance():
            from_account.withdraw(amount)
            to_account.deposit(amount)
            print(f"Transferred ${amount} from Account {from_account_number} to Account {to_account_number}.")
        else:
            print("Transfer amount must be positive and less than or equal to the current balance.")
    else:
        print("One or both account numbers are invalid.")


# run the program
while True: 
    print("\n--- Bank Account Simulation ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")
    main_choice = input("Choose an option: ")
    if main_choice == '1':
        create_account()
    elif main_choice == '2':
        access_account()
    elif main_choice == '3':
        transfer_funds()
    elif main_choice == '4':
        print("Exiting the program.")
        break
    else:
        print("Invalid option. Please try again.")