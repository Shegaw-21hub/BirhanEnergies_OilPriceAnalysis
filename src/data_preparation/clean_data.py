import pandas as pd
import numpy as np
import os

def load_and_clean_data(raw_data_path):
    """
    Loads raw Brent oil price data, cleans it, and calculates log returns.
    This function prepares the data for change point analysis.

    Args:
        raw_data_path (str): The file path to the raw data CSV.

    Returns:
        pd.DataFrame: A cleaned DataFrame with 'Date', 'Price', and 'Log_Return' columns.
        None: If the file is not found.
    """
    try:
        data = pd.read_csv(raw_data_path)

        # Use format='mixed' to infer the format for each date string
        data['Date'] = pd.to_datetime(data['Date'], format='mixed', dayfirst=False)
        data = data.sort_values(by='Date')
        data = data.set_index('Date')

        # Handle missing values by interpolation
        data['Price'] = data['Price'].interpolate(method='time')

        # Drop any remaining NaN values
        data = data.dropna(subset=['Price'])

        # Calculate log returns for stationarity
        data['Log_Return'] = np.log(data['Price']).diff()

        # Drop the first row which will have a NaN log return
        data = data.dropna(subset=['Log_Return'])

        # Reset the index to make 'Date' a column again, as per our original structure
        data = data.reset_index()

        return data

    except FileNotFoundError:
        print(f"Error: The file at '{raw_data_path}' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred during data loading or preprocessing: {e}")
        return None

if __name__ == "__main__":
    # Define the absolute path to your raw data file.
    # ACTION: You must still replace this path with the correct one for your machine.
    raw_data_path = r"D:\Project\BirhanEnergies_OilPriceAnalysis\data\raw\BrentOilPrices.csv"
    
    # Get the absolute path to the project's root directory
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    
    # Construct the full path to the output directory and file
    processed_data_dir = os.path.join(project_root, 'data', 'processed')
    processed_data_path = os.path.join(processed_data_dir, 'brent_oil_clean.csv')

    # Ensure the output directory exists before saving
    if not os.path.exists(processed_data_dir):
        os.makedirs(processed_data_dir)
        print(f"Created directory: {processed_data_dir}")

    cleaned_df = load_and_clean_data(raw_data_path)

    if cleaned_df is not None:
        cleaned_df.to_csv(processed_data_path, index=False)
        print("Data loaded, cleaned, and saved successfully to brent_oil_clean.csv")
        print("Sample of cleaned data:")
        print(cleaned_df.head())