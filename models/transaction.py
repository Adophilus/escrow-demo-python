from models.buyer import Buyer
from models.seller import Seller
from models.product import Product

class Transaction (object):
    def __init__ (self, buyer: Buyer, seller: Seller, product: Product):
        self.buyer = f"{buyer.first_name} {buyer.last_name}"
        self.seller = f"{seller.first_name} {seller.last_name}"
        self.product = product
    
    def __repr__ (self) -> str:
        return str(self.__dict__)
