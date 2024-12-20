class ATM:
    def __init__(self, Account_holder, balance=0):
        self.Account_holder = Account_holder
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount: {amount}")

    def withdrawal(self, amount):
        if amount > self.balance:
            print(f"Insufficient balance! Available balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"Withdrawal amount: {amount}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
name = input("Enter the user name: ")
account = ATM(name, 100)  

print(f"Account Holder: {account.Account_holder}")
account.deposit(1000)
account.withdrawal(500)  
account.check_balance()

