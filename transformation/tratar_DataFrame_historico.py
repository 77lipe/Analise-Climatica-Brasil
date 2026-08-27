import pandas as pd
from datetime import datetime

from transformation.converter_api_para_df import *

def tratar_DataFrame(dataframe_bruto: pd.DataFrame)-> pd.DataFrame:

    df_tratado = dataframe_bruto.copy()
    df_tratado["time"] = pd.to_datetime(
        df_tratado["time"],
        format="%Y-%m-%d",
        errors="raise"
    )

    df_tratado["temperature_2m_max"] = pd.to_numeric(
        df_tratado["temperature_2m_max"],
        errors="raise"
    )

    df_tratado["temperature_2m_min"] = pd.to_numeric(
            df_tratado["temperature_2m_min"],
            errors="raise"
        )

    df_tratado["temperature_2m_mean"] = pd.to_numeric(
            df_tratado["temperature_2m_mean"],
            errors="raise"
        )

    df_tratado["wind_speed_10m_max"] = pd.to_numeric(
                df_tratado["wind_speed_10m_max"],
                errors="raise"
            )

    df_tratado["wind_direction_10m_dominant"] = pd.to_numeric(
                df_tratado["wind_direction_10m_dominant"],
                errors="raise"
            )

    df_tratado["ano"] = (
        df_tratado["time"].dt.year
    )
    df_tratado["mes"] = (
        df_tratado["time"].dt.month
    )
    df_tratado["dia"] = (
        df_tratado["time"].dt.day
    )

    df_tratado["estado"] = "SP"

    df_tratado = df_tratado.sort_values(
        by="time"
    ).reset_index(drop=True)

    df_tratado = df_tratado.rename(columns={"time": "Data",
                                           "temperature_2m_mean": "Temperatura_media",
                                             "temperature_2m_max": "Temperatura_maxima",
                                               "temperature_2m_min": "Temperatura_minima",
                                                "wind_direction_10m_dominant": "Direcao_vento",
                                                "wind_speed_10m_max": "Velocidade_vento_max"
                                                })

    return df_tratado


if __name__ == "__main__":
    df_bruto = converter_para_df(data_inicial="2025-07-01", data_final="2025-08-26")
    print(tratar_DataFrame(df_bruto))