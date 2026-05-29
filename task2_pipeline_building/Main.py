import requests
import pandas as pd
from google.cloud import bigquery
import logging

# Logging setup
logging.basicConfig(level=logging.INFO)

# API configuration
BASE_URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 13.0827,
    "longitude": 80.2707,
    "current_weather": "true"
}

try:
    logging.info("Fetching weather data...")

    # API request
    response = requests.get(BASE_URL, params=params)

    # Check API response
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Extract current weather data
    weather = data["current_weather"]

    # Create DataFrame
    df = pd.DataFrame([weather])

    # Derived field
    df["temperature_fahrenheit"] = (df["temperature"] * 9/5) + 32

    # Handle null values
    df.fillna(0, inplace=True)

    logging.info("Transformed Data:")
    print(df)

    # BigQuery upload
    client = bigquery.Client()

    table_id = "weather-data-pipeline-497706.weather_pipeline.current_weather_data"

    job = client.load_table_from_dataframe(df, table_id)

    job.result()

    logging.info("Data uploaded to BigQuery successfully")

except Exception as e:
    logging.error(f"Error occurred: {e}")
