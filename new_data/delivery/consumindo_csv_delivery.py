import pandas as pd
import numpy as np
from pathlib import Path

def consumir_dados_delivery(caminho: str) -> pd.DataFrame:
    
    pasta = Path(caminho)
    if not pasta.exists():
        raise FileNotFoundError(
            f"Caminho não encontrado: {pasta}"
        )
    arq_meses = sorted(
        f for f in pasta.iterdir()
    )
    if not arq_meses:
        raise FileNotFoundError(
            f"Nenhum arquivo foi encontrado na pasta: {pasta}"
        )
    print(f"{len(arq_meses)} arquivos encontrados")
    
    df_meses_delivery = pd.DataFrame()
    df_meses_delivery = df_meses_delivery[["Time", "Food delivery"]]
    for arquivo_mes in arq_meses:
        df_mes = pd.read_csv(f"{caminho}/{arquivo_mes}")
        df_meses_delivery = pd.concat([df_mes, df_meses_delivery])
    
    df_meses_delivery["Time"] = pd.to_datetime(df_meses_delivery["Time"])
    df_meses_delivery = (
        df_meses_delivery.drop_duplicates(subset="Time", keep="last")
        .sort_values("Time")
        .reset_index(drop=True)
    )
    
    return df_meses_delivery        
    
if __name__ == "__main__":
    df = consumir_dados_delivery("newdata\delivery\base_meses_2026")
    print(df.heado)