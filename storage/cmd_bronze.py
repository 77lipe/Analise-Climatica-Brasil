from pathlib import Path
from datetime import datetime
import pandas as pd

from config.caminho import CAMINHO_BRONZE

def salvar_df_bronze(data_frame_bruto: pd.DataFrame) -> Path:

    CAMINHO_BRONZE.mkdir(
        parents=True,
        exist_ok=True
    )

    data_execucao = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nome_arquivo =  f"clima_sp_{data_execucao}.csv"


    caminho_arquivo = CAMINHO_BRONZE / nome_arquivo

    data_frame_bruto.to_csv(
        caminho_arquivo,
        index=False
    )

    return caminho_arquivo