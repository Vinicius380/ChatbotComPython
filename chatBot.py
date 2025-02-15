# !pip install langchain
# !pip install langchain-groq
# !pip install langchain-community
# !pip install beautifulsoup4
# !pip install youtube_transcript_api
# !pip install pypdf

from langchain.prompts import ChatPromptTemplate
from conexao import conection
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import YoutubeLoader

def resposta_bot(mensagens, documento):
    
    mensagem_system = '''Você é um assistente chamado Bot.IA.
    Utiliza as seguintes informações para formular as suas respostas: {informacoes}'''
    
    mensagens_modelo = [('system', mensagem_system)]
    mensagens_modelo += mensagens
    template = ChatPromptTemplate.from_messages(mensagens_modelo)
    Chat = conection()
    chain = template | Chat
    return chain.invoke({'informacoes:', documento}).content

def carrega_site():
    url_site = input("Digite a URL do site: ")
    loader = WebBaseLoader(url_site)
    lista_documentos = loader.load() 
    documento = ''
    for doc in lista_documentos:
     documento += doc.page_content
    return documento

def carrega_pdf():
    arquivo = 'RoteiroViagemEgito.pdf'
    loader_pdf = PyPDFLoader(arquivo)
    lista_documentos_pdf = loader_pdf.load() 
    documento = ''
    for doc in lista_documentos_pdf:
     documento_pdf += doc.page_content
    return documento

def carrega_youtube():
    url_video = input("Digite a URL do video: ")
    loader = YoutubeLoader.from_youtube_url(url_video, language=['pt'])
    lista_documentos_youtube = loader.load()  
    documento = ''
    for doc in lista_documentos_youtube:
        documento += doc.page_content
    return documento

print('Bem-vindo ao Bot.IA!')

texto_selecao = ''' 
Digite 1 se você quiser conversar com um site: 
Digite 2 se você quiser conversar com um pdf:  
Digite 3 se você quiser conversar com um video de youtube: 
'''

while True:
    selecao = input(texto_selecao)
    if selecao == "1":
        documento = carrega_site
        break
    if selecao == "2":
        documento = carrega_pdf
        break
    if selecao == "3":
        documento = carrega_youtube
        break
    print("Digite um valor entre 1 e 3: ")

mensagens = []
while True:
    pergunta = input('Usuário: ' )
    if pergunta.lower() == 'x':
        break
    mensagens.append(('user', pergunta))
    resposta = resposta_bot(mensagens, documento)
    mensagens.append(('assistant', resposta))
    print(f'Bot: {resposta}')

print('Muito obrigado por usar o Bot.IA')
print(mensagens)