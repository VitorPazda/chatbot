# todas as biliotecas necessárias

# pip install python-dotenv langchain langchain-openai langchain-community langchain-chroma chromadb openai pypdf

# chroma é o responsável em vetorizar o banco de dados

from langchain_chroma.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

databasePath = "db"

promptTemplate = """
Responda a pergunta do usuário
{pergunta}

com base nessas informações

{baseConhecimento}

Caso não encontre a resposta para a pergunta do usuário nessas informações, 
responda que não sabe dizer."""

question = input("Escreva sua pergunta: ")

# carregar db
embeddingFunction = OpenAIEmbeddings()
db = Chroma(persist_directory=databasePath, embedding_function=embeddingFunction)

# comparar a pergunta do usuario, com o db
results = db.similarity_search_with_relevance_scores(question)
print(results)
print(len(results))