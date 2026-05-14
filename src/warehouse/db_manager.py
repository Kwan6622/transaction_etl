import duckdb
import yaml

from src.utils.logger import logger

with open("config/settings.yaml") as file:
    config = yaml.safe_load(file)

DB_FILE = config["database"]["db_file"]
GOLD_PATH = config["paths"]["gold"]

def load_gold_to_warehouse():

    conn = duckdb.connect(DB_FILE)

    conn.execute(f"""
        CREATE OR REPLACE TABLE
        transaction_summary AS
        SELECT *
        FROM read_parquet(
            '{GOLD_PATH}/transaction_summary.parquet'
        )
    """)

    logger.info(
        "Loaded gold layer into DuckDB warehouse"
    )

    conn.close()

if __name__ == "__main__":
    load_gold_to_warehouse()