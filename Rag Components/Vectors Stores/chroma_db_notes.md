============================================================
CHROMA DB – COMPLETE CONCEPT NOTES
============================================================

1. WHAT IS CHROMA DB?
------------------------------------------------------------
Chroma DB is an open-source vector database designed
specifically for AI applications and LLM-based systems.

It is commonly used with LangChain for building RAG systems.

In simple words:
Chroma = A lightweight vector database that stores embeddings
and allows fast semantic similarity search.

------------------------------------------------------------

2. WHY CHROMA WHEN ALL VECTOR STORES ARE SIMILAR?
------------------------------------------------------------
Yes, the core concept of all vector stores is similar:
- Store embeddings
- Perform similarity search

But Chroma is popular because:

- Very easy to use
- Works locally
- Supports persistence
- Tight integration with LangChain
- No complex setup required

It is beginner-friendly and great for projects.

------------------------------------------------------------

3. CORE COMPONENTS OF CHROMA
------------------------------------------------------------

1) Collection
   - Like a table in SQL
   - Stores documents + embeddings + metadata

2) Documents
   - Text chunks stored in DB

3) Embeddings
   - Numerical representation of documents

4) Metadata
   - Additional info like:
     source = "chapter1"
     author = "Himanshu"

5) IDs
   - Unique identifiers for documents

------------------------------------------------------------

4. INTERNAL WORKING OF CHROMA
------------------------------------------------------------

Step 1: Load documents
Step 2: Split into chunks
Step 3: Convert chunks into embeddings
Step 4: Store embeddings inside a collection
Step 5: Query converted to embedding
Step 6: Similarity search performed
Step 7: Top-K results returned

Chroma uses approximate nearest neighbor search internally.

------------------------------------------------------------

5. PERSISTENCE (VERY IMPORTANT FEATURE)
------------------------------------------------------------

Chroma allows storing the database on disk.

Example:

persist_directory = "./chroma_db"

This means:
Even if you restart your system,
your embeddings remain saved.

Without persistence → Data lost after program ends.

------------------------------------------------------------

6. SEARCH METHODS IN CHROMA
------------------------------------------------------------

1) similarity_search(query)
2) similarity_search_with_score(query)
3) max_marginal_relevance_search(query)

------------------------------------------------------------

7. STRUCTURE IN LANGCHAIN
------------------------------------------------------------

Basic Usage:

from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

To load existing DB:

vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=embeddings
)

------------------------------------------------------------

8. HOW CHROMA STORES DATA
------------------------------------------------------------

Internally stores:

- Embedding vectors
- Document text
- Metadata
- IDs

All grouped inside a collection.

------------------------------------------------------------

9. DIFFERENCE BETWEEN FAISS AND CHROMA
------------------------------------------------------------

FAISS:
- Fast
- Local
- No built-in metadata filtering
- No automatic persistence

Chroma:
- Easy to use
- Metadata filtering supported
- Persistence built-in
- More structured for RAG systems

------------------------------------------------------------

10. WHEN TO USE CHROMA?
------------------------------------------------------------

Use Chroma when:

- Building small to medium RAG system
- Working locally
- Need metadata filtering
- Need persistence
- Learning vector databases

Not ideal for:
- Massive production-scale systems
- Distributed cloud architectures

------------------------------------------------------------

11. MATHEMATICAL BASE
------------------------------------------------------------

Chroma uses embedding similarity.

Most common similarity measure:
Cosine Similarity

cos(theta) = (A . B) / (||A|| * ||B||)

Higher similarity → More relevant document

------------------------------------------------------------

12. INTERVIEW DEFINITION
------------------------------------------------------------

"Chroma DB is an open-source vector database used to store
document embeddings and perform semantic similarity search,
commonly used in RAG systems with LangChain."

------------------------------------------------------------

13. KEY TAKEAWAYS
------------------------------------------------------------

- Chroma is a vector database
- Designed for AI/LLM applications
- Stores embeddings + metadata
- Supports persistence
- Works smoothly with LangChain
- Ideal for beginner to intermediate RAG systems

============================================================
END OF NOTES
============================================================



