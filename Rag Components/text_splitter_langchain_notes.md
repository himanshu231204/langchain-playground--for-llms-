# ✂️ Text Splitter – LangChain Notes

> Notes on text splitting strategies for preparing documents for embedding and retrieval in RAG pipelines.

## Table of Contents

- [What is a Text Splitter?](#what-is-a-text-splitter)
- [Role in RAG Pipeline](#role-in-rag-pipeline)
- [Important Parameters](#important-parameters)
- [Types of Text Splitters](#types-of-text-splitters)
- [Chunk Overlap Concept](#chunk-overlap-concept)
- [Length-Based Splitting](#length-based-splitting)
- [Choosing Chunk Size](#choosing-chunk-size)

## Related Notes

- [Document Loaders (RAG Notes)](rag_notes.md)
- [Vector Store Notes](Vectors%20Stores/vector_store_notes.md)
- [Chroma DB Notes](Vectors%20Stores/chroma_db_notes.md)
- [Retriever Notes](Retrievers/retriver.md)

---

## What is a Text Splitter?

A **Text Splitter** breaks large documents into smaller **chunks** before sending them to embeddings or the LLM.

**Why it's needed:**

- LLMs have **token limits** — large documents don't fit in one call
- **Better embedding quality** — smaller chunks embed more precisely
- **Better retrieval in RAG** — targeted chunks improve relevance
- **Prevent context loss** — overlapping ensures no information is cut off

---

## Role in RAG Pipeline

```
Raw Docs → Text Splitter → Chunks → Embeddings → Vector DB → Retriever → LLM
```

> **Core idea:** Better chunking → Better retrieval → Better RAG performance

---

## Important Parameters

| Parameter | Description |
|-----------|-------------|
| `chunk_size` | Maximum size of each chunk (characters or tokens) |
| `chunk_overlap` | Amount of text repeated between adjacent chunks |
| `separator` | Symbol or pattern used for splitting |

---

## Types of Text Splitters

### A) CharacterTextSplitter

Splits based on **character count**. Simple and basic — may cut sentences randomly.

```python
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = splitter.split_documents(documents)
```

**Best for:** Small or simple text

---

### B) RecursiveCharacterTextSplitter ⭐ (Most Recommended)

Splits **hierarchically**, trying separators in order: `"\n\n"` → `"\n"` → `" "` → `""`. Maintains semantic meaning better.

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = splitter.split_documents(documents)
```

**Best for:** RAG systems, general-purpose chunking

---

### C) TokenTextSplitter

Splits based on **token count** (not characters). Good when strict token limits are required.

```python
from langchain.text_splitter import TokenTextSplitter

splitter = TokenTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
```

**Best for:** OpenAI or token-based models

---

### D) MarkdownHeaderTextSplitter

Splits using **markdown headers**, keeping document structure intact.

```python
from langchain.text_splitter import MarkdownHeaderTextSplitter

headers_to_split_on = [
    ("#", "Header 1"),
    ("##", "Header 2"),
]
splitter = MarkdownHeaderTextSplitter(headers_to_split_on=headers_to_split_on)
```

**Best for:** README files, technical documentation

---

### Splitter Comparison

| Splitter | Basis | Preserves Meaning | Use Case |
|----------|-------|-------------------|---------|
| `CharacterTextSplitter` | Characters | ❌ | Simple text |
| `RecursiveCharacterTextSplitter` | Hierarchy | ✅ | RAG (recommended) |
| `TokenTextSplitter` | Tokens | ⚠️ | Token-limited models |
| `MarkdownHeaderTextSplitter` | Headers | ✅ | Structured docs |

---

## Chunk Overlap Concept

Chunk overlap prevents context from being cut off at chunk boundaries:

```
chunk_size = 500
chunk_overlap = 100

Chunk 1 → characters  0–500
Chunk 2 → characters  400–900   (100-char overlap with Chunk 1)
Chunk 3 → characters  800–1300  (100-char overlap with Chunk 2)
```

**Why overlap matters:**
- Prevents context break at boundaries
- Improves retrieval continuity
- Ensures related sentences stay accessible

---

## Length-Based Splitting

Length-based splitting splits text purely based on size (character count or token count), without considering meaning or structure.

### Character-Based

```python
from langchain.text_splitter import CharacterTextSplitter

splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=20,
    separator="\n"
)
```

| Advantage | Disadvantage |
|-----------|-------------|
| Simple to implement | Ignores semantic meaning |
| Easy to control size | May break sentences |
| Good for strict limits | Not ideal for structured docs |

### Token-Based

More accurate for LLM token limits, using the model's actual tokenizer.

---

## Choosing Chunk Size

| Model Size | Recommended Chunk Size |
|------------|----------------------|
| Small models | 300–500 tokens |
| Large models | 500–1000 tokens |

**General rule:** More overlap → Better retrieval, but more storage usage.

### Key Interview Points

- Chunking affects retrieval quality
- `RecursiveCharacterTextSplitter` is the most commonly used
- Overlap prevents information loss at chunk boundaries
- Token splitting is useful for models with strict context limits
