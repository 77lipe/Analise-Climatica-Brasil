import pandas as pd

def verificar_dados(dataframe_bruto: pd.DataFrame) -> pd.DataFrame:

    # Validação dos Tipos de dados e Dimensões - Antes de remover valores desnecessários
    print("Tipos de dados | Dimensões do df-Bruto:\n")
    print(dataframe_bruto.info())
    dataframe_tratado = dataframe_bruto.copy()

    nulos = dataframe_bruto.isnull().sum().values
    # Verificação de valores nulos
    if any(n > 0 for n in nulos):
        print(f"Dados Ausentes foram identificados!\nQuantidade: {dataframe_bruto.isnull().sum()}\n")
        apagar = str(input(f"{dataframe_bruto.isnull()}\nDeseja apagar valores nulos? (Y/N):"))
        if apagar.upper == "Y":
            dataframe_tratado = dataframe_tratado.dropna()

    print("teste:", dataframe_bruto.duplicated().sum())
    # Verificação de valores duplicados
    if dataframe_bruto.duplicated().sum() > 0:
        print(f"Dados duplicados foram identificados!\nQuantidade: {dataframe_bruto.duplicated().sum()}\n")
        apagar = str(input(f"{dataframe_bruto.duplicated()}\nDeseja apagar valores nulos? (Y/N):"))
        if apagar.upper == "Y":
            dataframe_tratado = dataframe_tratado.drop_duplicates()

    print("Tipos de dados | Dimensões do dataframe após remoção de valores:\n",dataframe_bruto.info())
    return dataframe_tratado
    
