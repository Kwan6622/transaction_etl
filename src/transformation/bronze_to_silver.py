import pandas as pd
import glob
import json
import yaml

from src.utils.logger import logger

with open("config/settings.yaml") as file:
    config = yaml.safe_load(file)

BRONZE_PATH = config["paths"]["bronze"]
SILVER_PATH = config["paths"]["silver"]

def transform_to_silver():

    files = glob.glob(
        f"{BRONZE_PATH}/*.json"
    )

    all_data = []

    for file in files:

        with open(file, "r") as f:
            data = json.load(f)
            all_data.extend(data)

    df = pd.DataFrame(all_data)

    if df.empty:
        logger.info("No data found to transform.")
        return

    # Cleaning
    df.drop_duplicates(
        subset=["transaction_id"],
        inplace=True
    )

    df["amount"] = df["amount"].astype(float)

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    output_file = (
        f"{SILVER_PATH}/transactions.parquet"
    )

    from pathlib import Path
    Path(SILVER_PATH).mkdir(parents=True, exist_ok=True)

    df.to_parquet(
        output_file,
        index=False
    )

    logger.info(
        f"Silver parquet saved: {output_file}"
    )

if __name__ == "__main__":
    transform_to_silver()