from datetime import datetime
import pandas as pd
import requests



params = {
    "latitude": -23.55,
    "longitude": -46.63,
    "daily": ["wind_speed_10m_max", "temperature_2m_max", "temperature_2m_min", "wind_direction_10m_dominant"]
}

response = requests.get(url, params=params)
data_atual_clima = response.json()