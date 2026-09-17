import pandas as pd

def graus_para_direcao(grau: int) -> str:
    grau = grau % 360
    if grau >= 337.5 or grau < 22.5:
        return "Norte"
    elif grau < 67.5:
        return "Nordeste"
    elif grau < 112.5:
        return "Leste"
    elif grau < 157.5:
        return "Sudeste"
    elif grau < 202.5:
        return "Sul"
    elif grau < 247.5:
        return "Sudoeste"
    elif grau < 292.5:
        return "Oeste"
    elif grau < 337.5:
        return "Noroeste"

def transformar_dataframe_analise(dataframe_tratado: pd.DataFrame) -> pd.DataFrame:
    dataframe_tratado["Direcao_vento"] = dataframe_tratado["Direcao_vento"].apply(graus_para_direcao)
    dataframe_tratado = dataframe_tratado[["Data", "dia","mes", "ano", "Temperatura_media", "Temperatura_maxima", "Temperatura_minima", "Probabilidade_chuva_max", "Chuva_total", "Direcao_vento", "estado"]]
    return dataframe_tratado