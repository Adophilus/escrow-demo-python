class Product (object):
    def __init__ (self, name: str, price: float, stock: int = 1):
        self.name = name
        self.price = price
        self.stock = stock

    def __repr__ (self) -> str:
        return str(self.__dict__)
