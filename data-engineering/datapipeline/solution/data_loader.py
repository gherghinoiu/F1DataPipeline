import pandas as pd

def load_data(path: str, type: str) -> pd.DataFrame:
    """
    Loads and validates a CSV file for races or results.

    Parameters:
    ----------
    path : str - File path to the CSV.
    type : str - Either 'races' or 'results', to determine required columns.

    Returns:
    -------
    pd.DataFrame - DataFrame containing the loaded data with all required columns.

    Raises:
    ------
    Exception
        If the file cannot be read or a required column is missing.
    """
    if type == 'races':
        required_columns = ['raceId', 'year', 'round', 'name', 'date', 'time']
    elif type == 'results':
        required_columns = ['resultId', 'raceId', 'driverId', 'position', 'fastestLapTime']
    else:
        raise ValueError("Type must be 'races' or 'results'")

    #Check if file can be read
    try:
        df = pd.read_csv(path)
    except Exception as e:
        raise Exception(f"Could not read races file: {e}")

    #Check that all required columns are present
    for col in required_columns:
        if col not in df.columns:
            raise Exception(f"Missing column '{col}' in races.csv. Please make sure the file has all required columns.")

    return df

