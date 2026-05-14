import requests
import json
from datetime import datetime
from pathlib import Path
import yaml

from src.utils.logger import logger

with open("config/settings.yaml") as file:
    config = yaml.safe_load(file)

BRONZE_PATH = config["paths"]["bronze"]

API_URL = (
    "http://localhost:5000/api/transactions"
)

def collect_data():

    response = requests.get(API_URL)

    transactions = response.json()

    timestamp = datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

    filename = (
        f"{BRONZE_PATH}/transactions_{timestamp}.json"
    )

    Path(BRONZE_PATH).mkdir(
        parents=True,
        exist_ok=True
    )

    with open(filename, "w") as file:

        json.dump(
            transactions,
            file,
            indent=4
        )

    logger.info(
        f"Collected API data into bronze: {filename}"
    )

if __name__ == "__main__":
    collect_data()