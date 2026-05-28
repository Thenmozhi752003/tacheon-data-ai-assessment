# Task 2 - Pipeline Building

This section contains the API data pipeline project using Python, BigQuery, and SQL.
# Task 2 - Pipeline Building

## Project Overview

This project builds a small data pipeline using the Open-Meteo public API. The pipeline fetches current weather data, transforms it using Python and Pandas, and uploads the processed data into Google BigQuery for analysis.

## API Chosen

I chose the Open-Meteo Weather API because it is free, does not require an API key, and returns structured weather data that can be easily processed.

## Pipeline Flow

Open-Meteo API → Python Script → Data Transformation → BigQuery Table → SQL Analysis

## Data Collected

The pipeline collects current weather data such as:

- Time
- Temperature
- Wind speed
- Wind direction
- Weather code
- Day/night indicator

## Data Transformation

The raw API response is converted into a tabular format using Pandas.

A derived field is added:

- `temperature_fahrenheit`

This converts Celsius temperature into Fahrenheit.

Null values are handled using fillna.

## BigQuery Storage

The transformed data is uploaded to Google BigQuery.

Dataset:

`weather_pipeline`

Table:

`current_weather_data`

## SQL Analysis

A sample SQL query is included in `sample_query.sql`.

The query calculates:

- Average temperature
- Highest wind speed
- Total number of records

## How to Run

Install required packages:

```bash
pip install -r requirements.txt
