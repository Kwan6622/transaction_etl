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
from src.utils.logger import log_action_time

def main():

    with log_action_time("Data Collection"):
        collect_data()

    with log_action_time("Transform Bronze to Silver"):
        transform_to_silver()

    with log_action_time("Create Gold Tables"):
        create_gold_tables()

    with log_action_time("Load Gold to Warehouse"):
        load_gold_to_warehouse()

if __name__ == "__main__":
    main()