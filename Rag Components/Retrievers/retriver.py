from langchain_ollama import OllamaEmbeddings
from langchain_community.retrievers import WikipediaRetriever
from langchain_core.documents import Document
from langchain_ollama import ChatOllama
from langchain_chroma import Chroma
from langchain_community.vectorstores import Chroma


# 1️⃣ Use Updated Ollama Embedding Model
embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe"
)

# 2️⃣ Create a Wikipedia Retriever
retriever = WikipediaRetriever(
    language="en",  # Language of the Wikipedia articles
    top_k=2,       # Number of relevant articles to retrieve
    embedding_function=embeddings_model  # Use the Ollama embeddings for retrieval
)

#define a query
query="the geopolitical history of india and pakistan from the perspective of a chinese"


# 3️⃣ Retrieve relevant Wikipedia articles based on the query
docs = retriever.invoke(query)

#print(docs)

#print the relevant documents

for i,docs in enumerate(docs):
    print(f"Document {i+1}:")
   # print(f"Title: {docs.metadata['title']}")
   # print(f"URL: {docs.metadata['url']}")
    print(f"Content: {docs.page_content[:500]}...")  # Print the first 500 characters of the content
    print("\n---\n")
    
    
    


#Vectorstore retriever
 
#  Your source documents
documents = [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="ollama provides powerful embedding models."),
]

# Create a Chroma vector store from the documents
vector_store = Chroma.from_documents(
    documents=documents,
 embedding=embeddings_model,
    collection_name="my_collection")

#convert vector store to retriever

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# Define a query
query = "What helps developers build LLM applications easily?"

results = retriever.invoke(query)

# Print the retrieved documents
for i, doc in enumerate(results):
    print(f"Document {i+1}: {doc.page_content}")