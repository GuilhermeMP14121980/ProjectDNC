import pandas as pd

# Carregar o arquivo Excel
try:
    dados_censo = pd.read_csv('arquivo.csv')  # Certifique-se que o arquivo está na mesma pasta
    print("Arquivo carregado com sucesso.")
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado. Verifique o caminho ou nome.")
    exit()

# Inspecionar os dados
print("Primeiras linhas do DataFrame:")
print(dados_censo.head())

print("\nInformações gerais:")
print(dados_censo.info())

print("\nEstatísticas descritivas das colunas numéricas:")
print(dados_censo.describe())

# Etapas de tratamento de dados
print("\nIniciando tratamento de dados...")

# 1. Identificar e tratar valores ausentes
print("\nValores ausentes antes do tratamento:")
print(dados_censo.isnull().sum())

# Preencher valores ausentes (exemplo: preenchimento com valores padrão)
dados_censo.fillna("Não informado", inplace=True)

print("\nValores ausentes após o tratamento:")
print(dados_censo.isnull().sum())

# 2. Converter tipos de dados (se necessário)
# Exemplo: Convertendo colunas numéricas que estão como objetos
for col in dados_censo.columns:
    if dados_censo[col].dtype == 'object':
        try:
            dados_censo[col] = pd.to_numeric(dados_censo[col], errors='ignore')
        except ValueError:
            pass  # Ignorar conversões que não fazem sentido para números

# 3. Remover duplicatas, se existirem
print("\nRemovendo duplicatas...")
dados_censo.drop_duplicates(inplace=True)
print(f"Total de linhas após remoção de duplicatas: {len(dados_censo)}")

# 4. Normalizar texto (exemplo: transformar tudo para letras minúsculas)
colunas_texto = dados_censo.select_dtypes(include=['object']).columns
for col in colunas_texto:
    dados_censo[col] = dados_censo[col].str.lower()

# Exibir resumo dos dados tratados
print("\nResumo após tratamento:")
print(dados_censo.head())

# Salvar os dados tratados em um novo arquivo Excel
dados_censo.to_excel('dados_censo_tratados.xlsx', index=False)
print("\nDados tratados foram salvos em 'dados_censo_tratados.xlsx'.")