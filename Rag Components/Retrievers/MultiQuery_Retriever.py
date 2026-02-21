from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Embedding model
embeddings_model = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe:latest"
)

# LLM
llm = ChatOllama(model="mistral")

# Sample documents
all_docs = [
    Document(page_content="Regular walking boosts heart health and can reduce symptoms of depression."),
    Document(page_content="Consuming leafy greens and fruits helps detox the body and improve longevity."),
    Document(page_content="Deep sleep is crucial for cellular repair and emotional regulation."),
    Document(page_content="Mindfulness and controlled breathing lower cortisol and improve mental clarity."),
    Document(page_content="Drinking sufficient water throughout the day helps maintain metabolism and energy."),
    Document(page_content="Python balances readability with power."),
]

# Create vector store
vector_store = FAISS.from_documents(
    documents=all_docs,
    embedding=embeddings_model
)

retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 🔥 Multi Query Prompt
prompt = ChatPromptTemplate.from_template(
    """You are an AI assistant.
Generate 3 different rephrased versions of the user question.
Return each question on a new line.

Original Question: {question}"""
)

# Chain to generate multiple queries
query_chain = prompt | llm | StrOutputParser()

# Original user query
query = "What are the benefits of regular walking and leafy greens for health?"

# Generate multiple queries
generated_queries = query_chain.invoke({"question": query})

# Split into list
query_list = generated_queries.split("\n")

# Collect results
all_results = []
for q in query_list:
    docs = retriever.invoke(q)
    all_results.extend(docs)

# Remove duplicates
unique_docs = list({doc.page_content: doc for doc in all_results}.values())

# Print results
for i, doc in enumerate(unique_docs):
    print(f"\nDocument {i+1}:")
    print(doc.page_content)