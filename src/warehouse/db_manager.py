import duckdb
import yaml

from src.utils.logger import logger

with open("config/settings.yaml") as file:
    config = yaml.safe_load(file)

DB_FILE = config["database"]["db_file"]
GOLD_PATH = config["paths"]["gold"]

def load_gold_to_warehouse():

    conn = duckdb.connect(DB_FILE)

    # Load gold_transactions
    conn.execute(f"""
        CREATE OR REPLACE TABLE
        gold_transactions AS
        SELECT *
        FROM read_parquet(
            '{GOLD_PATH}/gold_transactions.parquet'
        )
    """)
    logger.info("Loaded 'gold_transactions' into DuckDB warehouse.")

    # Load gold_status_summary
    conn.execute(f"""
        CREATE OR REPLACE TABLE
        gold_status_summary AS
        SELECT *
        FROM read_parquet(
            '{GOLD_PATH}/gold_status_summary.parquet'
        )
    """)
    logger.info("Loaded 'gold_status_summary' into DuckDB warehouse.")

    conn.close()

if __name__ == "__main__":
    load_gold_to_warehouse()