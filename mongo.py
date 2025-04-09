import pymongo
from langchain.llms import OpenAI
from datetime import datetime

# Configuração do MongoDB
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "chatbot_db"
COLLECTION_NAME = "chat_logs"

client = pymongo.MongoClient(MONGO_URI)
db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Função para salvar mensagens no MongoDB
def salvar_log(usuario, bot, timestamp):
    log = {
        "usuario": usuario,
        "bot": bot,
        "timestamp": timestamp
    }
    collection.insert_one(log)

# Função principal do chatbot
def chatbot(mensagem_usuario):
    llm = OpenAI(temperature=0)  # Configure o modelo de linguagem
    resposta_bot = llm.predict(mensagem_usuario)  # Processa a entrada do usuário

    # Salvar logs no MongoDB
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    salvar_log(mensagem_usuario, resposta_bot, timestamp)

    return resposta_bot

# Teste do chatbot
if __name__ == "__main__":
    print("Bem-vindo ao chatbot! Digite 'sair' para encerrar.")
    while True:
        mensagem_usuario = input("Você: ")
        if mensagem_usuario.lower() == "sair":
            print("Encerrando o chatbot...")
            break
        resposta_bot = chatbot(mensagem_usuario)
        print(f"Bot: {resposta_bot}")