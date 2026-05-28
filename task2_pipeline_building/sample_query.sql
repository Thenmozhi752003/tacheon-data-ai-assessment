SELECT
    AVG(temperature) AS average_temperature,
    MAX(windspeed) AS highest_wind_speed,
    COUNT(*) AS total_records
FROM `weather-data-pipeline-497706.weather_pipeline.current_weather_data`;
