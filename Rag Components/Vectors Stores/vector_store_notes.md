# 🗄️ Vector Stores in LangChain – Notes

> Comprehensive notes on vector stores — the semantic search databases powering RAG systems.

## Table of Contents

- [What is a Vector Store?](#what-is-a-vector-store)
- [Why Do We Need Vector Stores?](#why-do-we-need-vector-stores)
- [What is an Embedding?](#what-is-an-embedding)
- [Vector Store in RAG Pipeline](#vector-store-in-rag-pipeline)
- [Core Components](#core-components)
- [Similarity Measure](#similarity-measure)
- [Types of Search](#types-of-search)
- [Popular Vector Stores in LangChain](#popular-vector-stores-in-langchain)
- [How It Works Internally](#how-it-works-internally)
- [Advanced Concepts](#advanced-concepts)

## Related Notes

- [Chroma DB Notes](chroma_db_notes.md)
- [Chroma Internal Architecture](chroma_internal_architecture.md)
- [Vector DB Architecture Comparison](vector_db_architecture_comparison.md)
- [Document Loaders (RAG)](../rag_notes.md)
- [Text Splitter Notes](../text_splitter_langchain_notes.md)
- [Retriever Notes](../Retrievers/retriver.md)

---

## What is a Vector Store?

A **Vector Store** is a special database that stores text in the form of **numerical vectors (embeddings)** and allows **similarity search** instead of exact keyword matching.

> **Vector Store = Embedding Database + Similarity Search Engine**

Mainly used in **RAG (Retrieval-Augmented Generation)**.

---

## Why Do We Need Vector Stores?

| Normal Database | Vector Database |
|----------------|----------------|
| Works on exact match | Understands semantic meaning |
| Uses SQL queries | Performs similarity search |
| Cannot understand meaning | Returns most relevant documents |

**Example:**
- Query: `"Future of AI"`
- Document: `"Artificial Intelligence will transform industries"`

→ **Vector search** finds the match  
→ **Keyword search** may miss it

---

## What is an Embedding?

An **embedding** is the numerical representation of text in high-dimensional space.

```
"Machine learning is powerful"
→ [0.245, -0.556, 0.991, 0.112, ...]  (768 or 1536 dimensions)
```

- **Similar meaning** → vectors close together
- **Different meaning** → vectors far apart

---

## Vector Store in RAG Pipeline

```
User Query
    │
    ▼
Embedding Model
    │
    ▼
Vector Store (Similarity Search)  ◄── You are here
    │
    ▼
Top-K Relevant Chunks
    │
    ▼
LLM
    │
    ▼
Final Answer
```

> Vector Store acts as **long-term memory** for the LLM.

---

## Core Components

| Component | Description |
|-----------|-------------|
| Documents | Text chunks (usually split with a [Text Splitter](../text_splitter_langchain_notes.md)) |
| Embeddings | Numerical vectors created by embedding models |
| Index | Efficient structure for fast similarity search (e.g., HNSW, IVF) |

---

## Similarity Measure

Most common: **Cosine Similarity**

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

| Value | Meaning |
|-------|---------|
| `1` | Very similar (same direction) |
| `0` | No relation |
| `-1` | Opposite meaning |

Higher cosine similarity = More similar meaning.

---

## Types of Search

| Search Type | Description |
|-------------|-------------|
| Similarity Search | Find top-K most similar documents |
| Similarity Search with Score | Same, but returns similarity scores |
| Max Marginal Relevance (MMR) | Balances relevance and diversity |
| Hybrid Search | Combines keyword + vector search |

> See [MMR Notes](../Retrievers/mmr.md) for details on Max Marginal Relevance.

---

## Popular Vector Stores in LangChain

| Store | Type | Best For |
|-------|------|---------|
| **FAISS** | Local library | Fast local search, custom systems |
| **Chroma** | Local DB | RAG development, easy setup |
| **Pinecone** | Cloud managed | Production, scalability |
| **Weaviate** | Cloud / Open-source | Advanced filtering |
| **Milvus** | Large-scale | Production, distributed |

> See [Architecture Comparison](vector_db_architecture_comparison.md) for FAISS vs Chroma vs Pinecone.

---

## How It Works Internally

```
Step 1: Load documents
Step 2: Split into chunks  (Text Splitter)
Step 3: Convert each chunk to embedding
Step 4: Store embeddings in vector store
Step 5: Convert query into embedding
Step 6: Perform similarity search
Step 7: Retrieve Top-K closest vectors
Step 8: Send retrieved context to LLM
```

---

## Advanced Concepts

| Concept | Description |
|---------|-------------|
| **ANN (Approximate Nearest Neighbor)** | Faster search by trading slight accuracy for speed |
| **HNSW** | Graph-based indexing for fast search |
| **IVF** | Inverted file index for large datasets |
| **Quantization** | Compress vectors to reduce storage |
| **Sharding** | Distribute data across nodes |
| **Re-ranking** | Post-search refinement for better relevance |

---

## Key Takeaways

- Vector Store stores **embeddings**
- Enables **semantic search** (meaning-based, not keyword-based)
- Core component of **RAG pipelines**
- Uses cosine similarity or ANN algorithms
- Returns **Top-K relevant chunks** for the LLM
- Helps LLM generate **contextually grounded** answers

> **Interview definition:** A Vector Store is a database that stores high-dimensional embeddings of documents and enables efficient similarity search for retrieval-based LLM applications such as RAG.
