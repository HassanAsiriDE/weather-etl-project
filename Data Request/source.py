import requests
from datetime import datetime
import sqlite3

# Prompt the user for a city name
city = input("Enter city name: ")
Api_key = "d9768b797d03520dd6b02253aee61e19"

# Construct the API request URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Api_key}&units=metric"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    main_data = data['main']
    main_sys = data['sys']
    main_weather = data['weather'][0]
    
    # Construct the weather report dictionary
    report = {
        'City': data['name'],
        'Temp': main_data['temp'],
        'Feels_like': main_data['feels_like'],
        'Description': main_weather['description'],
        'Humidity': main_data['humidity'],
        'fetched_at': current_time  # Matched lowercase key to prevent KeyError
    }
    
    # Connect to the database and create a cursor
    conc = sqlite3.connect("weather_data.db")
    cursor = conc.cursor()
    
    # Create the table if it does not exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_logs(
            City TEXT,
            Temp REAL,
            Feels_Like REAL,
            Description TEXT,
            Humidity INTEGER,
            Fetched_at TEXT
        )
    ''')
    
    # Insert the weather report into the table
    cursor.execute(''' 
        INSERT INTO weather_logs VALUES(?,?,?,?,?,?)   
    ''', (
        report['City'],
        report['Temp'],
        report['Feels_like'],
        report['Description'],
        report['Humidity'],
        report['fetched_at']
    ))
    
    # Commit changes to save the entry
    conc.commit()
    print("Data saved successfully to database!\n")
    
    # --- Fetch and display all records from the database ---
    cursor.execute("SELECT * FROM weather_logs")
    all_logs = cursor.fetchall()  # Retrieve all rows
    
    print("=== Database Records ===")
    for log in all_logs:
        print(log)
    print("========================")
    
    # Close the database connection
    conc.close()
    
else:
    print("City not found or API error!")