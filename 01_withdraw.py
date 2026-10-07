class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")
account1 = BankAccount("Rudra",50000)
account1.withdraw(10000)
print(account1.balance)
account1.withdraw(60000)
print(account1.balance)