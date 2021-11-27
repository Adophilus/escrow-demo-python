from models.product import Product

class Commodity (Product):
    def __init__ (self, name: str, price: float):
        self.name = name
        self.price = price

    def __repr__ (self) -> str:
        return str(self.__dict__)
