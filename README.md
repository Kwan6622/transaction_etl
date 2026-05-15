# Modern Lakehouse ETL Pipeline

A modern end-to-end Data Engineering project that simulates a real-world banking transaction system using a Medallion Lakehouse Architecture (Bronze → Silver → Gold).

This project demonstrates:

- API-based ingestion
- Data Lake design
- ELT pipelines
- DuckDB analytics warehouse
- Parquet processing
- Modular Python architecture
- Automated testing
- Git/GitHub workflow

---

# Architecture

```text
Mock Banking Website (Flask)
            │
            ▼
Transaction API Endpoint
            │
            ▼
Ingestion Layer
(collector.py)
            │
            ▼
Bronze Layer (Raw JSON)
            │
            ▼
Silver Layer (Cleaned Parquet)
            │
            ▼
Gold Layer (Business Aggregations)
            │
            ▼
DuckDB Warehouse
            │
            ▼
Analytics / BI Ready
```

---

# Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Mock banking transaction API |
| Faker | Fake transaction generation |
| Pandas | Data transformations |
| DuckDB | OLAP analytics warehouse |
| Parquet | Columnar storage format |
| Pytest | Automated testing |
| Git/GitHub | Version control |

---

# Project Structure

```text
cv_project1/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── config/
│   └── settings.yaml
│
├── data/
│   ├── 1_bronze/
│   ├── 2_silver/
│   └── 3_gold/
│
├── src/
│   ├── ingestion/
│   │   ├── producer.py
│   │   └── collector.py
│   │
│   ├── transformation/
│   │   ├── bronze_to_silver.py
│   │   └── silver_to_gold.py
│   │
│   ├── warehouse/
│   │   └── db_manager.py
│   │
│   └── utils/
│       ├── helpers.py
│       └── logger.py
│
├── tests/
│   ├── test_logic.py
│   └── test_transformation.py
│
├── requirements.txt
├── main.py
└── README.md
```

---

# Features

## Mock Banking Web Application

- Generate transactions using a web button
- Simulates an OLTP transactional system
- Exposes API endpoints for ingestion

## Bronze Layer

- Stores immutable raw JSON data
- Simulates Data Lake landing zone

## Silver Layer

- Cleans and validates data
- Removes duplicates
- Converts timestamps
- Standardizes schema
- Stores optimized Parquet files

## Gold Layer

- Creates business-ready aggregated datasets
- Supports analytics and BI workloads

## DuckDB Warehouse

- Loads analytical tables into DuckDB
- Supports fast OLAP-style queries

## Testing

- Automated tests using Pytest
- Data validation checks
- Transformation verification

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPO
cd cv_project1
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running The Project

## Start Flask Banking Application

```bash
python app/app.py
```

Open browser:

```text
http://localhost:5000
```

Press:

```text
Create Transaction
```

to generate transactions.

---

## Run ETL Pipeline

Open another terminal:

```bash
python main.py
```

---

# Running Tests

```bash
pytest
```

---

# DuckDB Warehouse Query Example

Open Python shell:

```python
import duckdb

conn = duckdb.connect(
    "data/3_gold/warehouse.duckdb"
)

print(
    conn.execute(
        "SELECT * FROM transaction_summary"
    ).fetchdf()
)
```

---

# Example Pipeline Flow

```text
User presses transaction button
            ↓
Flask API creates transaction
            ↓
Collector ingests API data
            ↓
Raw JSON saved to Bronze layer
            ↓
Transformation creates Silver Parquet
            ↓
Business aggregation creates Gold layer
            ↓
DuckDB warehouse updated
```

---

# Example Transaction JSON

```json
{
    "transaction_id": "e5c4d9f8",
    "customer_name": "John Smith",
    "amount": 1250.50,
    "currency": "USD",
    "status": "SUCCESS",
    "timestamp": "2026-05-14T15:30:45"
}
```

---

# Learning Objectives

This project demonstrates understanding of:

- Data Engineering fundamentals
- ELT architecture
- Medallion Lakehouse design
- Data Lake concepts
- OLTP vs OLAP systems
- Batch ingestion pipelines
- Parquet optimization
- Warehouse analytics
- Python modular architecture
- Automated testing

---

# Future Improvements

Planned upgrades:

- Docker containerization
- Apache Airflow orchestration
- Kafka streaming ingestion
- Cloud Data Warehouse (Snowflake/BigQuery)
- dbt transformations
- Great Expectations data quality checks
- Multi-currency conversion support
- CI/CD pipeline
- Cloud deployment (AWS/GCP/Azure)
- Dashboard visualization

---

# Why DuckDB?

DuckDB was chosen because it:

- Reads Parquet directly
- Is lightweight and fast
- Supports analytical SQL workloads
- Works well for local lakehouse architectures
- Simulates modern OLAP workflows

---

# Author

Quang Nguyen Duy

Built as a portfolio Data Engineering project focused on modern Lakehouse architecture and real-world ETL workflows.