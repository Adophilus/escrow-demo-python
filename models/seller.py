from models.product import Product
from models.trader import Trader

class Seller (Trader):
    def __init__ (self, first_name: str, last_name: str, products: list[Product]):
        super().__init__(first_name, last_name)
        self.__products = products
    
    @property
    def products (self) -> list[Product]:
        return list(self.__products)

    def hasProductInStock (self, product: Product) -> bool:
        for my_product in self.__products:
            if (my_product.name == product.name):
                return bool(my_product.stock)
        return False
