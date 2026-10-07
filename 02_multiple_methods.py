# class BankAccount:
#     def __init__(self, name, balance):
#         self.name = name
#         self.balance = balance

#     def deposit(self, amount):
#         self.balance = self.balance + amount

#     def withdraw(self, amount):
#         if amount <= self.balance:
#             self.balance = self.balance - amount
#         else:
#             print("Insufficient balance")

#     def get_balance(self):
#         return self.balance

# account1 = BankAccount("Rudra", 50000)

# account1.deposit(10000)
# account1.withdraw(5000)
# account1.get_balance()

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance = self.balance + amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance = self.balance - amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.balance

account1 = BankAccount("Rudra",50000)

account1.deposit(10000)
account1.withdraw(5000)

result = account1.get_balance()

print(result)