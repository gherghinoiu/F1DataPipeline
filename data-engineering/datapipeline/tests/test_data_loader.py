import pandas as pd
import pytest
from solution.data_loader import load_data

@pytest.fixture
def create_test_csv(tmp_path):
    """A helper function to create temporary CSV files for testing."""
    def _create_csv(filename, data):
        file_path = tmp_path / filename
        df = pd.DataFrame(data)
        df.to_csv(file_path, index=False)
        return file_path
    return _create_csv

# Test 1: Check if a valid 'races.csv' file loads correctly.
def test_load_data_races_success(create_test_csv):
    """
    Tests that a valid races CSV file is loaded successfully into a DataFrame.
    """
    # Arrange: Create a valid races CSV file.
    races_data = {
        'raceId': [1], 
        'year': [2024], 
        'round': [1],
        'name': ['Test GP'], 
        'date': ['2024-01-01'], 
        'time': ['12:00:00']
    }
    file_path = create_test_csv("races.csv", races_data)

    # Act: Load the data.
    df = load_data(file_path, 'races')

    # Assert: Check that the result is a pandas DataFrame with the correct number of rows.
    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1



