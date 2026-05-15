import pandas as pd
import yaml
from src.utils.logger import logger

# Load Configuration
with open("config/settings.yaml") as file:
    config = yaml.safe_load(file)

SILVER_PATH = config["paths"]["silver"]
GOLD_PATH = config["paths"]["gold"]

def create_gold_tables():
    # 1. Read the clean data from Silver
    silver_file = f"{SILVER_PATH}/transactions.parquet"
    try:
        df = pd.read_parquet(silver_file)
    except FileNotFoundError:
        logger.error(f"Silver file not found at {silver_file}")
        return

    if df.empty:
        logger.info("No data found to transform.")
        return

    # 2. Save the Detailed Table (Fact Table) to Gold
    transactions_gold_file = f"{GOLD_PATH}/gold_transactions.parquet"
    df.to_parquet(transactions_gold_file, index=False)
    logger.info(f"Saved 'gold_transactions' to {transactions_gold_file}")

    # 3. Create the Summary Table and save to Gold
    gold_summary_df = (
        df.groupby("status")["amount"]
        .sum()
        .reset_index()
    )
    
    summary_gold_file = f"{GOLD_PATH}/gold_status_summary.parquet"
    gold_summary_df.to_parquet(summary_gold_file, index=False)
    logger.info(f"Saved 'gold_status_summary' to {summary_gold_file}")

    logger.info("Gold layer processing complete.")

if __name__ == "__main__":
    create_gold_tables()