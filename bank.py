class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited ₹{amount}. \nCurrent balance: ₹{self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Current balance: ₹{self.__balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.__balance}")


account = BankAccount("User", 1000)

while True:
    print("\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        amt = float(input("Enter amount: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter amount: "))
        account.withdraw(amt)
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        break
    else:
        print("Invalid choice")
