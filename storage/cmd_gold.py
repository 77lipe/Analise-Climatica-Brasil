from pathlib import Path
import pandas as pd

from config.caminho import CAMINHO_GOLD

def salvar_gold(
        dataframe: pd.DataFrame
) -> Path:
    if dataframe.empty:
        raise ValueError(
            "Não é posssível salvar um DataFrame VAZIO na camada gold"
        )

    data_inicial = dataframe["Data"].min()
    data_final = dataframe["Data"].max()

    data_inicial_str = pd.to_datetime(data_inicial).strftime("%Y-%m-%d")
    data_final_str = pd.to_datetime(data_final).strftime("%Y-%m-%d")
    
    CAMINHO_GOLD.mkdir(
        parents=True,
        exist_ok=True
    )

    caminho_arquivo = CAMINHO_GOLD / f"ddm_clima_sp_{data_inicial_str}_{data_final_str}.csv"

    dataframe.to_csv(
        caminho_arquivo,
        index=False
    )

    return caminho_arquivo