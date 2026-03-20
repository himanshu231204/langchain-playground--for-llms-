# 🔬 Chroma DB – Internal Architecture

> Deep dive into how Chroma DB stores, indexes, and retrieves vector embeddings internally.

## Table of Contents

- [Overview](#overview)
- [High-Level Architecture](#high-level-architecture)
- [Main Internal Layers](#main-internal-layers)
- [Query Execution Flow](#query-execution-flow)
- [Persistence Architecture](#persistence-architecture)
- [Memory Management](#memory-management)
- [Scalability Limits](#scalability-limits)
- [Mathematical Core](#mathematical-core)
- [Design Principles](#design-principles)
- [Internal Data Flow Summary](#internal-data-flow-summary)

## Related Notes

- [Chroma DB Notes](chroma_db_notes.md)
- [Vector Store Notes](vector_store_notes.md)
- [Vector DB Architecture Comparison](vector_db_architecture_comparison.md)
- [Retriever Notes](../Retrievers/retriver.md)

---

## Overview

Chroma is not just a simple vector store. Internally, it is a modular system that handles:

- Document storage
- Embedding storage
- Indexing
- Metadata filtering
- Persistence
- Query processing

It is optimized for LLM and RAG applications.

---

## High-Level Architecture

```
User Query
    │
    ▼
Embedding Function
    │
    ▼
Query Embedding Vector
    │
    ▼
     Chroma Collection
 ┌──────────────────────────┐
 │ 1. Vector Index          │
 │ 2. Metadata Store        │
 │ 3. Document Store        │
 │ 4. ID Mapping Layer      │
 └──────────────────────────┘
    │
    ▼
Similarity Search Engine
    │
    ▼
Top-K Results
    │
    ▼
LLM
```

---

## Main Internal Layers

### A) Collection Layer

A **Collection** is the core container. It holds:
- Embeddings
- Documents
- Metadata
- Unique IDs

Each collection works independently.

```python
collection_name = "ai_notes"
```

---

### B) Embedding Storage Layer

Stores high-dimensional vectors:

```
[0.123, -0.443, 0.991, ...]
```

Stored efficiently in memory and optionally on disk.

---

### C) Indexing Layer

Enables fast similarity search using **Approximate Nearest Neighbor (ANN)**.

**Why ANN?** Exact search in high-dimensional space is `O(n)`. ANN reduces this to approximately `O(log n)`.

Common indexing techniques:

| Technique | Description |
|-----------|-------------|
| **HNSW** (Hierarchical Navigable Small World Graph) | Graph-based, fast and accurate |
| **IVF** (Inverted File Index) | Cluster-based search |
| **Brute Force** | Used for small datasets |

> ANN trades slight accuracy for huge speed gain.

---

### D) Metadata Store

Chroma stores metadata separately from vectors.

```json
{
    "source": "chapter1",
    "author": "Himanshu"
}
```

**Metadata filtering happens BEFORE similarity ranking** — this improves precision significantly.

Example: Search only documents where `source="chapter1"`.

---

### E) Document Store

Stores the original text chunks. The vector index stores only embeddings, but final output requires the original text. Chroma maintains a document-text mapping internally.

---

### F) ID Mapping Layer

Each document has a unique ID that connects:

```
Embedding ↔ Metadata ↔ Original Text
```

Without ID mapping, the system cannot retrieve the correct document after a similarity search.

---

## Query Execution Flow

```
Step 1: User sends query
Step 2: Query converted into embedding
Step 3: Metadata filtering applied (if any)
Step 4: ANN index searches nearest vectors
Step 5: Top-K IDs selected
Step 6: Retrieve original text using ID mapping
Step 7: Return documents to user / LLM
```

---

## Persistence Architecture

When `persist_directory` is set, Chroma saves to disk:

- Embeddings
- Metadata
- Index structure
- Collection info

On restart: Chroma reloads everything from disk → **production-friendly**.

```python
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embeddings,
    persist_directory="./chroma_db"
)
```

---

## Memory Management

Chroma handles:

- **In-memory storage** for fast search
- **Disk-based storage** for persistence
- **Efficient batching** during large insertions

Large datasets require careful chunk sizing to stay within memory limits.

---

## Scalability Limits

| Use Case | Suitability |
|----------|-------------|
| Local development | ✅ Excellent |
| Medium-sized datasets | ✅ Good |
| Prototyping & RAG demos | ✅ Excellent |
| Very large distributed systems | ❌ Use Pinecone instead |

> See [Architecture Comparison](vector_db_architecture_comparison.md) for when to choose Pinecone.

---

## Mathematical Core

Chroma uses **Cosine Similarity**:

```
cos(θ) = (A · B) / (||A|| × ||B||)
```

High similarity → small angular distance.

ANN reduces search complexity:
- Exact search: `O(n)`
- ANN search: approximately `O(log n)`

---

## Design Principles

Chroma is built with:

- **Simplicity** — easy to use
- **Developer friendliness** — minimal setup
- **LLM-first architecture** — designed for RAG patterns
- **Metadata-aware search** — pre-filter before similarity
- **Persistence support** — production-ready

---

## Internal Data Flow Summary

### Insert Flow

```
Document
    │
    ▼
Text Splitter
    │
    ▼
Embedding Function
    │
    ▼
Store in Collection
    │
    ▼
Index Updated
```

### Query Flow

```
Query
    │
    ▼
Embedding
    │
    ▼
Metadata Filter
    │
    ▼
ANN Search
    │
    ▼
Retrieve Original Text
    │
    ▼
Return Top-K
```

---

> **Interview summary:** Internally, Chroma consists of a collection layer, embedding storage, ANN-based indexing, metadata store, and ID mapping system. It performs filtered semantic similarity search and supports persistence for RAG systems.

**Key understanding:**

- **Collection** is the core container
- **ANN indexing** enables fast search
- **Metadata filtering** improves precision
- **ID mapping** connects embeddings to original text
- **Persistence** allows production usage
