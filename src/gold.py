import pandas as pd
from pathlib import Path

SILVER_PATH = Path("data/silver")
GOLD_PATH = Path("data/gold")

GOLD_PATH.mkdir(
    parents=True,
    exist_ok=True
)


def run_gold():

    # =====================================
    # LOAD
    # =====================================

    products = pd.read_parquet(
        SILVER_PATH / "products_clean.parquet"
    )

    users = pd.read_parquet(
        SILVER_PATH / "users_clean.parquet"
    )

    cart_items = pd.read_parquet(
        SILVER_PATH / "cart_items.parquet"
    )

    # =====================================
    # KPI 1
    # Produtos por categoria
    # =====================================

    products_by_category = (
        products
        .groupby("category")
        .agg(
            total_products=("id", "count")
        )
        .reset_index()
    )

    # =====================================
    # KPI 2
    # Preço médio por categoria
    # =====================================

    avg_price_by_category = (
        products
        .groupby("category")
        .agg(
            avg_price=("price", "mean")
        )
        .reset_index()
    )

    # =====================================
    # KPI 3
    # Quantidade vendida por produto
    # =====================================

    product_sales = (
        cart_items
        .groupby("product_id")
        .agg(
            total_quantity=("quantity", "sum")
        )
        .reset_index()
    )

    # =====================================
    # KPI 4
    # Top produtos
    # =====================================

    top_products = (
        product_sales
        .merge(
            products,
            left_on="product_id",
            right_on="id",
            how="left"
        )
    )

    top_products = (
        top_products[
            [
                "product_id",
                "title",
                "category",
                "total_quantity"
            ]
        ]
        .sort_values(
            "total_quantity",
            ascending=False
        )
    )

    # =====================================
    # KPI 5
    # Top usuários
    # =====================================

    top_users = (
        cart_items
        .groupby("user_id")
        .agg(
            total_items=("quantity", "sum")
        )
        .reset_index()
    )

    top_users = (
        top_users
        .merge(
            users,
            left_on="user_id",
            right_on="id",
            how="left"
        )
    )

    top_users = (
        top_users[
            [
                "user_id",
                "firstname",
                "lastname",
                "city",
                "total_items"
            ]
        ]
        .sort_values(
            "total_items",
            ascending=False
        )
    )

    # =====================================
    # SAVE
    # =====================================

    products_by_category.to_parquet(
        GOLD_PATH / "products_by_category.parquet",
        index=False
    )

    avg_price_by_category.to_parquet(
        GOLD_PATH / "avg_price_by_category.parquet",
        index=False
    )

    product_sales.to_parquet(
        GOLD_PATH / "product_sales.parquet",
        index=False
    )

    top_products.to_parquet(
        GOLD_PATH / "top_products.parquet",
        index=False
    )

    top_users.to_parquet(
        GOLD_PATH / "top_users.parquet",
        index=False
    )

    print("Gold Layer concluída!")


if __name__ == "__main__":
    run_gold()