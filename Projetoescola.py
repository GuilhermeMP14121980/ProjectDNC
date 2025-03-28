import sqlite3
import requests
import os
from flask import Flask, request, jsonify
import streamlit as st
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
from Services import calcular_taxa_desistencia

openai_api_key = os.getenv("OPENAI_API_KEY")
import os
print(os.getenv("OPENAI_API_KEY"))  # Deve imprimir a chave da API

llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    temperature=0.7,
    openai_api_key="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"
)

# Memória de conversação
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory()

conversation = ConversationChain(
    llm=llm,
    memory=st.session_state.memory,
    verbose=False
)

# Interface Streamlit
st.title("Meu Chatbot Dinamizado")

user_input = st.text_input("Digite sua mensagem:")
if user_input:
    response = conversation.predict(input=user_input)
    st.write(response)

# Inicialização do Flask
app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()
    mensagem = data['mensagem'].lower()

    if mensagem.startswith("quantidade alunos"):
        resposta = consultar_quantidade_alunos()
    elif mensagem.startswith("taxa desistencia"):
        nivel = mensagem[17:].strip()
        resposta = calcular_taxa_desistencia(nivel)
    else:
        resposta = gerar_resposta_llm(mensagem)

    return jsonify({"resposta": resposta})

def gerar_resposta_llm(mensagem):
    prompt = f"Pergunta do usuário: {mensagem}\nResponda com base nos dados da escola."
    resposta = llm.predict(prompt)
    return resposta.strip()

def consultar_quantidade_alunos():
    try:
        con = sqlite3.connect('educacao.db')
        cur = con.cursor()
        cur.execute('SELECT COUNT(*) FROM alunos WHERE matriculado = 1')
        quantidade = cur.fetchone()[0]
        con.close()
        return f"Há {quantidade} alunos matriculados atualmente."
    except sqlite3.Error as e:
        return f"Erro ao consultar os dados: {e}"

def criar_tabelas():
    con = sqlite3.connect('educacao.db')
    cur = con.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        nivel_escolar TEXT,
        bairro TEXT,
        matriculado INTEGER,
        desistente INTEGER
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS familias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_aluno INTEGER,
        renda_media REAL,
        FOREIGN KEY(id_aluno) REFERENCES alunos(id)
    )
    ''')
    cur.execute('''
    CREATE TABLE IF NOT EXISTS municipios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        estado TEXT,
        populacao_estimada INTEGER
    )
    ''')
    con.commit()
    con.close()

# Criando tabelas ao iniciar
criar_tabelas()

if __name__ == "__main__":
    app.run(debug=False)