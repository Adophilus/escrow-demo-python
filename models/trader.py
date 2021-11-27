import helpers

class Trader (object):
    def __init__ (self, first_name: str, last_name: str, balance: float = 0.00):
        self.first_name = first_name
        self.last_name = last_name
        self._account = helpers.Account(balance)

    @property
    def account (self):
        return self._account

    def getAccountBalance (self):
        return self.account.balance

    def transferFunds (self, amount: float, trader: "Trader"):
        return self.account.transferFunds(amount, trader.account)

    def __repr__ (self) -> str:
        return str(self.__dict__)
