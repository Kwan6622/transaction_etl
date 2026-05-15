import pandas as pd
import pytest
from unittest.mock import patch, MagicMock

from src.transformation.bronze_to_silver import transform_to_silver
from src.transformation.silver_to_gold import create_gold_tables

@patch("src.transformation.bronze_to_silver.glob.glob")
@patch("src.transformation.bronze_to_silver.pd.DataFrame.to_parquet")
def test_transform_to_silver_empty(mock_to_parquet, mock_glob):

    mock_glob.return_value = []
    
    transform_to_silver()
    
    mock_to_parquet.assert_not_called()

@patch("src.transformation.silver_to_gold.pd.read_parquet")
@patch("src.transformation.silver_to_gold.pd.DataFrame.to_parquet")
def test_create_gold_tables(mock_to_parquet, mock_read_parquet):
    # Test business aggregation logic
    mock_df = pd.DataFrame({
        "status": ["SUCCESS", "SUCCESS", "FAILED"],
        "amount": [100.0, 50.0, 20.0]
    })
    mock_read_parquet.return_value = mock_df
    
    create_gold_tables()
    
    # Check that pd.read_parquet was called
    assert mock_read_parquet.called
    
    # Check that to_parquet commands were executed (one for details, one for summary)
    assert mock_to_parquet.call_count == 2
