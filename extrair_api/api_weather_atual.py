from datetime import datetime
import pandas as pd
import requests

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": -23.55,
    "longitude": -46.63,
    "daily": ["wind_speed_10m_max", "temperature_2m_max", "temperature_2m_min", "wind_direction_10m_dominant"]
}

response = requests.get(url, params=params)
print(response.json())
