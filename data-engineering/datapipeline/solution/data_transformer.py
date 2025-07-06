import json
import pandas as pd
import re

def transform_result(results_races: pd.DataFrame, year: int) -> list:
    """
    Transforms a combined df from races.csv and results.csv for a specific year into a structured list of dictionaries.

    This function filters race data for the given year and processes it into a clean, JSON-ready format.

    Parameters:
    ----------
    results_races : pd.DataFrame - DataFrame containing data from races.csv and results.csv
    year : int - Year to filter the df

    Returns:
    -------
    list[dict] - Clean JSON-ready data for the specified year.
       
    """
    # Filter the DataFrame for the specific year.
    df = results_races[results_races['year'] == year].copy()

    # Fill missing fastest lap times
    df['fastestLapTime'] = df['fastestLapTime'].fillna('No time available')

    # Clean the 'time' to use '00:00:00' for invalid formats.
    df = clean_race_times(df)

    # Create the 'Race Datetime' string by combining two columns and format it to timestamp.
    df['Race Datetime'] = pd.to_datetime(df['date'] + ' ' + df['time']).dt.strftime('%Y-%m-%dT%H:%M:%S.000')

    # Rename columns to match the final JSON structure.
    # 'Race Datetime' already created, so we don't need to rename 'date' and 'time'.
    df = df.rename(columns={
        'name': 'Race Name',
        'round': 'Race Round',
        'driverId': 'Race Winning driverId',
        'fastestLapTime': 'Race Fastest Lap'
    })

    # Select and order the final columns
    final_columns = [
        "Race Name",
        "Race Round",
        "Race Datetime",
        "Race Winning driverId",
        "Race Fastest Lap"
    ]
    df = df[final_columns]

    # Ensure final data types are correct.
    df['Race Round'] = df['Race Round'].astype(int)
    df['Race Winning driverId'] = df['Race Winning driverId'].astype(int)

    return df.to_dict(orient='records')

def clean_race_times(races: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans invalid time values in the 'time' column of a DataFrame.

    Replaces any non-HH:MM:SS formatted strings with '00:00:00'.

    Parameters:
    ----------
    races : pd.DataFrame - DataFrame containing a 'time' column

    Returns:
    -------
    pd.DataFrame - Modified DataFrame with cleaned 'time' values
    """
    time_pattern = re.compile(r'^\d{2}:\d{2}:\d{2}$')

    def fix_time(value):
        # Check if value is a string and matches the pattern
        if isinstance(value, str) and time_pattern.match(value.strip()):
            return value.strip()
        return '00:00:00'

    # Apply the fix_time function to every value in the 'time' column
    races['time'] = races['time'].apply(fix_time)

    return races

def write_json(data: list[dict], filename: str) -> None:
    """
    Writes a list of dictionaries to a JSON file with indentation and UTF-8 encoding.

    Parameters:
    ----------
    data : list[dict] - JSON-serializable list of dictionaries to write  
    filename : str - File name for output JSON

    Returns:
    -------
    None
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)