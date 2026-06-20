# Chatbot - Python

Este é um chatbot RAG focado no campeão Gragas do League of Legends. O projeto utiliza Python, o banco de dados vetorial ChromaDB e a API oficial do Google Gemini 
como modelo de linguagem para responder perguntas com base estritamente em um guia em PDF local

Funcionamento

1. Leitura do PDF: O script lê um arquivo PDF (`GuiaGragas.pdf`)
2. Chunking (Divisão): O texto é quebrado em pedaços menores para otimizar a busca de contexto
3. Embeddings: Os pedaços de texto são transformados em vetores matemáticos
4. Banco Vetorial: Esses vetores são armazenados localmente na pasta `db` através do ChromaDB
5. Consulta ao Gemini: Quando você faz uma pergunta, o sistema busca os 3 trechos mais relevantes do PDF e os envia ao Gemini 2.5 Flash para gerar uma resposta precisa e contextualizada

Tecnologias e Bibliotecas Utilizadas

O projeto foi construído utilizando o ecossistema moderno do **LangChain** e o SDK oficial da Google:

1. `os` (Nativo do Python)
2. `google-genai` (SDK Oficial da Google para o Gemini)
3. `python-dotenv` (Gerenciamento seguro de credenciais)
4. `langchain-community` (Integrações com loaders e vectorstores)
5. `langchain-text-splitters` (Divisor de texto inteligente)
6. `langchain-chroma` / `chromadb` (Banco de dados vetorial local)
7. `sentence-transformers` (Para os embeddings do HuggingFace)
8. `pypdf` (Leitor de arquivos PDF)

Como Rodar

Siga o passo a passo abaixo para configurar e executar o projeto na sua máquina:

1. Clonar o Repositório
git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)
cd NOME_DO_REPOSITORIO

2. Instalar as Bibliotecas
pip install google-genai python-dotenv langchain langchain-community langchain-chroma chromadb sentence-transformers pypdf

3. Criar o Arquivo .env na raiz do projeto

4. Adicionar a sua chave Gemini Api Key
GEMINI_API_KEY=AIzaSySuaChaveGeradaNoAIStudioAqui

5. Executar
