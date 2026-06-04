from langchain_community.document_loaders import PyPDFDirectoryLoader

baseFolder = "base"

def loadDocuments():
    loader = PyPDFDirectoryLoader(baseFolder, glob="*.pdf")
    documents = loader.load()
    return documents

def createDb():
    documents = loadDocuments()
    print(documents)
    #chunks = splitChunks(documents)
    #vectorizeChunks(chunks)
    # carregar os documentos
    # dividir os documentos em pedacos
    pass

createDb()