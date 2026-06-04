from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

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
    print(len(chunks))
    return chunks

def vectorizeChunks(chunks):
    pass

def createDb():
    documents = loadDocuments()
    print(documents)
    chunks = splitChunks(documents)
    vectorizeChunks(chunks)

createDb()