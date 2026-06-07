import pandas as pd

products = pd.read_json("data/raw/products.json")
users = pd.read_json("data/raw/users.json")
carts = pd.read_json("data/raw/carts.json")

print(products.head())
print(users.head())
print(carts.head())