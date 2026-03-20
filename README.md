## (versión en español más abajo)

# Real-Time Weather Data Pipeline

## Project Overview
This project demonstrates the design and implementation of a data engineering pipeline that consumes real-time weather data from an external API, processes it using Python, and stores it in a relational database.

**Important: This project is intended for portfolio purposes only. Due to API key restrictions and environment configuration, it may not run directly on another machine. The goal is to showcase the architecture, logic, and data pipeline skills through the code.**

## Objectives
* Consume real-time data from a weather API
* Build an automated data pipeline using Python
* Store structured data in a MySQL database
* Simulate a real-world data engineering workflow

## Tech Stack
* Python → Data extraction & processing
* Requests / JSON → API consumption
* MySQL → Data storage
* SQL → Data modeling & queries
* HTML / CSS / JavaScript → Simple frontend visualization

## Architecture

The project is divided into two main parts:
1. Data Pipeline (/pipeline)
* Connects to the weather API
* Extracts real-time data
* Transforms JSON into structured format
* Inserts data into MySQL

![First Screeshot](./images/img1.png)
![Second Screeshot](./images/img3.png)

2. Frontend (/frontend)
* Displays weather data
* Uses JavaScript to fetch and render information
* Simple UI for visualization

![Third Screeshot](./images/img2.png)

## Data Flow
1. API request is made to retrieve weather data
2. Data is received in JSON format
3. Python processes and cleans the data
4. Structured data is inserted into MySQL
5. Frontend consumes and displays the data

## Key Learnings
* Building end-to-end data pipelines
* Working with real-time data sources
* API integration and data transformation
* Database design and data insertion
* Connecting backend processes with a frontend

## Limitations
* API key is not included (security reasons)
* Environment variables are not configured
* Pipeline may not run without proper setup

## Future Improvements
* Automate pipeline execution (cron / scheduler)
* Deploy database to cloud (AWS / GCP)
* Add data visualization dashboards (Power BI / Tableau)
* Implement error handling and logging


## Author

Gian Sena