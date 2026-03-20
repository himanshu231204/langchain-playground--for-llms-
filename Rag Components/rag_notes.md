# 📚 RAG Components – Document Loaders

> Notes on Document Loaders — the entry point for data in LangChain RAG pipelines.

## Table of Contents

- [What is a Document Loader?](#what-is-a-document-loader)
- [What Does It Return?](#what-does-it-return)
- [Common Document Loaders](#common-document-loaders)
- [PDF Loader](#pdf-loader)
- [Directory Loader](#directory-loader)
- [Load vs Lazy Load](#load-vs-lazy-load)
- [WebBaseLoader](#webbaseloader)
- [RAG Pipeline Context](#rag-pipeline-context)

## Related Notes

- [Text Splitter Notes](text_splitter_langchain_notes.md)
- [Vector Store Notes](Vectors%20Stores/vector_store_notes.md)
- [Chroma DB Notes](Vectors%20Stores/chroma_db_notes.md)
- [Retriever Notes](Retrievers/retriver.md)
- [Sample Data](../sample_data.md)

---

## What is a Document Loader?

A **Document Loader** in LangChain is a component that **loads data from different sources and converts it into a standard `Document` format** that LangChain can process.

> 🔹 It is the **entry point of data** into your RAG pipeline.

Without a document loader → your LLM has nothing to read.

**Why we need it:**

LLMs cannot directly read PDFs, websites, YouTube videos, CSV files, or databases. Document Loaders:
1. Read the file/source
2. Extract text
3. Convert it into `Document` objects

---

## What Does It Return?

A list of **`Document` objects**, each containing:

```python
Document(
    page_content="Actual text here",
    metadata={"source": "file_name.pdf", "page": 0}
)
```

- ✅ `page_content` — the extracted text
- ✅ `metadata` — source info, page number, URL, etc.

---

## Common Document Loaders

### 1. PDF Loader

```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
documents = loader.load()
```

Returns one `Document` per page.

### 2. Text File Loader

```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader("notes.txt")
documents = loader.load()
```

### 3. CSV Loader

```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader("data.csv")
documents = loader.load()
```

### 4. Web Loader

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
documents = loader.load()
```

### 5. Directory Loader

```python
from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("./docs/")
documents = loader.load()
```

---

## PDF Loader

### Types of PDF Loaders

| Loader | Library | Best For |
|--------|---------|---------|
| `PyPDFLoader` | `pypdf` | Simple text-based PDFs (most common) |
| `UnstructuredPDFLoader` | `unstructured` | Complex layouts, tables |
| `PyMuPDFLoader` | `pymupdf` | Large PDFs, better metadata |
| `PDFMinerLoader` | `pdfminer` | Detailed text extraction, layout preservation |
| `OnlinePDFLoader` | — | PDFs hosted online via URL |

### Common Errors

- `FileNotFoundError` if path is wrong
- Scanned PDFs may not extract text (need OCR tools)
- Encoding issues may occur

---

## Directory Loader

Use `DirectoryLoader` to load **multiple files from a folder**:

```python
from langchain_community.document_loaders import DirectoryLoader, TextLoader

loader = DirectoryLoader(
    "data/",
    glob="*.txt",       # load only .txt files
    loader_cls=TextLoader
)

documents = loader.load()
```

**Why use it:** Instead of loading each file manually, loads all matching files at once. Essential for large document collections in RAG.

---

## Load vs Lazy Load

| Method | Behavior | Memory Usage | Use When |
|--------|----------|--------------|---------|
| `load()` | Loads entire file at once | Higher | Small files, simple use cases |
| `lazy_load()` | Loads content step by step | Lower | Large files, streaming, production |

### load() example

```python
loader = PyPDFLoader("sample.pdf")
documents = loader.load()  # returns list of Documents
```

### lazy_load() example

```python
loader = PyPDFLoader("sample.pdf")
for doc in loader.lazy_load():
    print(doc.page_content)  # one page at a time
```

**Interview Point:**
- `load()` returns a **list**
- `lazy_load()` returns an **iterator**
- Lazy loading improves performance for large datasets

---

## WebBaseLoader

Used to load data from websites:

```python
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
documents = loader.load()
```

**Extracts:** readable text from HTML pages (strips HTML, CSS, scripts).

**Use cases:**
- Build chatbot from blog content
- Load documentation websites
- Extract online research material
- Create Q&A systems from web articles

**Common issues:**
- ❌ Some websites block bots
- ❌ JavaScript-heavy sites may not load fully
- ❌ Internet connection required
- ❌ Dynamic content may not appear

---

## RAG Pipeline Context

```
Raw Data (PDF / Web / CSV / Directory)
        │
        ▼
Document Loader  ◄── You are here
        │
        ▼
Text Splitter     (see: text_splitter_langchain_notes.md)
        │
        ▼
Embedding Model
        │
        ▼
Vector DB         (see: Vectors Stores/chroma_db_notes.md)
        │
        ▼
Retriever         (see: Retrievers/retriver.md)
        │
        ▼
LLM
        │
        ▼
Final Answer
```

> **Interview definition:** A Document Loader in LangChain is a component that loads data from external sources and converts it into standardized `Document` objects containing text and metadata, which are then used in RAG pipelines for embedding and retrieval.
