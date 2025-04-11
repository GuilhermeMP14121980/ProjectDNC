from flask import Flask, request, jsonify
from pymongo import MongoClient
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

# Configuração do MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["chatbot_rag"]
colecao = db["documentos"]

# Configuração do Flask
app = Flask(__name__)

# Configuração do RAG
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
vectorstore = Chroma(persist_directory="chroma_db", embedding_function=embeddings)
llm = OpenAI(model="gpt-3.5-turbo")  # Ou outro modelo disponível
qa = RetrievalQA(llm=llm, retriever=vectorstore.as_retriever())

# Endpoint para adicionar documentos ao MongoDB
@app.route('/adicionar_documento', methods=['POST'])
def adicionar_documento():
    dados = request.json
    colecao.insert_one(dados)
    return jsonify({"mensagem": "Documento adicionado com sucesso!"})

# Endpoint para buscar resposta com base em perguntas do usuário
@app.route('/perguntar', methods=['POST'])
def perguntar():
    pergunta = request.json.get("pergunta")
    
    # Recupera embeddings relevantes e passa para o LLM
    resposta = qa.run(pergunta)
    return jsonify({"resposta": resposta})

# Endpoint para buscar documentos por título
@app.route('/buscar_por_titulo', methods=['POST'])
def buscar_por_titulo():
    titulo = request.json.get("titulo")
    documento = colecao.find_one({"titulo": titulo})
    if documento:
        return jsonify({
            "titulo": documento["titulo"],
            "tema": documento["tema"],
            "caminho_arquivo": documento["caminho_arquivo"]
        })
    else:
        return jsonify({"erro": "Documento não encontrado."})

if __name__ == '__main__':
    app.run(debug=True)