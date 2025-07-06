import os
import pandas as pd
from pathlib import Path
from data_loader import load_data
from data_transformer import transform_result, write_json

# Get the directory where main.py is located
SCRIPT_DIR = Path(__file__).parent 

# Build paths relative to the project root
PROJECT_ROOT = SCRIPT_DIR.parent
SOURCE_DATA_DIR = PROJECT_ROOT / 'source-data'
RESULTS_DIR = PROJECT_ROOT / 'results'

RACES_FILE = SOURCE_DATA_DIR / 'races.csv'
RESULTS_FILE = SOURCE_DATA_DIR / 'results.csv'

def main():
    # Load the data from sorce-data directory 
    races_df = load_data(RACES_FILE, 'races')
    results_df = load_data(RESULTS_FILE, 'results')

    # Filter results to get only the winning drivers
    winners_df = results_df[results_df['position'] == 1.0]
    
    # Create results folder if it does not exist
    os.makedirs(RESULTS_DIR, exist_ok=True)

    # Join the 2 data frames
    results_races_df = pd.merge(races_df, winners_df, on='raceId', how='inner')

    # Get all unique years in a separate variable
    available_years_df = results_races_df['year'].unique()

    # Iterate through each year and transform the results
    for year in available_years_df:
        # Define the complete file path for the output JSON file.
        output_path = RESULTS_DIR / f'stats_{year}.json'

        # Call the main transformation function to process the data for the selected year.
        transformed_result_df = transform_result(results_races_df, year)

        # Write the transformed data to a JSON file.
        write_json(transformed_result_df, output_path)


main()