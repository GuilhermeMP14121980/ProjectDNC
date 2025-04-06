# Importação de bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# Configuração inicial do Streamlit
st.title("Dashboard de Análise de Dados do Chatbot")
st.write("Este dashboard apresenta a análise baseada nos dados do chatbot.")

# 1. Carregar os dados
# Carregamento de dados brutos
dados = pd.read_csv("arquivo.csv")
st.write("Dados Brutos:")
st.dataframe(dados.head())  # Exibe os dados diretamente no dashboard para inspeção

# 2. Configurar as colunas para análise
if 2 in dados.columns and 3 in dados.columns:
    inicio_coluna = dados[2]
    fim_coluna = dados[3]

    # Conversão para datetime e cálculo de tempo de resposta
    dados['inicio'] = pd.to_datetime(inicio_coluna, errors='coerce')
    dados['fim'] = pd.to_datetime(fim_coluna, errors='coerce')
    dados['tempo_resposta'] = dados['fim'] - dados['inicio']

    # Exibir os dados tratados
    st.write("Dados Tratados:")
    st.dataframe(dados[['inicio', 'fim', 'tempo_resposta']].head())

    # Análises estatísticas
    tempo_medio = dados['tempo_resposta'].mean()
    st.write(f"Tempo médio de resposta: {tempo_medio}")

    # Gráfico de distribuição do tempo de resposta
    if 'tempo_resposta' in dados.columns:
        dados['tempo_resposta_segundos'] = dados['tempo_resposta'].dt.total_seconds()

        # Criar o histograma
        st.write("Distribuição do Tempo de Resposta:")
        fig, ax = plt.subplots()
        ax.hist(dados['tempo_resposta_segundos'].dropna(), bins=20, color='blue', edgecolor='black')
        ax.set_title('Distribuição do Tempo de Resposta')
        ax.set_xlabel('Tempo de Resposta (segundos)')
        ax.set_ylabel('Frequência')
        st.pyplot(fig)

# 3. Exportar os dados
if st.button("Exportar Relatório"):
    dados.to_excel("C:\\Users\\Manoel\\.vscode\\relatorio_dashboard.xlsx", index=False)
    st.success("Relatório exportado com sucesso!")