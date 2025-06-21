import pandas as pd

# Carregando os dados aqui 
def carregar_dados (german_credit_data_csv : str) -> pd.DataFrame:

    " Lê o CSV aqui"

    # Lendo os dados aqui
    df = pd.read_csv(german_credit_data_csv)
    return df

def tratar_dados(df: pd.DataFrame) -> pd.DataFrame:

    "Trata os dados aqui"

    #Remover primeira coluna
    if 'Unnamed: 0' in df.columns:

        df = df.drop(columns=['Unnamed: 0'])

        #Preencher colunas com valores faltantes
        df['Saving accounts'] = df ['Saving accounts'].fillna('unknown')
        df['Checking account'] = df ['Checking account'].fillna('unknown')

        return df