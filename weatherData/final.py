import random
import csv
from datetime import datetime, timedelta

def generate_weather_data(lat, lon, level):
    # Define weather conditions with associated levels
    weather_conditions = [
        {"id": 800, "main": "Clear", "description": "clear sky", "icon": "01n", "level": 0},
        {"id": 721, "main": "Haze", "description": "haze", "icon": "50d", "level": 1},
        {"id": 804, "main": "Clouds", "description": "overcast clouds", "icon": "04d", "level": 1},
        {"id": 501, "main": "Rain", "description": "moderate rain", "icon": "10d", "level": 2},
        {"id": 202, "main": "Thunderstorm", "description": "thunderstorm with heavy rain", "icon": "11d", "level": 2}
    ]

    # Filter weather conditions based on the specified level
    filtered_conditions = [wc for wc in weather_conditions if wc["level"] == level]
    weather = random.choice(filtered_conditions)
    
    data = {
        "lon": lon,
        "lat": lat,
        "weather_id": weather["id"],
        "main": weather["main"],
        "description": weather["description"],
        "icon": weather["icon"],
        "base": "stations",
        "temp": round(random.uniform(220.0, 320.0), 2),
        "feels_like": round(random.uniform(220.0, 320.0), 2),
        "temp_min": round(random.uniform(220.0, 320.0), 2),
        "temp_max": round(random.uniform(220.0, 320.0), 2),
        "pressure": random.randint(980, 1030),
        "humidity": random.randint(10, 100),
        "sea_level": random.randint(980, 1030),
        "grnd_level": random.randint(900, 1030),
        "visibility": random.randint(1000, 10000),
        "wind_speed": round(random.uniform(0.0, 15.0), 2),
        "wind_deg": random.randint(0, 360),
        "wind_gust": round(random.uniform(0.0, 20.0), 2),
        "clouds_all": random.randint(0, 100),
        "dt": int((datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).timestamp()),
        "sys_type": 1,
        "sys_id": random.randint(1000, 10000),
        "country": random.choice(["IT", "IN", "US", "GB"]),
        "sunrise": int((datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).timestamp()),
        "sunset": int((datetime.utcnow() - timedelta(seconds=random.randint(0, 86400))).timestamp()),
        "timezone": random.choice([7200, 19800, -25200, -43200, 0]),
        "city_id": random.randint(1000000, 9999999),
        "city_name": random.choice(["Zocca", "Pitampura", "Pune", "Rumbak", "Cornville", "Whitby", "Nantucket"]),
        "cod": 200,
        "level": weather["level"]
    }
    return data

def generate_dataset(num_entries_per_level):
    dataset = []
    for level in range(3):  # 0, 1, 2 for good, moderate, poor
        for _ in range(num_entries_per_level):
            lat = round(random.uniform(-90.0, 90.0), 6)
            lon = round(random.uniform(-180.0, 180.0), 6)
            dataset.append(generate_weather_data(lat, lon, level))
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
filename = "random_weather_data.csv"
save_dataset_to_csv(dataset, filename)

print(f"Generated dataset with {len(dataset)} entries and saved to {filename}")
