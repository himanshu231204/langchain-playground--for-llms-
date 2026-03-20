# 🎯 MMR – Maximal Marginal Relevance

> Notes on the MMR retrieval strategy — balancing relevance and diversity in retrieved documents.

## Table of Contents

- [What is MMR?](#what-is-mmr)
- [Problem with Normal Similarity Search](#problem-with-normal-similarity-search)
- [How MMR Works](#how-mmr-works)
- [MMR Score Formula](#mmr-score-formula)
- [Why MMR is Important in RAG](#why-mmr-is-important-in-rag)
- [Using MMR in LangChain](#using-mmr-in-langchain)
- [When to Use MMR](#when-to-use-mmr)

## Related Notes

- [Retriever Notes](retriver.md)
- [MultiQuery Retriever](MultiQuery_Retriever_Notes.md)
- [Contextual Compression Retriever](Contextual_Compression_Retriever_Notes.md)
- [Chroma DB Notes](../Vectors%20Stores/chroma_db_notes.md)
- [Vector Store Notes](../Vectors%20Stores/vector_store_notes.md)

---

## What is MMR?

**MMR = Maximal Marginal Relevance**

A retrieval technique that returns documents which are both:
- **Relevant** to the query
- **Diverse** from each other

---

## Problem with Normal Similarity Search

Standard similarity search finds the top-K most similar documents using cosine similarity.

**Problem:** The top results may be very similar to each other, causing:
- Repetitive context in the LLM prompt
- Wasted context window tokens
- Reduced answer quality (LLM sees the same info multiple times)

---

## How MMR Works

MMR balances two objectives:

1. **Relevance** to the original query
2. **Diversity** among already-selected documents

It selects documents **iteratively**:
- Each new document must be relevant to the query **AND** different from documents already selected

---

## MMR Score Formula

```
MMR Score = λ × (Similarity to Query) - (1 - λ) × (Max Similarity to Already Selected Docs)
```

| λ value | Effect |
|---------|--------|
| `λ = 1` | Pure similarity search (same as normal) |
| `λ = 0` | Maximum diversity only |
| `λ = 0.5` | Balanced relevance + diversity |

The `lambda_mult` parameter in LangChain corresponds to λ.

---

## Why MMR is Important in RAG

In RAG systems:

| Problem | MMR Solution |
|---------|-------------|
| Retrieved chunks too similar | Diversifies results |
| Context window wasted on duplicates | Reduces redundancy |
| LLM sees same info multiple times | Ensures broader topic coverage |
| Lower answer quality | Improves LLM responses |

---

## Using MMR in LangChain

```python
# Basic MMR retriever
retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,           # number of final documents
        "lambda_mult": 0.5  # diversity vs relevance balance
    }
)

docs = retriever.invoke("What are the benefits of RAG?")
```

### With Chroma directly

```python
docs = vectorstore.max_marginal_relevance_search(
    query="What are the benefits of RAG?",
    k=4,
    lambda_mult=0.5
)
```

---

## When to Use MMR

Use MMR when:

- ✅ Your documents have many similar chunks (e.g., long repetitive text)
- ✅ You want broader topic coverage in responses
- ✅ Normal similarity search returns redundant results
- ✅ Building production RAG applications

---

## MMR vs Other Retrievers

| Retriever | What it improves | How |
|-----------|-----------------|-----|
| MMR | **Diversity** of results | Penalizes similar documents |
| MultiQuery | **Recall** (finding more) | Generates multiple query variants |
| Contextual Compression | **Precision** (removing noise) | LLM compresses documents |

---

> **Quick interview answer:** MMR improves retrieval quality by balancing relevance and diversity, reducing redundancy in retrieved documents for better LLM output.
