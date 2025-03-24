import requests
from googleapiclient.discovery import build
from langdetect import detect
from flask import Flask, request

# Função para obter dados da API do IBGE
def get_ibge_data(endpoint):
    url = f"https://api.ibge.gov.br/{endpoint}"
    response = requests.get(url)
    return response.json()

# Função para agendar eventos usando Google Calendar
def schedule_event(service, event):
    service.events().insert(calendarId='primary', body=event).execute()

# Função para identificar a linguagem de um texto
def identify_language(text):
    return detect(text)

# Configuração do Flask para detectar linguagem
app = Flask(__name__)

@app.route('/language', methods=['POST'])
def detect_language():
    data = request.json
    language = identify_language(data['text'])
    return {'language': language}

# Função para responder aos comandos do bot
def responder_comando(comando):
    if comando == "olá":
        return "Olá! Como posso ajudar?"
    elif comando == "ajuda":
        return """Aqui está o que eu posso fazer: 
        - Dizer 'olá'
        - Procurar serviços
        - Oferecer mensagens de vendas
        - Encerrar"""
    elif comando == "procurar serviços":
        return "Por favor, digite o serviço que deseja procurar:"
    elif comando.startswith("serviço:"):
        servico = comando.split("serviço:")[1].strip()
        return f"Buscando informações sobre o serviço '{servico}'... (exemplo: aqui você pode integrar com uma API de serviços)"
    elif comando == "mensagem de vendas":
        return "Aqui está uma mensagem de vendas: 'Aproveite nossa promoção especial! Ligue agora para saber mais.'"
    elif comando == "sair":
        return "Tchau! Até a próxima."
    else:
        return "Desculpe, não entendi esse comando."

# Loop principal do bot no terminal
if __name__ == "__main__":
    print("Bem-vindo ao bot interno! Digite um comando:")
    while True:
        comando_usuario = input("> ").lower()
        resposta = responder_comando(comando_usuario)
        print(resposta)
        if comando_usuario == "sair":
            break


    
