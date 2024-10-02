import csv
import random
import numpy as np

# Number of rows for each level (0, 1, 2)
num_rows_per_level = 10000 // 3

# Helper functions to generate realistic random data
def random_temperature():
    return round(random.uniform(280, 290), 2)

def random_feels_like(temp):
    return round(temp - random.uniform(0, 2), 2)

def random_temp_min(temp):
    return round(temp - random.uniform(1, 3), 2)

def random_temp_max(temp):
    return round(temp + random.uniform(1, 3), 2)

def random_pressure():
    return random.randint(990, 1030)

def random_humidity():
    return random.randint(50, 100)

def random_wind_speed():
    return round(random.uniform(0, 10), 2)

def random_wind_deg():
    return random.randint(0, 360)

def random_wind_gust(speed):
    return round(speed + random.uniform(0, 5), 2)

def random_clouds():
    return random.randint(0, 100)

def random_visibility():
    return random.randint(1000, 10000)

def random_sea_level():
    return random.randint(990, 1030)

def random_grnd_level():
    return random.randint(900, 1000)

# Generating dataset
def generate_weather_data(num_rows):
    data = []
    for level in range(3):
        for _ in range(num_rows_per_level):
            temp = random_temperature()
            wind_speed = random_wind_speed()
            row = {
                "coord_lon": 10.99,
                "coord_lat": 44.34,
                "weather_id": 800,
                "weather_main": "Clear",
                "weather_description": "clear sky",
                "weather_icon": "01n",
                "base": "stations",
                "main_temp": temp,
                "main_feels_like": random_feels_like(temp),
                "main_temp_min": random_temp_min(temp),
                "main_temp_max": random_temp_max(temp),
                "main_pressure": random_pressure(),
                "main_humidity": random_humidity(),
                "main_sea_level": random_sea_level(),
                "main_grnd_level": random_grnd_level(),
                "visibility": random_visibility(),
                "wind_speed": wind_speed,
                "wind_deg": random_wind_deg(),
                "wind_gust": random_wind_gust(wind_speed),
                "clouds_all": random_clouds(),
                "dt": random.randint(1600000000, 1700000000),
                "sys_type": 1,
                "sys_id": 6812,
                "sys_country": "IT",
                "sys_sunrise": random.randint(1600000000, 1700000000),
                "sys_sunset": random.randint(1600000000, 1700000000),
                "timezone": 7200,
                "id": 3163858,
                "name": "Zocca",
                "cod": 200,
                "level": level
            }
            data.append(row)
    return data

# Writing to CSV
def write_to_csv(data, filename='weather_data.csv'):
    keys = data[0].keys()
    with open(filename, 'w', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Generate and save data
weather_data = generate_weather_data(10000)
write_to_csv(weather_data)

print("CSV file 'weather_data.csv' generated successfully.")
