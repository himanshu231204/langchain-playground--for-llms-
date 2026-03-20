# 🗜️ Contextual Compression Retriever – Notes

> Notes on the Contextual Compression Retriever — improves RAG precision by filtering out irrelevant content before passing documents to the LLM.

## Table of Contents

- [What is Contextual Compression Retriever?](#what-is-contextual-compression-retriever)
- [Why Do We Need It?](#why-do-we-need-it)
- [How It Works](#how-it-works)
- [Internal Flow](#internal-flow)
- [Key Components](#key-components)
- [Usage in LangChain](#usage-in-langchain)
- [Example](#example)
- [Benefits and Drawbacks](#benefits-and-drawbacks)
- [Comparison with Other Retrievers](#comparison-with-other-retrievers)
- [When to Use It](#when-to-use-it)

## Related Notes

- [Retriever Notes](retriver.md)
- [MMR Retriever](mmr.md)
- [MultiQuery Retriever](MultiQuery_Retriever_Notes.md)
- [Vector Store Notes](../Vectors%20Stores/vector_store_notes.md)
- [Chroma DB Notes](../Vectors%20Stores/chroma_db_notes.md)

---

## What is Contextual Compression Retriever?

`ContextualCompressionRetriever` is an advanced retriever that **compresses retrieved documents using an LLM** and keeps only the parts relevant to the user query.

It improves **precision** in RAG systems.

> **Interview definition:** Contextual Compression Retriever enhances RAG systems by compressing retrieved documents using an LLM to retain only query-relevant content before passing it to the final language model.

---

## Why Do We Need It?

**Problem with normal retrieval:**

- Retrieved documents may be **long**
- They contain **irrelevant information**
- The **context window gets wasted** on noise
- Response quality may decrease

**Solution:** Compress documents before sending to the final LLM.

---

## How It Works

```
Step 1: Retrieve top-K documents using base retriever
Step 2: Pass each document to an LLM compressor
Step 3: LLM extracts only query-relevant sentences
Step 4: Return compressed, focused documents to the LLM
```

---

## Internal Flow

```
User Query
    │
    ▼
Base Retriever (Vector Search → Top-K Docs)
    │
    ▼
LLM-based Compressor
    │
    ▼
Filtered / Compressed Documents
    │
    ▼
Final LLM → Answer
```

---

## Key Components

| Component | Role |
|-----------|------|
| **Base Retriever** | FAISS / Chroma / Pinecone — retrieves top-K raw documents |
| **Compressor** | LLM-based extractor — filters out irrelevant content |
| `ContextualCompressionRetriever` | Combines base retriever + compressor |

---

## Usage in LangChain

```python
from langchain.retrievers import ContextualCompressionRetriever
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

# Create the compressor
compressor = LLMChainExtractor.from_llm(llm)

# Wrap your base retriever
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=vectorstore.as_retriever()
)

docs = compression_retriever.invoke("What are the health benefits of walking?")
```

---

## Example

**Original retrieved document:**

```text
"Walking improves heart health.
Walking shoes are important for comfort.
It reduces stress and anxiety.
Many people walk in parks during weekends."
```

**Query:** `"What are the health benefits of walking?"`

**Compressed output:**

```text
"Walking improves heart health and reduces stress."
```

The irrelevant sentences about shoes and parks are removed.

---

## Benefits and Drawbacks

### Benefits

- ✅ **Reduces token usage** — sends only relevant content to LLM
- ✅ **Removes irrelevant information** — cleaner context
- ✅ **Improves answer precision** — LLM focuses on what matters
- ✅ **Better for long documents**
- ✅ **Production-ready technique**

### Drawbacks

- ❌ **Extra LLM call** — slower than basic retrieval
- ❌ **Slightly higher cost**
- ❌ Not necessary for short, focused documents

---

## Comparison with Other Retrievers

| Retriever | What it improves | Mechanism |
|-----------|-----------------|-----------|
| **MMR** | Diversity of results | Penalizes similar docs |
| **MultiQuery** | Recall (finding more) | Generates multiple query variants |
| **Contextual Compression** | Precision (removing noise) | LLM compresses each retrieved doc |

---

## When to Use It

Use Contextual Compression when:

- ✅ Retrieved documents are **long**
- ✅ Context window is **limited**
- ✅ **High precision** is required
- ✅ Building a **production RAG system**
- ✅ Documents contain lots of noise around relevant answers
