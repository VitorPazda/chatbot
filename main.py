# Migrando para o gemini

import os
from google import genai
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Carregar .env 
load_dotenv()

# Iniciar cliente
client = genai.Client()

databasePath = "db"

# Processar PDF
# Se a pasta 'db' não existir, vamos ler o PDF e criar o banco vetorial
if not os.path.exists(databasePath):
    print("Processando o pdf e criando o bd")
    
    loader = PyPDFLoader("GuiaGragas.pdf") 
    paginas = loader.load()
    
    # Dividindo o pdf em chunks
    textSplitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=100)
    textosDivididos = textSplitter.split_documents(paginas)
    embeddingFunction = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Cria e salva o banco
    db = Chroma.from_documents(textosDivididos, embeddingFunction, persist_directory=databasePath)
else:
    # Se o bd existe, irá carregar e não criar
    embeddingFunction = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory=databasePath, embedding_function=embeddingFunction)

# Pergunta ao usuario
os.system('cls' if os.name == 'nt' else 'clear')
pergunta = input("\nEscreva sua pergunta sobre como jogar de Gragas: ")

# Busca os trechos mais relevantes do pdf
resultados = db.similarity_search(pergunta, k=3)

# Une os textos da base de conhecimento (pdf)
baseConhecimento = "\n\n".join([doc.page_content for doc in resultados])

# O seu template de prompt adaptado para o Gemini
promptTemplate = f"""
Responda a pergunta do usuário:
{pergunta}

com base nessas informações:
{baseConhecimento}

Caso não encontre a resposta para a pergunta do usuário nessas informações, 
responda estritamente que não sabe dizer, não invente nada fora do documento
"""

print("\nConsultando o Gemini")

# Envia o prompt estruturado para o Gemini gerar a resposta pro player
resposta = client.models.generate_content(
    model='gemini-2.5-flash',
    contents=promptTemplate,
)

print("Resposta")
print(resposta.text)