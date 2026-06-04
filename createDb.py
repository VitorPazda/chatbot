from langchain_community.document_loaders import PyPDFDirectoryLoader

baseFolder = "base"

def loadDocuments():
    loader = PyPDFDirectoryLoader(baseFolder, glob="*.pdf")

def createDb():
    documents = loadDocuments()
    chunks = splitChunks(documents)
    vectorizeChunks(chunks)
    # carregar os documentos
    # dividir os documentos em pedacos
    pass

createDb()