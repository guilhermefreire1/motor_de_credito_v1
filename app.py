import streamlit as st
import pandas as pd
import os
from src.tratamento import carregar_dados, tratar_dados
from src.avaliador import aplicar_motor_credito

st.set_page_config(page_title="Motor de Crédito", layout="wide")
st.title("💳 Analisador de Crédito Simulação Técnica")

# 1. Confirma se o arquivo CSV existe
caminho_csv = os.path.join("data", "german_credit_data.csv")
st.write("Verificando caminho:", caminho_csv)

# 2. Tenta carregar o CSV
try:
    df_original = carregar_dados(caminho_csv)
    st.write("Dados carregados")
except Exception as e:
    st.error(f"❌ Erro ao carregar os dados: {e}")

# 3. Continua se carregamento deu certo
if 'df_original' in locals():
    try:
        df_tratado = tratar_dados(df_original)
        st.write("Dados tratados com sucesso")
        
        df_resultado = aplicar_motor_credito(df_tratado)
        st.write("Análise de crédito aplicada")

        st.subheader("Resultado da análise de crédito")
        st.dataframe(df_resultado[['Age', 'Credit amount', 'Saving accounts', 'Checking account', 'Duration', 'Decisao']])
    
    except Exception as e:
        st.error(f"❌ Erro ao processar dados: {e}")
