import pandas as pd
from src.regras import avaliar_cliente

def aplicar_motor_credito(df: pd.DataFrame) -> pd.DataFrame:
    df['Decisao'] = df.apply(avaliar_cliente, axis=1)
    return df
