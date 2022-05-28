class Account (object):
    def __init__(self, balance: float = 0.00):
        self.balance = balance

    def transferFunds(self, amount: float, account: "Account") -> bool:
        amount = amount
        if not (self.withdraw(amount)):
            return False
        return account.deposit(amount)

    def withdraw(self, amount: float) -> bool:
        amount = amount
        if ((self.balance - amount) >= 0):
            self.balance -= amount
            return True

    def deposit(self, amount: float) -> bool:
        self.balance += amount
        return True
