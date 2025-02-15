
# Utilizando Langchain para acessar o Modelo de Linguagem 
# !pip install langchain
# !pip install langchain-groq

import os
from langchain_groq import ChatGroq

# Craindo uma api key - Groq 
API_KEY = "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"

# Conexão com o modelo de linguagem
def conection():
    API_KEY = "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"
    os.environ["GROQ_API_KEY"] = API_KEY
    chat = ChatGroq(model="llama-3.3-70b-versatile")
    return chat

# Teste de requisição
resposta = conection().invoke("Teste 0: Olá Modelo! O que pode fazer?")
print(resposta.content)