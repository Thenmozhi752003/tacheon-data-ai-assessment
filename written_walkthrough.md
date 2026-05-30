# Assessment Walkthrough

## Introduction

This repository contains my submission for the Tacheon Data & AI Product Engineer assessment. The assessment consists of two tasks: Product Scoping and Pipeline Building.

My goal was to create practical solutions that are simple, easy to understand, and aligned with the requirements provided.

# Task 1: Product Scoping

## Understanding the Problem

The scenario described a marketing technology team that manually collects marketing performance data from multiple platforms and prepares reports manually.

This process creates several challenges:

* Reporting takes a significant amount of time.
* Insights may vary depending on who prepares the report.
* Teams become dependent on specific employees.
* Decision-making becomes slower.

The core problem was not a lack of data but the lack of a centralized and consistent way to access and analyze that data.

## My Approach

I decided to propose a centralized marketing analytics dashboard called **Marketing Performance Insights Hub**.

Instead of changing the tools currently used by the team, the solution integrates with existing platforms and brings the data together in one place.

The dashboard focuses on:

* Campaign performance tracking
* Channel comparison
* ROI analysis
* Trend analysis
* KPI monitoring

## Users

I identified two user groups:

### Primary Users

Internal marketing analysts who need to monitor campaign performance and generate insights quickly.

### Secondary Users

Clients and account managers who want a quick overview of marketing performance and high-performing channels.

## Data Collection Strategy

To fit the existing workflow, I proposed two methods:

1. API integrations for platforms such as Google Ads and Meta Ads.
2. CSV uploads for platforms where API access is unavailable.

This approach minimizes workflow changes while improving reporting consistency.

## Scope Decisions

For Version 1, I focused on the most valuable features:

* Campaign dashboard
* ROI tracking
* Trend analysis
* Filters
* Automated daily refresh

I intentionally excluded (maybe in future):

* AI predictions
* Real-time streaming analytics
* Mobile applications
* Advanced attribution models

These features can be considered in future versions after validating the core product.

------------

# Task 2: Pipeline Building

## Choosing the API

For the pipeline project, I selected the Open-Meteo Weather API.

I chose it because:

* It is free to use.
* No API key is required.
* The data is structured and easy to process.
* It provides a realistic example of API-based data ingestion.

## Pipeline Design

The pipeline follows a simple workflow:

Open-Meteo API → Python Script → Data Transformation → BigQuery → SQL Analysis

## Data Extraction

Using Python and the Requests library, I fetched current weather data from the API.

The script includes:

* API requests
* Error handling
* Parameterized configuration
* Logging messages

This makes the pipeline easier to maintain and troubleshoot.

## Data Transformation

After retrieving the API response, I transformed the data using Pandas.

The transformation process included:

* Converting JSON data into a tabular DataFrame
* Handling null values
* Creating a derived field called `temperature_fahrenheit`

The derived field converts temperature from Celsius to Fahrenheit and demonstrates how analytical value can be added during processing.

## BigQuery Integration

The transformed data is loaded into Google BigQuery.

Dataset:

* weather_pipeline

Table:

* current_weather_data

I used the BigQuery Sandbox environment because it is free and satisfies the requirements of the assessment.

## SQL Analysis

To demonstrate that the data is queryable and useful, I created a SQL query that calculates:

* Average temperature
* Highest wind speed
* Total record count

This provides a simple example of how the stored data can be analyzed.

---

# Production Considerations

If this pipeline were moved into production, I would:

### Scheduling

Use Cron Jobs, Apache Airflow, or Google Cloud Scheduler to automate execution.

### Monitoring

Use logging and alerting mechanisms to detect failures quickly.

### Scaling

If data volume increased significantly, I would:

* Implement batch processing
* Use partitioned BigQuery tables
* Add retry mechanisms
* Optimize data ingestion and storage

---

# Reflect# Assessment Walkthrough

## Introduction

This repository contains my submission for the Tacheon Data & AI Product Engineer assessment. The assessment consists of two tasks: Product Scoping and Pipeline Building.

My goal was to create practical solutions that are simple, easy to understand, and aligned with the requirements provided.

---

# Task 1: Product Scoping

## Understanding the Problem

The scenario described a marketing technology team that manually collects marketing performance data from multiple platforms and prepares reports manually.

This process creates several challenges:

* Reporting takes a significant amount of time.
* Insights may vary depending on who prepares the report.
* Teams become dependent on specific employees.
* Decision-making becomes slower.

The core problem was not a lack of data but the lack of a centralized and consistent way to access and analyze that data.

## My Approach

I decided to propose a centralized marketing analytics dashboard called **Marketing Performance Insights Hub**.

Instead of changing the tools currently used by the team, the solution integrates with existing platforms and brings the data together in one place.

The dashboard focuses on:

* Campaign performance tracking
* Channel comparison
* ROI analysis
* Trend analysis
* KPI monitoring

## Users

I identified two user groups:

### Primary Users

Internal marketing analysts who need to monitor campaign performance and generate insights quickly.

### Secondary Users

Clients and account managers who want a quick overview of marketing performance and high-performing channels.

## Data Collection Strategy

To fit the existing workflow, I proposed two methods:

1. API integrations for platforms such as Google Ads and Meta Ads.
2. CSV uploads for platforms where API access is unavailable.

This approach minimizes workflow changes while improving reporting consistency.

## Scope Decisions

For Version 1, I focused on the most valuable features:

* Campaign dashboard
* ROI tracking
* Trend analysis
* Filters
* Automated daily refresh

I intentionally excluded:

* AI predictions
* Real-time streaming analytics
* Mobile applications
* Advanced attribution models

These features can be considered in future versions after validating the core product.

---

# Task 2: Pipeline Building

## Choosing the API

For the pipeline project, I selected the Open-Meteo Weather API.

I chose it because:

* It is free to use.
* No API key is required.
* The data is structured and easy to process.
* It provides a realistic example of API-based data ingestion.

## Pipeline Design

The pipeline follows a simple workflow:

Open-Meteo API → Python Script → Data Transformation → BigQuery → SQL Analysis

## Data Extraction

Using Python and the Requests library, I fetched current weather data from the API.

The script includes:

* API requests
* Error handling
* Parameterized configuration
* Logging messages

This makes the pipeline easier to maintain and troubleshoot.

## Data Transformation

After retrieving the API response, I transformed the data using Pandas.

The transformation process included:

* Converting JSON data into a tabular DataFrame
* Handling null values
* Creating a derived field called `temperature_fahrenheit`

The derived field converts temperature from Celsius to Fahrenheit and demonstrates how analytical value can be added during processing.

## BigQuery Integration

The transformed data is loaded into Google BigQuery.

Dataset:

* weather_pipeline

Table:

* current_weather_data

I used the BigQuery Sandbox environment because it is free and satisfies the requirements of the assessment.

## SQL Analysis

To demonstrate that the data is queryable and useful, I created a SQL query that calculates:

* Average temperature
* Highest wind speed
* Total record count

This provides a simple example of how the stored data can be analyzed.

---

# Production Considerations

If this pipeline were moved into production, I would:

### Scheduling

Use Cron Jobs, Apache Airflow, or Google Cloud Scheduler to automate execution.

### Monitoring

Use logging and alerting mechanisms to detect failures quickly.

### Scaling

If data volume increased significantly, I would:

* Implement batch processing
* Use partitioned BigQuery tables
* Add retry mechanisms
* Optimize data ingestion and storage

---

# Reflection
Overall, my focus throughout the assessment was to build solutions that are practical, easy to understand, and aligned with real-world business needs.
