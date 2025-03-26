city_data = {
    "São Paulo": {
        "população": "12,33 milhões",
        "pontos_turisticos": ["Parque Ibirapuera", "Avenida Paulista", "Mercado Municipal", "Catedral da Sé"],
        "universidade": "Universidade de São Paulo (USP)"
    },
    "Rio de Janeiro": {
        "população": "6,7 milhões",
        "pontos_turisticos": ["Cristo Redentor", "Pão de Açúcar", "Praia de Copacabana"],
        "universidade": "Universidade Federal do Rio de Janeiro (UFRJ)"
    },
    "Salvador": {
        "população": "2,9 milhões",
        "pontos_turisticos": ["Pelourinho", "Elevador Lacerda", "Farol da Barra"],
        "universidade": "Universidade Federal da Bahia (UFBA)"
    },
    "Belo Horizonte": {
        "população": "2,5 milhões",
        "pontos_turisticos": ["Praça da Liberdade", "Igreja São José", "Museu de Artes e Ofícios"],
        "universidade": "Universidade Federal de Minas Gerais (UFMG)"
    },
    "Fortaleza": {
        "população": "2,7 milhões",
        "pontos_turisticos": ["Praia do Futuro", "Catedral Metropolitana", "Mercado Central"],
        "universidade": "Universidade Federal do Ceará (UFC)"
    },
    "Brasília": {
        "população": "3,1 milhões",
        "pontos_turisticos": ["Congresso Nacional", "Catedral de Brasília", "Palácio do Planalto"],
        "universidade": "Universidade de Brasília (UnB)"
    },
    "Curitiba": {
        "população": "1,9 milhões",
        "pontos_turisticos": ["Jardim Botânico", "Ópera de Arame", "Rua XV de Novembro"],
        "universidade": "Universidade Federal do Paraná (UFPR)"
    },
    "Porto Alegre": {
        "população": "1,5 milhões",
        "pontos_turisticos": ["Parque Redenção", "Caminho dos Antiquários", "Fundação Iberê Camargo"],
        "universidade": "Universidade Federal do Rio Grande do Sul (UFRGS)"
    },
    "Recife": {
        "população": "1,6 milhões",
        "pontos_turisticos": ["Praia de Boa Viagem", "Instituto Ricardo Brennand", "Marco Zero"],
        "universidade": "Universidade Federal de Pernambuco (UFPE)"
    },
    "Manaus": {
        "população": "2,1 milhões",
        "pontos_turisticos": ["Teatro Amazonas", "Encontro das Águas", "Palácio Rio Negro"],
        "universidade": "Universidade Federal do Amazonas (UFAM)"
    },
    "Natal": {
        "população": "1,4 milhões",
        "pontos_turisticos": ["Forte dos Reis Magos", "Praia de Ponta Negra", "Dunas de Genipabu"],
        "universidade": "Universidade Federal do Rio Grande do Norte (UFRN)"
    },
    "Maceió": {
        "população": "1,0 milhão",
        "pontos_turisticos": ["Praia do Francês", "Palácio Marechal Floriano Peixoto", "Igreja de São Gonçalo do Amarante"],
        "universidade": "Universidade Federal de Alagoas (UFAL)"
    },
    "Cuiabá": {
        "população": "620 mil",
        "pontos_turisticos": ["Parque Nacional de Chapada dos Guimarães", "Catedral Basílica do Senhor Bom Jesus", "Museu do Morro da Caixa D'Água"],
        "universidade": "Universidade Federal de Mato Grosso (UFMT)"
    },
    "Aracaju": {
        "população": "650 mil",
        "pontos_turisticos": ["Praia de Atalaia", "Museu Palácio Marechal Floriano Peixoto", "Mercado Municipal"],
        "universidade": "Universidade Federal de Sergipe (UFS)"
    }
}

def chatbot():
    print("Olá! Sou um chatbot que pode te ajudar com informações sobre algumas cidades brasileiras.")
    cidade_atual = None  # Variável para armazenar a cidade em contexto

    while True:
        pergunta = input("Faça sua pergunta (ou digite 'sair' para encerrar): ")
        if pergunta.lower() == 'sair':
            print("Até logo!")
            break

        # Verifica se uma cidade foi mencionada na pergunta
        for cidade in city_data:
            if cidade.lower() in pergunta.lower():
                cidade_atual = cidade
                break

        if not cidade_atual:
            print("Por favor, mencione uma cidade para que eu possa te ajudar!")
            continue

        # Responde à pergunta com base na cidade
        if "população" in pergunta.lower():
            print(f"A população de {cidade_atual} é {city_data[cidade_atual]['população']}.")

        elif "pontos turísticos" in pergunta.lower():
            pontos = ', '.join(city_data[cidade_atual]['pontos_turisticos'])
            print(f"Os pontos turísticos de {cidade_atual} são: {pontos}.")

        elif "universidade" in pergunta.lower():
            print(f"A principal universidade de {cidade_atual} é {city_data[cidade_atual]['universidade']}.")

        else:
            print("Desculpe, não entendi sua pergunta. Tente perguntar sobre população, pontos turísticos ou universidade.")

if __name__ == "__main__":
    chatbot()