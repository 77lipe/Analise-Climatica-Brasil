from datetime import datetime
from pathlib import Path

import pandas as pd

from config.caminho import CAMINHO_SILVER

def salvar_silver(dataframe_tratado: pd.DataFrame) -> Path:

    if dataframe_tratado.empty:
        raise ValueError(
            "DataFrame recebido está vazio! Não foi possível carregar os dados na SILVER."
        )

    data_inicial = dataframe_tratado["Data"].min()
    data_final = dataframe_tratado["Data"].max()

    print(data_inicial)
    print(data_final)

    CAMINHO_SILVER.mkdir(
        parents=True,
        exist_ok=True
    )

    nome_arquivo = (
        f"clima_sp_{data_inicial}_{data_final}_tgt.csv"
    )
    caminho_arquivo = CAMINHO_SILVER / nome_arquivo

    dataframe_tratado.to_csv(
        caminho_arquivo,
        index=False,
        engine="pyarrow"
    )

    return caminho_arquivo



