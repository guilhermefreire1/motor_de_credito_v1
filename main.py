# main.py

from src.tratamento import carregar_dados, tratar_dados
from src.avaliador import aplicar_motor_credito
import os

def main():
    # Caminho para o arquivo CSV original
    caminho_arquivo = os.path.join("data", "german_credit_data.csv")

    # Carrega o dataset
    df = carregar_dados(caminho_arquivo)

    # Aplica tratamento de dados
    df_tratado = tratar_dados(df)

    # Aplica as regras de crédito
    df_com_decisao = aplicar_motor_credito(df_tratado)

    # Caminho para salvar o resultado
    caminho_saida = os.path.join("outputs", "resultado_credito.csv")
    os.makedirs("outputs", exist_ok=True)  # Cria a pasta se não existir

    # Salva o resultado final em CSV
    df_com_decisao.to_csv(caminho_saida, index=False)

    # Mostra uma prévia dos resultados no console
    print("\nPrévia das decisões geradas:\n")
    print(df_com_decisao[['Age', 'Credit amount', 'Saving accounts', 'Checking account', 'Duration', 'Decisao']].head(10))

    print(f"\n✅ Arquivo salvo com sucesso em: {caminho_saida}")

# Executa o fluxo principal
if __name__ == "__main__":
    main()
