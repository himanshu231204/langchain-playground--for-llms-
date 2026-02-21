from langchain_ollama import OllamaEmbeddings
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.documents import Document
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS


# 1️⃣ Use Updated Ollama Embedding Model
embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe:latest"
)

# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]
#create the fassis vector store from the documents

vector_store = FAISS.from_documents(
    documents=docs,
    embedding=embeddings_model
)

#create  the MMR retriever from the vector store

mmr_retriever = vector_store.as_retriever(
    search_type="mmr",  #this will enable the MMR retrieval strategy 
    search_kwargs={
        "k": 2, 
    "lambda_mult": 0.5} # lambda_mult is a parameter that controls the balance between relevance and diversity in the MMR algorithm. A value of 0.5 gives equal weight to both factors.
    )  


query = "What are the benefits of using LangChain for LLM applications?"

# Retrieve relevant documents using the MMR retriever
reults = mmr_retriever.invoke(query)

#print the relevant documents
for i,docs in enumerate(reults):
    print(f"Document {i+1}:")
    print(f"Content: {docs.page_content[:500]}...")  # Print the first 500 characters of the content
    print("\n---\n")
