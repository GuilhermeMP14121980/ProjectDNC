import pandas as pd
import os

# Função para verificar a existência e acessibilidade do arquivo
def verificar_arquivo(arquivo):
    """
    Verifica se o arquivo especificado existe e está acessível para leitura.
    :param arquivo: Caminho completo para o arquivo.
    :return: True se o arquivo existir e estiver acessível, False caso contrário.
    """
    if os.path.exists(arquivo):
        if os.access(arquivo, os.R_OK):
            print("Arquivo encontrado e está acessível.")
            return True
        else:
            print("Erro: O arquivo existe, mas não está acessível para leitura. Verifique as permissões.")
            return False
    else:
        print("Erro: Arquivo não encontrado. Verifique o caminho.")
        return False

# Função para limpar o arquivo CSV e resolver possíveis inconsistências
def corrigir_arquivo_csv(arquivo, arquivo_corrigido):
    """
    Lê o arquivo CSV original e corrige inconsistências como linhas com número incorreto de colunas.
    Salva o arquivo corrigido em um novo local.
    :param arquivo: Caminho do arquivo original.
    :param arquivo_corrigido: Caminho do arquivo corrigido.
    :return: Caminho do arquivo corrigido.
    """
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            linhas = file.readlines()
        
        # Corrige linhas inconsistentes
        colunas_esperadas = linhas[0].count(',')  # Número de colunas da primeira linha
        linhas_corrigidas = [
            linha for linha in linhas if linha.count(',') == colunas_esperadas
        ]

        # Salva o arquivo corrigido
        with open(arquivo_corrigido, 'w', encoding='utf-8') as file:
            file.writelines(linhas_corrigidas)

        print(f"Arquivo corrigido salvo em: {arquivo_corrigido}")
        return arquivo_corrigido
    except Exception as e:
        print(f"Erro ao corrigir o arquivo: {e}")
        return None

# Função para carregar os dados do arquivo CSV
def carregar_dados(arquivo):
    """
    Lê os dados de um arquivo CSV e retorna um DataFrame.
    :param arquivo: Caminho completo para o arquivo CSV.
    :return: DataFrame com os dados carregados ou None se houver erro.
    """
    try:
        # Lê o arquivo CSV
        dados = pd.read_csv(arquivo, encoding='utf-8')
        print(f"Dados carregados com sucesso de: {arquivo}")
        return dados
    except FileNotFoundError:
        print("Erro: Arquivo não encontrado. Verifique o caminho.")
        return None
    except pd.errors.ParserError as e:
        print(f"Erro ao carregar o arquivo CSV: {e}")
        print("Tentando corrigir o arquivo...")
        # Tentar corrigir e recarregar
        arquivo_corrigido = 'arquivo_corrigido.csv'
        corrigido = corrigir_arquivo_csv(arquivo, arquivo_corrigido)
        if corrigido:
            return carregar_dados(corrigido)
        else:
            print("Erro: Não foi possível corrigir o arquivo.")
            return None
    except Exception as e:
        print(f"Erro ao carregar o arquivo: {e}")
        return None

# Função para realizar testes nos dados
def testar_dados(dados):
    """
    Realiza testes nos dados carregados.
    :param dados: DataFrame com os dados a serem testados.
    """
    if dados is not None:
        print("\n--- Resultados dos Testes ---")
        # Teste 1: Verificar se há valores nulos
        tem_valores_nulos = dados.isnull().values.any()
        print(f"Há valores nulos nos dados? {'Sim' if tem_valores_nulos else 'Não'}")
        
        # Teste 2: Exibir resumo estatístico das colunas numéricas
        print("\nResumo estatístico:")
        print(dados.describe())
        
        # Teste 3: Informações gerais do DataFrame
        print("\nInformações gerais dos dados:")
        print(dados.info())
        
        # Teste 4: Visualizar as primeiras linhas
        print("\nPrimeiras linhas dos dados:")
        print(dados.head())
    else:
        print("Erro: Não foi possível realizar os testes. Os dados não foram carregados.")

# Caminho para o arquivo CSV
arquivo = "C:/Users/Manoel/Downloads/Material_Estatistica_Avancada.csv"

# Fluxo principal do programa
def main():
    """
    Função principal para executar o programa.
    """
    # Verificar se o arquivo existe e está acessível
    if verificar_arquivo(arquivo):
        # Carregar os dados do arquivo
        dados_carregados = carregar_dados(arquivo)
        
        # Testar os dados carregados
        testar_dados(dados_carregados)

# Executa o programa
if __name__ == "__main__":
    main()