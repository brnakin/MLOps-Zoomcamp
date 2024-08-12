import requests
import pandas as pd
from io import BytesIO
from typing import List

# Importing the necessary decorator if not already available in the environment
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader

@data_loader
def ingest_files(**kwargs) -> pd.DataFrame:
    """
    This function downloads a CSV file from the given GitHub URL and returns it as a pandas DataFrame.
    """
    # GitHub raw content URL
    url = 'https://raw.githubusercontent.com/brnakin/MLOps-Zoomcamp/main/project/data/Walmart_Sales.csv'

    # Sending a GET request to the URL
    response = requests.get(url)
    
    # Checking if the request was successful
    if response.status_code != 200:
        raise Exception(f"Failed to download data: {response.text}")

    # Reading the CSV content directly from the response and converting it to a DataFrame
    df = pd.read_csv(BytesIO(response.content))

    # Returning the DataFrame
    return df