import requests
import pandas as pd
from google.cloud import bigquery

# API URL
url = "https://api.open-meteo.com/v1/forecast?latitude=13.0827&longitude=80.2707&current_weather=true"

try:
    print("Fetching weather data...")

    # API request
    response = requests.get(url)

    # Check API response
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Extract current weather
    weather = data["current_weather"]

    # Create dataframe
    df = pd.DataFrame([weather])

    # Derived field
    df["temperature_fahrenheit"] = (df["temperature"] * 9/5) + 32

    # Handle null values
    df.fillna(0, inplace=True)

    print("Transformed Data:")
    print(df)

    # BigQuery upload
    client = bigquery.Client()

    table_id = "weather-data-pipeline-497706.weather_pipeline.current_weather_data"

    job = client.load_table_from_dataframe(df, table_id)

    job.result()

    print("Data uploaded to BigQuery successfully")

except Exception as e:
    print("Error occurred:", e)
