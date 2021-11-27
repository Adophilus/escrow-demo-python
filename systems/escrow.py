from models import Trader, Buyer, Seller, Product, Transaction
import helpers
import litedb

class Escrow (object):
    def __init__ (self, database: litedb.database, transaction_fee: float = 10.00):
        self.database = database
        self.__transaction_fee = transaction_fee
        self._account = helpers.Account()

    @property
    def account (self) -> helpers.Account:
        return self._account

    @property
    def transaction_fee (self) -> float:
        return self.__transaction_fee

    def transact (self, buyer: Buyer, seller: Seller, product: Product) -> Transaction:
        if not (seller.hasProductInStock(product)):
            raise Exception(f"{product.name} not in {seller.first_name}'s stock")
        if not (buyer.getAccountBalance() >= product.price):
            raise Exception(f"{buyer.first_name} does not have the required balance to complete the transaction")
        buyer.transferFunds(product.price, self)
        self.transferFunds(product.price - self.transaction_fee, buyer)
        transaction = Transaction(buyer, seller, product)
        self.database.insert(transaction)
        return transaction

    def transferFunds (self, amount: float, trader: Trader) -> bool:
        return self.account.transferFunds(amount, trader.account)
