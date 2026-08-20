from datetime import datetime
import pandas as pd
import requests

url = "https://historical-forecast-api.open-meteo.com/v1/forecast"

params = {
    "latitude": -23.55,
    "longitude": -46.63,
    "start_date": "2026-06-01",
    "end_date": "2026-08-19",
    "daily": ["wind_speed_10m_max", "temperature_2m_max", "temperature_2m_min", "wind_direction_10m_dominant"]
}

response = requests.get(url, params=params)
dados = response.json()

data = dados["daily"]["time"]
print("Code:", response.status_code)
# print("Dados:", dados)
print("Datas:", data)

