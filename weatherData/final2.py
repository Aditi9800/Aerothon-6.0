import random
import csv
from datetime import datetime, timedelta

# Define weather conditions with realistic ranges
weather_conditions = [
    {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n", "level": 0, "temp_range": (290, 310), "wind_speed_range": (0, 5), "humidity_range": (20, 50)},
    {"id": 721, "main": "Haze", "description": "haze", "icon": "50d", "level": 1, "temp_range": (280, 300), "wind_speed_range": (0, 5), "humidity_range": (30, 70)},
    {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d", "level": 1, "temp_range": (275, 295), "wind_speed_range": (5, 15), "humidity_range": (50, 90)},
    {"id": 501, "main": "Rain", "description": "moderate rain", "icon": "10d", "level": 2, "temp_range": (270, 290), "wind_speed_range": (10, 20), "humidity_range": (70, 100)},
    {"id": 202, "main": "Thunderstorm", "description": "thunderstorm with heavy rain", "icon": "11d", "level": 2, "temp_range": (265, 285), "wind_speed_range": (15, 30), "humidity_range": (80, 100)},
    {"id": 600, "main": "Snow", "description": "light snow", "icon": "13d", "level": 1, "temp_range": (250, 270), "wind_speed_range": (0, 10), "humidity_range": (50, 90)},
    {"id": 611, "main": "Sleet", "description": "sleet", "icon": "13d", "level": 2, "temp_range": (255, 275), "wind_speed_range": (10, 20), "humidity_range": (60, 100)},
    {"id": 701, "main": "Mist", "description": "mist", "icon": "50d", "level": 1, "temp_range": (280, 300), "wind_speed_range": (0, 5), "humidity_range": (60, 100)},
    {"id": 781, "main": "Tornado", "description": "tornado", "icon": "50d", "level": 2, "temp_range": (270, 290), "wind_speed_range": (30, 50), "humidity_range": (70, 100)}
]

# Define some example cities with their coordinates
cities = [
    {"city_name": "New York", "country": "US", "lat": 40.7128, "lon": -74.0060},
    {"city_name": "London", "country": "GB", "lat": 51.5074, "lon": -0.1278},
    {"city_name": "Tokyo", "country": "JP", "lat": 35.6895, "lon": 139.6917},
    {"city_name": "Sydney", "country": "AU", "lat": -33.8688, "lon": 151.2093},
    {"city_name": "Moscow", "country": "RU", "lat": 55.7558, "lon": 37.6176},
    {"city_name": "Mumbai", "country": "IN", "lat": 19.0760, "lon": 72.8777},
    {"city_name": "Cairo", "country": "EG", "lat": 30.0444, "lon": 31.2357},
    {"city_name": "Paris", "country": "FR", "lat": 48.8566, "lon": 2.3522},
    {"city_name": "São Paulo", "country": "BR", "lat": -23.5505, "lon": -46.6333},
    {"city_name": "Cape Town", "country": "ZA", "lat": -33.9249, "lon": 18.4241}
]

def generate_weather_data(city, level):
    weather = random.choice([wc for wc in weather_conditions if wc["level"] == level])
    temp = round(random.uniform(*weather["temp_range"]), 2)
    data = {
        "lon": city["lon"],
        "lat": city["lat"],
        "weather_id": weather["id"],
        "main": weather["main"],
        "description": weather["description"],
        "icon": weather["icon"],
        "base": "stations",
        "temp": temp,
        "feels_like": round(temp - random.uniform(0, 5), 2),  # Feel-like temp slightly lower
        "temp_min": round(temp - random.uniform(0, 3), 2),
        "temp_max": round(temp + random.uniform(0, 3), 2),
        "pressure": random.randint(980, 1030),
        "humidity": random.randint(*weather["humidity_range"]),
        "sea_level": random.randint(980, 1030),
        "grnd_level": random.randint(900, 1030),
        "visibility": random.randint(1000, 10000),
        "wind_speed": round(random.uniform(*weather["wind_speed_range"]), 2),
        "wind_deg": random.randint(0, 360),
        "wind_gust": round(random.uniform(0, 20), 2),
        "clouds_all": random.randint(0, 100),
        "dt": int((datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).timestamp()),
        "sys_type": 1,
        "sys_id": random.randint(1000, 10000),
        "country": city["country"],
        "sunrise": int((datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).timestamp()),
        "sunset": int((datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).timestamp()),
        "timezone": random.choice([7200, 19800, -25200, -43200, 0]),
        "city_id": random.randint(1000000, 9999999),
        "city_name": city["city_name"],
        "cod": 200,
        "level": weather["level"]
    }
    return data

def generate_dataset(num_entries_per_level):
    dataset = []
    for level in range(3):  # 0, 1, 2 for good, moderate, poor
        for _ in range(num_entries_per_level):
            city = random.choice(cities)
            dataset.append(generate_weather_data(city, level))
    return dataset

def save_dataset_to_csv(dataset, filename):
    fieldnames = ["lon", "lat", "weather_id", "main", "description", "icon", "base", "temp", "feels_like", 
                  "temp_min", "temp_max", "pressure", "humidity", "sea_level", "grnd_level", "visibility", 
                  "wind_speed", "wind_deg", "wind_gust", "clouds_all", "dt", "sys_type", "sys_id", "country", 
                  "sunrise", "sunset", "timezone", "city_id", "city_name", "cod", "level"]

    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for data in dataset:
            writer.writerow(data)

# Number of entries per level (10000 total, so 3333 per level to balance it)
num_entries_per_level = 10000 // 3

# Generate the dataset
dataset = generate_dataset(num_entries_per_level)

# Save the dataset to a CSV file
filename = "realistic_weather_data.csv"
save_dataset_to_csv(dataset, filename)

print(f"Generated dataset with {len(dataset)} entries and saved to {filename}")
