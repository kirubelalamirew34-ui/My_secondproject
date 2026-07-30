class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance   

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def statement(self):
        print(f"{self.owner}: {self.balance} ETB")


# Create an account
a = Account("Almaz", 1500)
b = Account("kirubel", 1800)
c = Account("Alamirew", 2000)

# Deposit money
a.deposit(500)
b.deposit(600)
c.deposit(900)

# Withdraw money
a.withdraw(200)
c.withdraw(600)

# Deposit money
a.deposit(2000)
b.deposit(700)

# Display account balance
a.statement()
b.statement()
c.statement()