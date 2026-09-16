import requests

from config.base_config_api import *

def extrair_api_historico(data_inicial: str, data_final: str, url=BASE_URL_HISTORICA, latitude=latitude_sp, longitude=longitude_sp):
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": data_inicial,
        "end_date": data_final,
        "daily": ["temperature_2m_max", "temperature_2m_min", "temperature_2m_mean", "precipitation_probability_max", "rain_sum", "wind_speed_10m_max", "wind_direction_10m_dominant"]
    }

    response = requests.get(url, params=params)
    return response.json()


if __name__ == "__main__":
    print(extrair_api_historico(data_inicial="2026-01-01", data_final="2026-01-10"))
    