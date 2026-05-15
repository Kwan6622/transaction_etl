from flask import Flask
from flask import render_template
from flask import jsonify
from faker import Faker

import uuid
import random
from datetime import datetime

app = Flask(__name__)

fake = Faker()

# Simulated transaction storage
transactions = []

def generate_transaction():

    transaction = {
        "transaction_id": str(uuid.uuid4()),
        "timestamp": datetime.now().isoformat(),
        "customer_name": fake.name(),
        "amount": round(
            random.uniform(10, 5000),
            2
        ),
        "currency": "USD",
        "status": random.choice(
            ["SUCCESS", "FAILED", "PENDING"]
        )
        
    }

    transactions.append(transaction)

    return transaction

# Main Website
@app.route("/")
def home():

    return render_template(
        "index.html",
        transaction_count=len(transactions)
    )

# Button Action
@app.route("/create_transaction")
def create_transaction():

    transaction = generate_transaction()

    return jsonify({
        "message": "Transaction Created",
        "transaction": transaction,
        "total_count": len(transactions) # Added this to return the updated count
    })

# API Endpoint for ETL ingestion
@app.route("/api/transactions")
def get_transactions():

    return jsonify(transactions)

if __name__ == "__main__":

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )