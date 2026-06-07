import pandas as pd

#PRODUCTS
products = pd.read_parquet("data/bronze/products.parquet")

products["rating_rate"] = products["rating"].apply(
    lambda x: x["rate"]
)

products["rating_count"] = products["rating"].apply(
    lambda x: x["count"]
)

products = products.drop(columns=["rating"])

print(products.head())
print(products.columns)


# USERS
users = pd.read_parquet("data/bronze/users.parquet")

users["firstname"] = users["name"].apply(
    lambda x: x["firstname"]
)

users["lastname"] = users["name"].apply(
    lambda x: x["lastname"]
)

users["city"] = users["address"].apply(
    lambda x: x["city"]
)

users["street"] = users["address"].apply(
    lambda x: x["street"]
)

users["number"] = users["address"].apply(
    lambda x: x["number"]
)

users["zipcode"] = users["address"].apply(
    lambda x: x["zipcode"]
)

users["latitude"] = users["address"].apply(
    lambda x: x["geolocation"]["lat"]
)

users["longitude"] = users["address"].apply(
    lambda x: x["geolocation"]["long"]
)

users = users.drop(
    columns=[
        "name",
        "address",
        "__v",
        "password"
    ]
)

print("\nUSERS CLEAN")
print(users.head())

print("\nCOLUNAS")
print(users.columns)

# CARTS
carts = pd.read_parquet("data/bronze/carts.parquet")

cart_items = []

for _, row in carts.iterrows():

    cart_id = row["id"]

    user_id = row["userId"]

    for product in row["products"]:

        cart_items.append({
            "cart_id": cart_id,
            "user_id": user_id,
            "product_id": product["productId"],
            "quantity": product["quantity"]
        })

cart_items = pd.DataFrame(cart_items)

print("\nCART ITEMS")
print(cart_items.head())

print("\nSHAPE")
print(cart_items.shape)

# CRIAR DIRETÓRIO
from pathlib import Path

SILVER_PATH = Path("data/silver")

SILVER_PATH.mkdir(
    parents=True,
    exist_ok=True
)


products.to_parquet(
    SILVER_PATH / "products_clean.parquet",
    index=False
)

users.to_parquet(
    SILVER_PATH / "users_clean.parquet",
    index=False
)

cart_items.to_parquet(
    SILVER_PATH / "cart_items.parquet",
    index=False
)


carts_clean = carts.drop(
    columns=[
        "products",
        "__v"
    ]
)

carts_clean.to_parquet(
    SILVER_PATH / "carts_clean.parquet",
    index=False
)