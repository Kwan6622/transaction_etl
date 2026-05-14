import pandas as pd
import yaml
import duckdb
from src.utils.logger import logger

# Load Configuration
with open("config/settings.yaml") as file:
    config = yaml.safe_load(file)

SILVER_PATH = config["paths"]["silver"]
DUCKDB_PATH = config["database"]["db_file"]

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

    # 2. Connect to the persistent DuckDB file
    conn = duckdb.connect(DUCKDB_PATH)
    logger.info(f"Connected to DuckDB at {DUCKDB_PATH}")

    # 3. Create the Detailed Table (Fact Table)
    conn.sql("CREATE OR REPLACE TABLE gold_transactions AS SELECT * FROM df")
    logger.info("Loaded 'gold_transactions' table (contains transaction_id & username).")

    # 4. Create the Summary Table
    # Recreate your grouping logic
    gold_summary_df = (
        df.groupby("status")["amount"]
        .sum()
        .reset_index()
    )
    
    conn.sql("CREATE OR REPLACE TABLE gold_status_summary AS SELECT * FROM gold_summary_df")
    logger.info("Loaded 'gold_status_summary' table.")

    # 5. Close connection
    conn.close()
    logger.info("Gold layer processing complete.")

if __name__ == "__main__":
    create_gold_tables()