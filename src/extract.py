import requests
import json
from pathlib import Path

RAW_PATH = Path("data/raw")

RAW_PATH.mkdir(parents=True, exist_ok=True)


def extract_endpoint(url):
    response = requests.get(url, timeout=30)

    response.raise_for_status()

    return response.json()


def save_json(data, filename):

    filepath = RAW_PATH / filename

    with open(filepath, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )


def run_extract():

    endpoints = {
        "products.json": "https://fakestoreapi.com/products",
        "users.json": "https://fakestoreapi.com/users",
        "carts.json": "https://fakestoreapi.com/carts"
    }

    for filename, url in endpoints.items():

        print(f"Extraindo {filename}")

        data = extract_endpoint(url)

        save_json(data, filename)

    print("Extract concluído!")


if __name__ == "__main__":
    run_extract()