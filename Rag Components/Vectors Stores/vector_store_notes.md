============================================================
VECTOR STORES IN LANGCHAIN – COMPLETE NOTES
============================================================

1. WHAT IS A VECTOR STORE?
------------------------------------------------------------
A Vector Store is a special database that stores text in the
form of numerical vectors (embeddings) and allows similarity
search instead of exact keyword matching.

In simple words:
Vector Store = Embedding Database + Similarity Search Engine

It is mainly used in RAG (Retrieval-Augmented Generation).

------------------------------------------------------------

2. WHY DO WE NEED VECTOR STORES?
------------------------------------------------------------
Normal databases:
- Work on exact match
- Use SQL queries
- Cannot understand meaning

Vector databases:
- Understand semantic meaning
- Perform similarity search
- Return most relevant documents

Example:
Query: "Future of AI"
Document: "Artificial Intelligence will transform industries"
Vector search will match this.
Keyword search may not.

------------------------------------------------------------

3. WHAT IS AN EMBEDDING?
------------------------------------------------------------
Embedding = Numerical representation of text.

Example:
"Machine learning is powerful"

becomes

[0.245, -0.556, 0.991, 0.112, ...]

These numbers represent meaning in high-dimensional space
(e.g., 768 or 1536 dimensions).

Similar meaning → Vectors close together
Different meaning → Vectors far apart

------------------------------------------------------------

4. VECTOR STORE IN RAG PIPELINE
------------------------------------------------------------

User Query
    ↓
Embedding Model
    ↓
Vector Store (Similarity Search)
    ↓
Top-K Relevant Chunks
    ↓
LLM
    ↓
Final Answer

Vector Store acts as long-term memory for LLM.

------------------------------------------------------------

5. CORE COMPONENTS
------------------------------------------------------------

1) Documents
   - Text chunks
   - Usually split using a Text Splitter

2) Embeddings
   - Created using embedding models
   - Example: OpenAI Embeddings

3) Index
   - Efficient structure for fast similarity search
   - Example: HNSW, IVF

------------------------------------------------------------

6. SIMILARITY MEASURE
------------------------------------------------------------

Most common: Cosine Similarity

Formula:

cos(theta) = (A . B) / (||A|| * ||B||)

Range:
1  → Very similar
0  → No relation
-1 → Opposite meaning

Higher cosine similarity = More similar meaning.

------------------------------------------------------------

7. TYPES OF SEARCH
------------------------------------------------------------

1) Similarity Search
2) Similarity Search with Score
3) Max Marginal Relevance (MMR)
4) Hybrid Search (Keyword + Vector)

------------------------------------------------------------

8. POPULAR VECTOR STORES IN LANGCHAIN
------------------------------------------------------------

1) FAISS
   - Local
   - Fast
   - Lightweight

2) Chroma
   - Local
   - Supports persistence
   - Easy to use

3) Pinecone
   - Cloud-based
   - Scalable

4) Weaviate
   - Cloud / Open-source

5) Milvus
   - Large-scale production use

------------------------------------------------------------

9. HOW IT WORKS INTERNALLY
------------------------------------------------------------

Step 1: Load documents
Step 2: Split into chunks
Step 3: Convert each chunk to embedding
Step 4: Store embeddings in vector store
Step 5: Convert query into embedding
Step 6: Perform similarity search
Step 7: Retrieve Top-K closest vectors
Step 8: Send retrieved context to LLM

------------------------------------------------------------

10. IMPORTANT PARAMETERS
------------------------------------------------------------

Top-K:
- Number of similar documents to retrieve

Metadata Filtering:
- Filter documents based on metadata
- Example: source="chapter1"

Persistence:
- Save vector database to disk

------------------------------------------------------------

11. ADVANCED CONCEPTS
------------------------------------------------------------

1) Approximate Nearest Neighbor (ANN)
2) HNSW Indexing
3) IVF Indexing
4) Quantization
5) Sharding
6) Re-ranking

These improve performance for large datasets.

------------------------------------------------------------

12. INTERVIEW DEFINITION
------------------------------------------------------------

"A Vector Store is a database that stores high-dimensional
embeddings of documents and enables efficient similarity
search for retrieval-based LLM applications such as RAG."

------------------------------------------------------------

13. KEY TAKEAWAYS
------------------------------------------------------------

- Vector Store stores embeddings
- Enables semantic search
- Core component of RAG
- Uses cosine similarity or ANN
- Returns Top-K relevant chunks
- Helps LLM generate contextual answers

============================================================
END OF NOTES
============================================================
