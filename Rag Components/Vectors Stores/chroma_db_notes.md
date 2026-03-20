# 🟣 Chroma DB – Notes

> Notes on Chroma DB — the lightweight, developer-friendly vector database for LangChain RAG systems.

## Table of Contents

- [What is Chroma DB?](#what-is-chroma-db)
- [Why Chroma?](#why-chroma)
- [Core Components](#core-components)
- [How Chroma Works](#how-chroma-works)
- [Persistence](#persistence)
- [Search Methods](#search-methods)
- [Using Chroma with LangChain](#using-chroma-with-langchain)
- [When to Use Chroma](#when-to-use-chroma)
- [Chroma vs FAISS](#chroma-vs-faiss)

## Related Notes

- [Vector Store Notes](vector_store_notes.md)
- [Chroma Internal Architecture](chroma_internal_architecture.md)
- [Vector DB Architecture Comparison](vector_db_architecture_comparison.md)
- [Retriever Notes](../Retrievers/retriver.md)
- [Text Splitter Notes](../text_splitter_langchain_notes.md)

---

## What is Chroma DB?

**Chroma DB** is an open-source vector database designed specifically for AI applications and LLM-based systems. It is commonly used with LangChain for building RAG systems.

> **Simple definition:** Chroma = A lightweight vector database that stores embeddings and allows fast semantic similarity search.

---

## Why Chroma?

While all vector stores share the same core concept (store embeddings + similarity search), Chroma is popular because:

- ✅ Very easy to use
- ✅ Works locally (no cloud required)
- ✅ Supports persistence to disk
- ✅ Tight integration with LangChain
- ✅ No complex setup required
- ✅ Beginner-friendly

---

## Core Components

| Component | Description |
|-----------|-------------|
| **Collection** | Like a table in SQL — stores documents + embeddings + metadata |
| **Documents** | Text chunks stored in the DB |
| **Embeddings** | Numerical representations of documents |
| **Metadata** | Additional info like `source`, `author`, `chapter` |
| **IDs** | Unique identifiers for each document |

---

## How Chroma Works

```
Step 1: Load documents
Step 2: Split into chunks
Step 3: Convert chunks to embeddings
Step 4: Store embeddings in a collection
Step 5: Convert query to embedding
Step 6: Similarity search
Step 7: Return Top-K results
```

Chroma uses **Approximate Nearest Neighbor (ANN)** search internally.

> For deep architecture details, see [Chroma Internal Architecture](chroma_internal_architecture.md).

---

## Persistence

A key Chroma feature — store the database on disk so data survives restarts:

```python
persist_directory = "./chroma_db"
```

- **Without persistence** → data lost after program ends
- **With persistence** → embeddings, metadata, and index saved to disk

---

## Search Methods

```python
# Basic similarity search
vectorstore.similarity_search("your query", k=4)

# With relevance scores
vectorstore.similarity_search_with_score("your query", k=4)

# Max Marginal Relevance (diversity + relevance)
vectorstore.max_marginal_relevance_search("your query", k=4)
```

> See [MMR Notes](../Retrievers/mmr.md) for details on `max_marginal_relevance_search`.

---

## Using Chroma with LangChain

### Create a new vector store

```python
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=OpenAIEmbeddings(),
    persist_directory="./chroma_db"
)
```

### Load an existing vector store

```python
vectorstore = Chroma(
    persist_directory="./chroma_db",
    embedding_function=OpenAIEmbeddings()
)
```

### Use as a retriever

```python
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
docs = retriever.invoke("What is RAG?")
```

---

## When to Use Chroma

**Use Chroma when:**

- Building small to medium RAG systems
- Working locally
- Need metadata filtering
- Need persistence
- Learning vector databases

**Not ideal for:**

- Massive production-scale distributed systems
- Multi-node cloud architectures

---

## Chroma vs FAISS

| Feature | Chroma | FAISS |
|---------|--------|-------|
| Type | Full vector DB | Similarity search library |
| Metadata filtering | ✅ Built-in | ❌ Manual |
| Persistence | ✅ Built-in | ❌ Manual |
| Ease of use | Easy | Requires more setup |
| LangChain integration | ✅ Native | ✅ Native |
| Best for | RAG development | Custom high-speed systems |

> See [Architecture Comparison](vector_db_architecture_comparison.md) for full FAISS vs Chroma vs Pinecone comparison.

---

## Mathematical Foundation

Chroma uses **Cosine Similarity**:

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

Higher similarity → more relevant document.

> **Interview definition:** Chroma DB is an open-source vector database used to store document embeddings and perform semantic similarity search, commonly used in RAG systems with LangChain.
