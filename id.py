from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Classe Dado
class Dado:
    def __init__(self, identificador, conteudo):
        self.identificador = identificador
        self.conteudo = conteudo

# Funções auxiliares
def gerar_identificador(conteudo):
    palavras = conteudo.split()
    identificador = "-".join(palavras[:3])
    return identificador.lower()

def receber_dado(dados, conteudo):
    identificador = gerar_identificador(conteudo)
    novo_dado = Dado(identificador, conteudo)
    dados.append(novo_dado)
    return f"Dado com ID '{identificador}' recebido com sucesso!"

# Lista para armazenar os dados
dados_recebidos = []

# Rota para receber mensagens do WhatsApp
@app.route("/webhook", methods=["POST"])
def whatsapp_webhook():
    # Captura a mensagem recebida
    mensagem = request.form.get("Body")  # Mensagem enviada pelo usuário

    # Processa a mensagem e armazena o dado
    resposta = receber_dado(dados_recebidos, mensagem)

    # Envia a resposta para o usuário
    twiml = MessagingResponse()
    twiml.message(resposta)
    return str(twiml)

# Inicializa o servidor
if __name__ == "__main__":
    app.run(debug=True)

