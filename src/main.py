from src.ingestion.collector import collect_data
from src.transformation.bronze_to_silver import (
    transform_to_silver
)
from src.transformation.silver_to_gold import (
    create_gold_tables
)
from src.warehouse.db_manager import (
    load_gold_to_warehouse
)

def main():

    collect_data()

    transform_to_silver()

    create_gold_tables()

    load_gold_to_warehouse()

if __name__ == "__main__":
    main()