# Importação das bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# 1. Carregar os dados do arquivo Excel
# Carregar os dados sem cabeçalhos ajustados
dados = pd.read_csv(arquivo.csv, header=None)
print("Dados brutos carregados:")
print(dados.head(10))  # Exibir os primeiros 10 registros para inspeção

# 2. Trabalhar diretamente com os dados brutos
# Exibir os nomes das colunas conforme carregados
print("Colunas disponíveis no DataFrame:")
print(dados.columns)

# 3. Inspecionar o conteúdo das colunas
# Verificar os primeiros registros de cada coluna para identificar onde estão os dados relevantes
for col in dados.columns:
    print(f"Conteúdo da coluna {col}:")
    print(dados[col].head(10))

# 4. Operações específicas com os dados (se aplicável)
# Exemplo de visualização ou manipulação direta de colunas brutas
# Vamos supor que os dados relevantes estão nas colunas 'coluna_2' e 'coluna_3'
if 2 in dados.columns and 3 in dados.columns:  # Verificar os índices das colunas brutas
    inicio_coluna = dados[2]  # Coluna com dados de 'inicio'
    fim_coluna = dados[3]     # Coluna com dados de 'fim'

    # Converter para datetime diretamente sem renomear
    dados['inicio'] = pd.to_datetime(inicio_coluna, errors='coerce')
    dados['fim'] = pd.to_datetime(fim_coluna, errors='coerce')

    # Calcular tempo de resposta
    dados['tempo_resposta'] = dados['fim'] - dados['inicio']
    print("Dados tratados com 'inicio', 'fim' e 'tempo_resposta':")
    print(dados[['inicio', 'fim', 'tempo_resposta']].head())
else:
    print("As colunas relevantes para 'inicio' e 'fim' não foram identificadas. Verifique o arquivo Excel.")

# 5. Visualizar os dados (se aplicável)
if 'tempo_resposta' in dados.columns:
    dados['tempo_resposta_segundos'] = dados['tempo_resposta'].dt.total_seconds()
    plt.hist(dados['tempo_resposta_segundos'].dropna(), bins=20, color='blue', edgecolor='black')
    plt.title('Distribuição do Tempo de Resposta')
    plt.xlabel('Tempo de Resposta (segundos)')
    plt.ylabel('Frequência')
    plt.show()
else:
    print("A coluna 'tempo_resposta' não está disponível para visualização.")

# 6. Exportar os dados tratados
dados.to_csv(local do arquivo.csv\\relatorio_final_tratado.csv", index=False)
print("Relatório exportado com sucesso para 'relatorio_final_tratado.xlsx'.")