from faker import Faker
import uuid
import random
from datetime import datetime

fake = Faker()

def generate_transaction():
    return {
        "transaction_id": str(uuid.uuid4()),
        "customer_name": fake.name(),
        "amount": round(random.uniform(10, 5000), 2),
        "currency": "USD",
        "status": random.choice(
            ["SUCCESS", "FAILED", "PENDING"]
        ),
        "timestamp": datetime.now().isoformat()
    }