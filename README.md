# Weather ETL Project

A simple and clean Python ETL (Extract, Transform, Load) pipeline project that fetches real-time weather data using the OpenWeatherMap API, processes the JSON response, and stores the logs securely into a local SQLite database.

## Features
- Fetches live weather information based on user input (City name).
- Parses and structures relevant metrics (Temperature, Feels Like, Humidity, Description, and Timestamp).
- Automatically creates an SQLite database (`weather_data.db`) and logs the weather entries.
- Displays all saved records directly in the terminal.

## Technologies Used
- **Python 3**
- **Requests Library** (for API communication)
- **SQLite3** (for local data storage)

## How to Run
1. Clone the repository:
   ```bash
   git clone [https://github.com/HassanAsiriDE/weather-etl-project.git](https://github.com/HassanAsiriDE/weather-etl-project.git)
