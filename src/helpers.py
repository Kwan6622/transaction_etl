from datetime import datetime
import pandas as pd

def generate_timestamp():

    return datetime.now().strftime(
        "%Y%m%d_%H%M%S"
    )

def standardize_currency(value):

    return round(float(value), 2)

def validate_status(status):

    allowed_statuses = [
        "SUCCESS",
        "FAILED",
        "PENDING"
    ]

    return status in allowed_statuses

def clean_column_names(df):

    df.columns = [
        col.lower().strip().replace(" ", "_")
        for col in df.columns
    ]

    return df

def remove_duplicate_transactions(df):

    return df.drop_duplicates(
        subset=["transaction_id"]
    )

def convert_timestamp_column(df):

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    return df