# 💳 Motor de Crédito com Python e Streamlit

Este projeto simula um **motor de decisão de crédito**, como os utilizados em instituições financeiras para aprovar ou negar propostas. Ele foi desenvolvido com foco técnico em **Python, tratamento de dados com Pandas e lógica de decisão automatizada**, e conta com uma interface interativa via **Streamlit**.

---

## 🚀 Funcionalidades

- 🔎 Análise automática de propostas com base em regras de crédito
- 📊 Interface visual com filtros por idade e decisão
- 📁 Download dos resultados diretamente pelo app
- ⚙️ Estrutura modular com separação de regras, tratamento e execução

---

## 🧠 Tecnologias utilizadas

- Python 3.12
- Streamlit
- Pandas


## ▶️ Como rodar localmente

1. Clone o repositório:

git clone https://github.com/guilhermefreire1/motor_de_credito_v1.git
cd motor_de_credito_v1

Instale as dependências:

pip install -r requirements.txt

Execute a aplicação:

streamlit run app.py

A aplicação será aberta no navegador em http://localhost:8501.

🧪 Lógica de decisão aplicada

As regras são baseadas em condições comuns a motores de risco de crédito, como:

❌ Valor solicitado alto + ausência de poupança → Negado

❌ Idade baixa + prazo longo → Negado

❌ Conta corrente com saldo baixo + duração alta → Negado

✅ Todos os demais casos → Aprovado

Essas regras são aplicadas sobre um dataset real de crédito (German Credit Data) e podem ser facilmente adaptadas para outros critérios.

🌐 Deploy Online
Acesse a versão web interativa:

🔗 [https://seuusuario.streamlit.app](https://motordecreditov1.streamlit.app/)


📄 Licença
Este projeto está disponível para fins de estudo e demonstração. Sinta-se livre para clonar, adaptar ou contribuir.
