from faker import Faker
from models import Buyer, Seller, Product
from systems import Escrow
from main import run
from tests.integration.config import Config

def create_products () -> list[Product]:
    faker = Faker()
    return list(Product(faker.currency_code(), faker.random_int(100, 500), faker.random_int(0, 10)) for _ in range(3))

def display_buyer_commodities (buyer):
    print(f"Buyer: {buyer.first_name} {buyer.last_name}")
    for i, commodity in enumerate(buyer.commodities):
        print(f"{i+1}. {commodity.name} @{commodity.price}")

def display_seller_products (seller):
    print(f"Seller: {seller.first_name} {seller.last_name}")
    for i, product in enumerate(seller.products):
        print(f"{i+1}. {product.name}")
        print(f"\tprice: {product.price}")
        print(f"\tstock: {product.stock}")

def test_escrow ():
    database = run(Config)
    escrow = Escrow(database, 2)
    assert escrow.transaction_fee == float(2)
    buyer = Buyer(input("Enter your first name: "), input("Enter your last name: "), float(input("Enter your account balance: ")))
    seller = Seller("adophilus", "brian", products=create_products())
    for i, product in enumerate(seller.products):
        print(f"{i+1}. {product.name}")
        print(f"\tprice: {product.price}")
        print(f"\tstock: {product.stock}")
    user_selection = None
    while (user_selection not in range(len(seller.products))):
        user_selection = int(input("\nEnter a selection: ")) - 1
    assert bool(escrow.transact(buyer, seller, seller.products[user_selection])) == True
    print("Transaction successful!")
    display_buyer_commodities(buyer)
    print()
    display_seller_products(seller)
