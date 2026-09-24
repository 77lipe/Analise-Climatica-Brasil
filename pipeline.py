import pandas as pd

from transformation.converter_api_para_df import converter_para_df
from transformation.tratar_DataFrame_historico import tratar_DataFrame
from transformation.direcionamento_dataframe_analise import transformar_dataframe_analise
from storage.cmd_gold import salvar_gold
from storage.cmd_silver import salvar_silver

def executar_pipeline(data_inicial: str, data_final: str) -> pd.DataFrame:

    df_bruto_b = converter_para_df(data_inicial=data_inicial, data_final=data_final)
    print("DataFrame Bronze:\n", df_bruto_b.head())
    df_tratado_s = tratar_DataFrame(df_bruto_b)
    salvar_silver(df_tratado_s)
    df_analise_g = transformar_dataframe_analise(df_tratado_s)
    salvar_gold(df_analise_g)

    return df_analise_g

if __name__ == "__main__":
    df_analise = executar_pipeline(data_inicial="1982-01-01", data_final="1982-09-20")