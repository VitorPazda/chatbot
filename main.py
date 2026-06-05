# todas as biliotecas necessárias

# pip install python-dotenv langchain langchain-openai langchain-community langchain-chroma chromadb openai pypdf langchain-ollama

# Teste hugging face
# pip install langchain-huggingface sentence-transformers

# chroma é o responsável em vetorizar o banco de dados

from langchain_chroma.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama
from dotenv import load_dotenv

load_dotenv()

databasePath = "db"

promptTemplate = """
Responda a pergunta do usuário
{question}

com base nessas informações

{baseConhecimento}

Caso não encontre a resposta para a pergunta do usuário nessas informações, 
responda que não sabe dizer."""

def ask():
    question = input("Escreva sua pergunta: ")

    # carregar db
    # embeddingFunction = OpenAIEmbeddings()
    embeddingFunction = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma(persist_directory=databasePath, embedding_function=embeddingFunction)

    # comparar a pergunta do usuario, com o db
    results = db.similarity_search_with_relevance_scores(question, k=3)
    #if len(results) == 0 or results[0][1] < 0.7:
    #    print("Não achei nada relevante na base de dados")
    #    return 
    
    textsResult = []
    for result in results:
        text = result[0].page_content
        textsResult.append(text)

    baseConhecimento = "\n\n---\n\n".join(textsResult)
    prompt = ChatPromptTemplate.from_template(promptTemplate)
    prompt = prompt.invoke({"question": question, "baseConhecimento": baseConhecimento})

    model = ChatOllama()
    textAnswer = model.invoke(prompt)
    print(textAnswer)
    
ask()
