from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma.vectorstores import Chroma
# from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

baseFolder = "base"

def loadDocuments():
    loader = PyPDFDirectoryLoader(baseFolder, glob="*.pdf")
    documents = loader.load()
    return documents

def splitChunks(documents):
    documentSplitter = RecursiveCharacterTextSplitter(
        chunk_size = 2000, 
        chunk_overlap = 500,
        length_function = len,
        add_start_index = True
    )

    chunks = documentSplitter.split_documents(documents)
    return chunks

def vectorizeChunks(chunks):
    # db = Chroma.from_documents(chunks, OpenAIEmbeddings(), persist_directory="db")
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    db = Chroma.from_documents(chunks,embeddings,persist_directory="db")
    print("Database created successfully")

def createDb():
    documents = loadDocuments()
    print(documents)
    chunks = splitChunks(documents)
    vectorizeChunks(chunks)

createDb()