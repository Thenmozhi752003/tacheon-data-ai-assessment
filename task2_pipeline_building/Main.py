
import requests
import pandas as pd

# API URL
url = "https://api.open-meteo.com/v1/forecast?latitude=13.0827&longitude=80.2707&current_weather=true"

try:
    print("Fetching weather data...")

    # Get API response
    response = requests.get(url)

    # Convert JSON response
    data = response.json()

    # Extract current weather data
    weather = data["current_weather"]

    # Create dataframe
    df = pd.DataFrame([weather])

    # Create derived column
    df["temperature_fahrenheit"] = (df["temperature"] * 9/5) + 32

    # Handle null values
    df.fillna(0, inplace=True)

    print("Transformed Data:")
    print(df)

except Exception as e:
    print("Error occurred:", e)
