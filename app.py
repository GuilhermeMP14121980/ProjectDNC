import streamlit as st
import requests
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

# Configure a chave da API OpenAI
import os
os.environ["OPENAI_API_KEY"] = "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"

# Função para obter dados do município via API IBGE
def get_municipality_data(municipality_id):
    if not municipality_id:
        return {"error": "ID do município não fornecido."}
    
    url = f"https://servicodados.ibge.gov.br/api/v3/agregados/7392/periodos/2014/variaveis/10484?localidades=N1[all]"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Não foi possível obter os dados. Status code: {response.status_code}"}

# Inicialize o LangChain para conversas
llm = ChatOpenAI()
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

# Configurar interface Streamlit
st.title("Chatbot Simplificado")
st.subheader("Busque dados ou converse com o assistente!")

# Entrada do usuário
user_input = st.text_input("Digite um comando ou mensagem:")

# Lógica de Comandos
if user_input:
    if user_input.lower().startswith("municipio:"):
        # Buscar dados do município
        municipio_id = user_input.split("municipio:")[1].strip()
        municipio_data = get_municipality_data(municipio_id)
        st.json(municipio_data)
    else:
        # Conversa com LangChain
        response = conversation.predict(input=user_input)
        st.write(response)