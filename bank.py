class Bank:
    def __init__(self, acc_no, acc_holder, acc_balance=0):
        self.acc_no =  acc_no
        self.acc_holder = acc_holder
        self.acc_balance = acc_balance

    def deposit(self,amount):
        if amount > 0:
            self.acc_balance += amount
        print(f"Amount Deposited: {amount}$")
        print(f"New Balance: {self.acc_balance}$")

    def withdraw(self,amount):
        if amount > 0:
            if (amount<=self.acc_balance):
                self.acc_balance = self.acc_balance - amount
                print(f"Money withdrawn: {amount}$")
                print(f"New Balance: {self.acc_balance}$")

            else:
                print("Insufficient Balance")

        else:
            print("Amount should be positive")


    def showBalance(self):
        print(f"Account Holder Name: {self.acc_holder}")
        print(f"Account No: {self.acc_no}")
        print(f"Account Balance: {self.acc_balance}$")
    


acc1 = Bank(123460,"John")
print(acc1.showBalance())
print()
acc1.deposit(50000)
print()
print(acc1.showBalance())
print()
acc1.withdraw(20000)
print()
print(acc1.showBalance())
print()
acc1.withdraw(40000)