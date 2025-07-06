import pandas as pd
import pytest
from solution.data_transformer import transform_result, clean_race_times

@pytest.fixture
def sample_merged_data():
    """
    Creates a sample merged DataFrame for testing.
    This fixture will be automatically used by tests that ask for it.
    """
    data = {
        'year': [2025, 2025],
        'name': ['British Grand Prix', 'Monaco Grand Prix'],
        'round': [12, 8],
        'date': ['2025-06-07', '2025-05-26'],
        'time': ['14:00:00', '13:00:00'],
        'driverId': [1, 16],
        'fastestLapTime': ['01:29.4', '01:14.1']
    }
    return pd.DataFrame(data)

def test_transform_result(sample_merged_data):
    """
    Tests the main transformation function for structure, types, and content.
    """
    # Run the transformation for the year 2025
    transformed_data = transform_result(sample_merged_data, 2025)
    
    # 1. Check the structure and content of the first race record
    first_race = transformed_data[0]
    assert first_race['Race Name'] == 'British Grand Prix'
    assert first_race['Race Round'] == 12
    assert first_race['Race Datetime'] == '2025-06-07T14:00:00.000'
    assert first_race['Race Winning driverId'] == 1
    assert first_race['Race Fastest Lap'] == '01:29.4'
    
    # 2. Check that the data types are correct
    assert isinstance(first_race['Race Round'], int)
    assert isinstance(first_race['Race Winning driverId'], int)

def test_clean_race_times():
    """
    Tests that times are correctly formatted or replaced.
    """
    # Create a sample DataFrame with messy time data
    messy_times_df = pd.DataFrame({
        'time': ["14:30:00", "15:00", " ", None, " 13:00:00 ", "13::00:00", "  :  :  "]
    })
    
    cleaned_df = clean_race_times(messy_times_df)
    
    # Define the expected outcome after cleaning
    expected_times = ["14:30:00", "00:00:00", "00:00:00", "00:00:00", "13:00:00", "00:00:00", "00:00:00"]
    
    # Assert that the cleaned column matches the expected outcome
    assert cleaned_df['time'].tolist() == expected_times