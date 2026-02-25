from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain.retrievers import ContextualCompressionRetriever # type: ignore
from langchain.retrievers.document_compressors import LLMChainExtractor # type: ignore
# Embeddings
embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe:latest"
)

# LLM
llm = ChatOllama(model="mistral")

# Sample docs
docs = [
    Document(page_content="Walking improves heart health and reduces stress."),
    Document(page_content="Leafy greens improve digestion and increase lifespan."),
    Document(page_content="Python is used for AI development."),
]

# Vector store
vector_store = FAISS.from_documents(docs, embeddings_model)

base_retriever = vector_store.as_retriever(search_kwargs={"k": 2})

#  Compressor 
compressor = LLMChainExtractor.from_llm(llm)

compression_retriever = ContextualCompressionRetriever(
    base_retriever=base_retriever,
    base_compressor=compressor
)

query = "How does walking improve health?"

results = compression_retriever.invoke(query)

for doc in results:
    print(doc.page_content)