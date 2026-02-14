from langchain_experimental.text_splitter import SemanticChunker
from langchain_ollama import OllamaEmbeddings


# 1️⃣ Use Updated Ollama Embedding Model
embeddings = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe"
)

# 2️⃣ Create Semantic Chunker
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season. The sun was bright, and the air smelled of earth and fresh grass. The Indian Premier League (IPL) is the biggest cricket league in the world. People all over the world watch the matches and cheer for their favourite teams.

Terrorism is a big danger to peace and safety. It causes harm to people and creates fear in cities and villages. When such attacks happen, they leave behind pain and sadness. To fight terrorism, we need strong laws, alert security forces, and support from people who care about peace and safety.
"""

# 3️⃣ Create Semantic Chunks
docs = text_splitter.create_documents([sample])

# 4️⃣ Print Results
print("Total Chunks:", len(docs))
print("\n--- Semantic Chunks ---\n")

for i, doc in enumerate(docs):
    print(f"Chunk {i+1}:\n{doc.page_content}")
    print("-" * 60)
