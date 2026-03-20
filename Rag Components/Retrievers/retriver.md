# 🔎 Retrievers in LangChain – Notes

> Comprehensive notes on retrievers — the search component in RAG pipelines.

## Table of Contents

- [What is a Retriever?](#what-is-a-retriever)
- [How Retriever Works](#how-retriever-works)
- [Types of Retrievers](#types-of-retrievers)
- [Important Parameters](#important-parameters)
- [Retriever vs Vector Store](#retriever-vs-vector-store)
- [Retriever in LCEL](#retriever-in-lcel)
- [Why Retrievers Are Important](#why-retrievers-are-important)
- [Common Interview Questions](#common-interview-questions)

## Related Notes

- [MMR Retriever](mmr.md)
- [MultiQuery Retriever](MultiQuery_Retriever_Notes.md)
- [Contextual Compression Retriever](Contextual_Compression_Retriever_Notes.md)
- [Vector Store Notes](../Vectors%20Stores/vector_store_notes.md)
- [Chroma DB Notes](../Vectors%20Stores/chroma_db_notes.md)
- [Document Loaders (RAG)](../rag_notes.md)
- [Text Splitter Notes](../text_splitter_langchain_notes.md)

---

## What is a Retriever?

A **Retriever** in LangChain is a component that:

1. Takes a user query
2. Searches the knowledge base (vector store/documents)
3. Returns the most relevant documents

> ⚠️ **Important:** Retriever does NOT generate answers. It only retrieves relevant information.
>
> **Retriever = Search Engine** | **LLM = Answer Generator**

---

## How Retriever Works

### Step by Step

```
Step 1: Convert query to embedding
        Query text → Embedding Model → Query vector

Step 2: Similarity search
        Query vector compared to stored document vectors

Step 3: Return Top-K documents
        Most similar documents returned (e.g., top 3 or 5)
```

### Similarity Formula (Cosine Similarity)

```
similarity(A, B) = (A · B) / (||A|| × ||B||)
```

Higher value → more similar documents.

### RAG Flow

```
User Query
    │
    ▼
Embedding Model
    │
    ▼
Retriever (Vector Search)  ◄── You are here
    │
    ▼
Top-K Documents
    │
    ▼
LLM
    │
    ▼
Final Answer
```

---

## Types of Retrievers

### 1. Vector Store Retriever (Most Common)

Basic cosine similarity search over embedded documents.

```python
# Default retriever (k=4)
retriever = vectorstore.as_retriever()

# Custom k value
retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Retrieve documents
docs = retriever.invoke("What is RAG?")
```

---

### 2. MMR Retriever (Max Marginal Relevance)

Balances **relevance** and **diversity** in retrieved results. Reduces duplicate similar chunks.

```python
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={"k": 5}
)
```

> See [MMR Notes](mmr.md) for full details.

---

### 3. MultiQuery Retriever

Uses an LLM to generate **multiple variations** of the query, improving recall.

```
Original: "What is RAG?"
Generated:
  → "Explain Retrieval Augmented Generation"
  → "How does RAG work?"
  → "Architecture of RAG systems"
```

> See [MultiQuery Retriever Notes](MultiQuery_Retriever_Notes.md) for full details.

---

### 4. Contextual Compression Retriever

Compresses retrieved documents using an LLM to return only the query-relevant parts.

> See [Contextual Compression Retriever Notes](Contextual_Compression_Retriever_Notes.md) for full details.

---

### 5. Self Query Retriever

Converts natural language into **structured metadata filters**.

```
Query: "Show research papers after 2022 about LLM"
→ Applies: year > 2022 AND topic = "LLM"
→ Then performs similarity search on filtered set
```

---

### 6. Time-Weighted Retriever

Gives higher priority to **recent documents**. Useful for chat memory systems.

---

### Retriever Type Comparison

| Retriever | Purpose | Extra LLM Call? |
|-----------|---------|----------------|
| Vector Store | Basic similarity | ❌ |
| MMR | Relevance + diversity | ❌ |
| MultiQuery | Improve recall | ✅ |
| Contextual Compression | Improve precision | ✅ |
| Self Query | Metadata filtering | ✅ |
| Time-Weighted | Recent docs priority | ❌ |

---

## Important Parameters

| Parameter | Description | Example |
|-----------|-------------|---------|
| `k` | Number of documents to retrieve | `search_kwargs={"k": 5}` |
| `search_type` | Algorithm: `"similarity"` or `"mmr"` | `search_type="mmr"` |

**MMR** should be used when:
- Retrieved results are too similar to each other
- You need more diverse coverage

---

## Retriever vs Vector Store

| | Vector Store | Retriever |
|-|-------------|-----------|
| Role | Database layer | Interface layer |
| What it stores | Embeddings | — |
| What it does | Stores and organizes | Searches and returns |
| Examples | FAISS, Chroma | `as_retriever()`, MMR, MultiQuery |
| Relationship | — | Wrapper over vector store |

> **Retriever = Abstraction layer over a Vector Store**

---

## Retriever in LCEL

In modern LangChain, retrievers integrate directly into chains:

```python
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke("What is RAG?")
```

> See [Runnables (LCEL)](../../Runnables/Runnables.md) for more on building chains.

---

## Why Retrievers Are Important

| Without Retriever | With Retriever |
|-------------------|---------------|
| LLM guesses | LLM gives grounded answers |
| Limited to training data | Access to external knowledge |
| Higher hallucination risk | Reduced hallucination |
| Domain-agnostic | Domain-specific intelligence |

---

## Common Interview Questions

**Q1: What is a Retriever?**  
A: A component that fetches relevant documents based on semantic similarity.

**Q2: How does Retriever reduce hallucination?**  
A: It provides external context to the LLM, grounding responses in actual documents.

**Q3: What similarity metric is used?**  
A: Cosine similarity, dot product, or Euclidean distance.

**Q4: What is MMR?**  
A: Max Marginal Relevance — balances relevance and diversity in retrieved documents.

**Q5: Difference between MultiQuery and SelfQuery?**  
A: MultiQuery generates multiple semantic queries to improve recall. SelfQuery applies metadata filtering for more precise retrieval.

**Q6: Where is Retriever used?**  
A: In RAG (Retrieval-Augmented Generation) systems.

---

> **Interview definition:** A Retriever in LangChain is a component that performs semantic search over embedded documents and returns the most relevant chunks to the LLM for grounded answer generation.
