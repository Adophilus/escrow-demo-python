from models import Buyer

def test_buyer ():
    buyer = Buyer("adophilus", "brian", 100)
    assert buyer.first_name == "adophilus"
    assert buyer.last_name == "brian"
    assert buyer.getAccountBalance() == float(100)
