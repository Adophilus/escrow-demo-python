from models.trader import Trader
from models.commodity import Commodity

class Buyer (Trader):
    commodities = []

    def addCommodity (self, commodity: Commodity):
        self.commodities.append(commodity)
        return True
