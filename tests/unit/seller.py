from models import Seller

def test_seller ():
    seller = Seller("john", "doe", 0)
    assert seller.first_name == "john"
    assert seller.last_name == "doe"
    assert seller.getAccountBalance() == float(0)
