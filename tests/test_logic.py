import sys
import os
import pandas as pd

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.helpers import (
    validate_status,
    standardize_currency,
    remove_duplicate_transactions
)

def test_validate_status():
    assert validate_status("SUCCESS") == True
    assert validate_status("FAILED") == True
    assert validate_status("INVALID") == False

def test_standardize_currency():
    result = standardize_currency(100.567)
    assert result == 100.57

def test_remove_duplicates():
    data = {
        "transaction_id": [1, 1, 2],
        "amount": [100, 100, 200]
    }
    df = pd.DataFrame(data)

    cleaned_df = remove_duplicate_transactions(df)

    assert len(cleaned_df) == 2