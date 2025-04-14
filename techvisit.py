from transformers import pipeline
from langgraph import LangGraph, Node
from datetime import datetime

# Funções relacionadas ao modelo LLM
def iniciar_modelo_llm():
    """
    Inicializa o modelo LLM para geração de texto.
    """
    print("Inicializando o modelo LLM...")
    modelo_llm = pipeline("text-generation", model="gpt-2")  # Substituir por um modelo mais avançado, se necessário.
    print("Modelo carregado com sucesso!")
    return modelo_llm


# Funções relacionadas ao LangGraph e visitas técnicas
def configurar_langgraph_verificador_independente():
    """
    Configura o LangGraph com os nós necessários para realizar as funções
    de agendamento, registro e geração de relatórios de visitas técnicas como verificador independente.
    """
    # Inicializar o LangGraph
    graph = LangGraph(name="Chatbot para Verificador Independente")

    # Banco de dados de visitas técnicas
    visitas = []

    # Função: Agendar Visitas
    def agendar_visita(usuario_input):
        try:
            dados = usuario_input.split(",")  # Espera input no formato: "Escola X, DD/MM/AAAA"
            escola = dados[0].strip()
            data = datetime.strptime(dados[1].strip(), "%d/%m/%Y")
            visitas.append({"escola": escola, "data_planejada": data, "data_realizada": None, "observacoes": ""})
            return f"Visita técnica agendada como Verificador Independente para a escola {escola} em {data.strftime('%d/%m/%Y')}."
        except (IndexError, ValueError):
            return "Por favor, insira o formato correto: 'Escola X, DD/MM/AAAA'."

    # Função: Registrar Visitas
    def registrar_visita(usuario_input):
        try:
            dados = usuario_input.split(",")  # Espera input no formato: "Escola X, DD/MM/AAAA, Observações"
            escola = dados[0].strip()
            data = datetime.strptime(dados[1].strip(), "%d/%m/%Y")
            observacoes = dados[2].strip()

            for visita in visitas:
                if visita["escola"] == escola and visita["data_planejada"] == data:
                    visita["data_realizada"] = data
                    visita["observacoes"] = observacoes
                    return f"Visita realizada como Verificador Independente na escola {escola} em {data.strftime('%d/%m/%Y')}. Observações: {observacoes}"
            return "Visita planejada não encontrada. Certifique-se de que os dados estão corretos."
        except (IndexError, ValueError):
            return "Por favor, insira o formato correto: 'Escola X, DD/MM/AAAA, Observações'."

    # Função: Gerar Relatório de Visitas
    def visualizar_relatorio(_):
        relatorio = "Relatório de Visitas Técnicas - Verificador Independente:\n"
        if not visitas:
            return "Nenhuma visita técnica registrada até agora."
        for visita in visitas:
            relatorio += (
                f"- Escola: {visita['escola']}\n"
                f"  Data Planejada: {visita['data_planejada'].strftime('%d/%m/%Y')}\n"
                f"  Data Realizada: {visita['data_realizada'].strftime('%d/%m/%Y') if visita['data_realizada'] else 'Não realizada'}\n"
                f"  Observações: {visita['observacoes'] if visita['observacoes'] else 'Nenhuma'}\n"
            )
        return relatorio

    # Adicionar funções como nós no LangGraph
    graph.add_node(Node("agendar_visita", agendar_visita))
    graph.add_node(Node("registrar_visita", registrar_visita))
    graph.add_node(Node("visualizar_relatorio", visualizar_relatorio))

    return graph


# Função principal de interação com o chatbot
def chatbot_interativo(graph):
    """
    Gerencia a interação com o chatbot. Permite ao usuário executar comandos para agendar visitas,
    registrar visitas realizadas e visualizar relatórios.
    """
    print("Chatbot inicializado para Visitas Técnicas como Verificador Independente!")
    print("Digite 'sair' para encerrar.")
    print("Comandos disponíveis: agendar_visita, registrar_visita, visualizar_relatorio")

    while True:
        comando = input("Digite o comando: ")
        if comando.lower() == "sair":
            print("Chatbot encerrado. Até a próxima!")
            break

        mensagem_usuario = input("Insira os dados: ")
        if comando in graph.nodes:
            resposta = graph.run(comando, mensagem_usuario)
            print("Chatbot:", resposta)
        else:
            print("Comando inválido. Tente novamente.")


# Execução do programa principal
if __name__ == "__main__":
    langgraph = configurar_langgraph_verificador_independente()
    chatbot_interativo(langgraph)