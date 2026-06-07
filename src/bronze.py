import pandas as pd
from pathlib import Path

RAW_PATH = Path("data/raw")
BRONZE_PATH = Path("data/bronze")

BRONZE_PATH.mkdir(parents=True, exist_ok=True)


def json_to_parquet(json_file, parquet_file):

    df = pd.read_json(json_file)

    df.to_parquet(
        parquet_file,
        index=False
    )

    print(f"Arquivo salvo: {parquet_file}")


def main():

    datasets = [
        "products",
        "users",
        "carts"
    ]

    for dataset in datasets:

        json_file = RAW_PATH / f"{dataset}.json"

        parquet_file = BRONZE_PATH / f"{dataset}.parquet"

        json_to_parquet(
            json_file,
            parquet_file
        )

    print("Bronze concluída!")


if __name__ == "__main__":
    main()