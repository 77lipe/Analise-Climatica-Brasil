import pandas as pd

from extrair_api.api_weather_historica import *
from storage.cmd_bronze import salvar_df_bronze

def converter_para_df(data_inicial: str, data_final: str) -> pd.DataFrame:

        dados = extrair_api_historico(data_inicial=data_inicial,data_final=data_final)
        df_bruto = pd.DataFrame(dados["daily"])

        salvar_df_bronze(df_bruto)

        return df_bruto
