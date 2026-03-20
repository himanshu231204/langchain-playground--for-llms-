# 🔀 MultiQuery Retriever – Notes

> Notes on the MultiQuery Retriever — improves RAG recall by generating multiple query variations.

## Table of Contents

- [What is MultiQuery Retriever?](#what-is-multiquery-retriever)
- [Why Do We Need It?](#why-do-we-need-it)
- [How It Works](#how-it-works)
- [Internal Flow](#internal-flow)
- [Usage in LangChain](#usage-in-langchain)
- [Key Benefits and Drawbacks](#key-benefits-and-drawbacks)
- [MultiQuery vs MMR](#multiquery-vs-mmr)
- [When to Use MultiQuery](#when-to-use-multiquery)

## Related Notes

- [Retriever Notes](retriver.md)
- [MMR Retriever](mmr.md)
- [Contextual Compression Retriever](Contextual_Compression_Retriever_Notes.md)
- [Vector Store Notes](../Vectors%20Stores/vector_store_notes.md)
- [Chroma DB Notes](../Vectors%20Stores/chroma_db_notes.md)

---

## What is MultiQuery Retriever?

`MultiQueryRetriever` is an advanced retriever in LangChain that **generates multiple variations of a user query** using an LLM and retrieves documents for each variation.

It improves **recall** in RAG systems.

> **Interview definition:** MultiQueryRetriever improves retrieval performance by generating multiple semantically different queries from the original query using an LLM, and combining the retrieved results to improve recall.

---

## Why Do We Need It?

**Problem:** Vector search depends heavily on the exact wording of the query.

If document wording differs from the query, relevant documents may not be retrieved.

**Example:**

```
User query: "Benefits of LangChain"

But documents may contain:
  "Advantages of LangChain"
  "Why use LangChain?"
  "Features of LangChain"
```

A standard retriever may miss all three documents.

---

## How It Works

```
Step 1: Take original user query
Step 2: Use LLM to generate multiple rephrased queries
Step 3: Perform vector retrieval for each generated query
Step 4: Merge all results
Step 5: Remove duplicate documents
Step 6: Return combined unique results
```

---

## Internal Flow

```
User Query: "Benefits of LangChain"
    │
    ▼
LLM generates variations:
  → "Advantages of using LangChain"
  → "Why should I use LangChain?"
  → "What are LangChain's key features?"
    │
    ▼
Each query → Vector Search
    │
    ▼
Merge all results
    │
    ▼
Remove duplicate documents
    │
    ▼
Final retrieved documents (broader coverage)
```

---

## Usage in LangChain

```python
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

retriever = MultiQueryRetriever.from_llm(
    retriever=vectorstore.as_retriever(),
    llm=llm
)

docs = retriever.invoke("What are the benefits of LangChain?")
```

---

## Key Benefits and Drawbacks

### Benefits

- ✅ **Improves recall** — finds more relevant documents
- ✅ **Handles synonyms** and rephrasing
- ✅ **Better coverage** of knowledge base
- ✅ Works well when user queries are short or ambiguous

### Drawbacks

- ❌ **Extra LLM call** required → slower than normal retrieval
- ❌ **Slightly higher cost** (more LLM tokens used)
- ❌ Not needed for small, simple datasets

---

## MultiQuery vs MMR

| Feature | MMR | MultiQuery |
|---------|-----|------------|
| What it improves | **Diversity** of results | **Recall** (finding more) |
| How | Penalizes similar selected docs | Generates multiple query variations |
| Extra LLM call | ❌ | ✅ |
| Best when | Results are too similar | Query wording may not match docs |

---

## When to Use MultiQuery

Use MultiQuery when:

- ✅ Knowledge base is large and diverse
- ✅ User queries may use different terminology than documents
- ✅ Synonyms or rephrasing matters
- ✅ High recall is more important than low latency
- ✅ Short or ambiguous queries need expansion
