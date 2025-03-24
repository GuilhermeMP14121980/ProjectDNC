import requests
from flask import Flask, request

# Função para obter dados de um município pela API do IBGE
def get_municipality_data(municipality_id):
    if not municipality_id:
        return {"error": "ID do município não fornecido."}
    
    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/7392/periodos/2014/variaveis/10484?localidades=N1[all]"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Não foi possível obter os dados. Status code: {response.status_code}"}
   
# Configuração do Flask para detectar linguagem e buscar dados de município
app = Flask(__name__)

@app.route('/language', methods=['POST'])
def detect_language():
    data = request.json
    language = identify_language(data['text'])
    return {'language': language}

@app.route('/municipality', methods=['GET'])
def fetch_municipality():
    municipality_id = request.args.get('municipality_id')
    if not municipality_id:
        return {"error": "ID do município não fornecido."}
    
    municipality_data = get_municipality_data(municipality_id)
    return municipality_data

# Função para responder aos comandos do bot
def responder_comando(comando):
    if comando == "olá":
        return "Olá! Como posso ajudar?"
    elif comando == "ajuda":
        return """Aqui está o que eu posso fazer: 
        - Dizer 'olá'
        - Procurar serviços
        - Buscar dados de municípios
        - Oferecer mensagens de vendas
        - Encerrar"""
    elif comando == "procurar serviços":
        return "Por favor, digite o serviço que deseja procurar:"
    elif comando.startswith("municipio:"):
        municipio_id = comando.split("municipio:")[1].strip()
        municipio_data = get_municipality_data(municipio_id)
        return f"Dados do município: {municipio_data}"
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