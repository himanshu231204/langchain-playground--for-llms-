## 📄 What is a **Document Loader** in LangChain?

A **Document Loader** in LangChain is a component that **loads data from different sources and converts it into a standard Document format** that LangChain can process.

In simple words:

> 🔹 It is the **entry point of data** into your RAG pipeline.

Without a document loader → your LLM has nothing to read.

---

## 🔹 Why Do We Need It?

LLMs cannot directly read:

* PDFs
* Websites
* YouTube videos
* CSV files
* Databases

So LangChain provides **Document Loaders** to:

1. Read the file/source
2. Extract text
3. Convert it into `Document` objects

---

## 🔹 What Does It Return?

It returns a list of **Document objects**.

Each Document contains:

```python
Document(
    page_content="Actual text here",
    metadata={"source": "file_name.pdf"}
)
```

So it gives:

* ✅ Text
* ✅ Metadata (source info, page number, etc.)

---

# 🔹 Common Document Loaders in LangChain

---

## 1️⃣ PDF Loader

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader("gate_notes.pdf")
documents = loader.load()
```

👉 Reads PDF and returns one Document per page.

---

## 2️⃣ Text File Loader

```python
from langchain.document_loaders import TextLoader

loader = TextLoader("notes.txt")
documents = loader.load()
```

---

## 3️⃣ CSV Loader

```python
from langchain.document_loaders import CSVLoader

loader = CSVLoader("data.csv")
documents = loader.load()
```

---

## 4️⃣ Web Loader (Website)

```python
from langchain.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
documents = loader.load()
```

---

## 5️⃣ Directory Loader (Load multiple files)

```python
from langchain.document_loaders import DirectoryLoader

loader = DirectoryLoader("./docs/")
documents = loader.load()
```

---

# 🔥 Where It Fits in RAG

```
Raw Data (PDF / Web / CSV)
        ↓
Document Loader
        ↓
Documents (structured format)
        ↓
Text Splitter
        ↓
Embeddings
        ↓
Vector DB
```

---

# 🔹 Simple Real-Life Example

Imagine you want to build a chatbot for your GATE notes.

Step 1:
You have:

* Compiler.pdf
* OS.pdf
* TOC.pdf

Step 2:
Document Loader reads them.

Step 3:
Now LangChain understands your notes.

---

# 🎯 Interview-Ready Definition

> A Document Loader in LangChain is a component that loads data from external sources and converts it into standardized Document objects containing text and metadata, which are then used in RAG pipelines for embedding and retrieval.

---


--------------------------------------------------------------------------------------------------------------------------------------
================================================================================================================================================================================================================================================================================================================================


PDF Loader in LangChain - Short Notes

PDF Loader is used to read PDF files in LangChain.
It extracts text from PDF documents.
It converts PDF content into Document objects.
Each Document contains:
1. page_content (actual text)
2. metadata (source, page number)

PDF Loader is mainly used in RAG pipelines.
It is the first step before text splitting and embeddings.

Basic Example

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("sample.pdf")
documents = loader.load()

print(documents[0].page_content)
print(documents[0].metadata)

load() vs lazy_load()

load() loads entire PDF at once.
lazy_load() loads page by page.
lazy_load() is memory efficient for large PDFs.

Different Types of PDF Loaders in LangChain

1. PyPDFLoader
   Uses PyPDF library.
   Simple and most commonly used.
   Best for normal text-based PDFs.
   Each page becomes one Document.

2. UnstructuredPDFLoader
   Uses unstructured library.
   Better for complex layouts.
   Can extract structured elements.
   Useful for tables and formatted PDFs.

3. PyMuPDFLoader
   Uses PyMuPDF (fitz library).
   Faster and more powerful.
   Good for large PDFs.
   Handles metadata and layout better.

4. PDFMinerLoader
   Uses pdfminer library.
   Good for detailed text extraction.
   Preserves layout information better.

5. OnlinePDFLoader
   Loads PDF directly from URL.
   Useful when PDF is hosted online.

Common Errors

FileNotFoundError if path is wrong.
Scanned PDFs may not extract text.
Scanned PDFs need OCR tools.
Encoding issues may occur sometimes.

Where It Fits in RAG

PDF File
↓
PDF Loader
↓
Documents
↓
Text Splitter
↓
Embeddings
↓
Vector Database

Important Interview Points

PDF Loader extracts text from PDF files.
Each page becomes a Document object.
Metadata includes page number and source.
Used as first step in RAG pipeline.
Different loaders exist for different use cases.

Summary

PDF Loader helps LangChain read PDF files.
It converts PDF content into structured documents.
Choose loader based on PDF complexity and size.


===============================================================================================




Directory Loader in LangChain - Short Notes

DirectoryLoader is used to load multiple files from a folder.
Instead of loading one file at a time, it loads all files inside a directory.
It is useful when you have many documents for RAG.

Why We Use DirectoryLoader

When working on real projects, data is stored in folders.
Example:
data/
  file1.txt
  file2.pdf
  file3.txt

Instead of loading each file manually,
DirectoryLoader loads everything at once.

Basic Example

from langchain_community.document_loaders import DirectoryLoader

loader = DirectoryLoader("data/")
documents = loader.load()

print(len(documents))

What It Does

It scans the given folder.
It loads supported files.
It converts them into Document objects.
Each file becomes one or more Document objects.
Metadata contains file path and source.

Using with Specific Loader

You can specify file type and loader.

from langchain_community.document_loaders import TextLoader

loader = DirectoryLoader(
    "data/",
    glob="*.txt",
    loader_cls=TextLoader
)

documents = loader.load()

glob="*.txt" means load only text files.

Where It Fits in RAG

Folder of Files
↓
DirectoryLoader
↓
Documents
↓
Text Splitter
↓
Embeddings
↓
Vector Database

Important Points

Loads multiple files at once.
Saves time in large projects.
Works with different file types.
Often used in production RAG systems.

Common Error

Wrong folder path causes FileNotFoundError.
Always check working directory.

Summary

DirectoryLoader loads all files from a folder.
It simplifies large document handling.
It is very useful in real-world RAG applications.



================================================================*********************************************************************=========================================

Load vs Lazy Load in LangChain

Load and Lazy Load are two different ways of reading documents in LangChain.
Both methods are used in Document Loaders like TextLoader, PyPDFLoader, etc.
The main difference between them is how and when the data is loaded into memory.

The load() method reads the entire document at once.
When we call load(), it immediately loads all pages or content into memory.
It returns a list of Document objects.
If the file is small, load() works perfectly fine.
But if the file is very large, it may consume more memory.
This can slow down the system.

Example of load()

loader = PyPDFLoader("sample.pdf")
documents = loader.load()

In this case, the whole PDF is loaded at once.
All pages are stored in the documents list.

Lazy loading works differently.
The lazy_load() method loads data step by step.
It does not load everything at once.
Instead, it returns an iterator.
Documents are generated one by one when needed.
This is memory efficient.

Example of lazy_load()

loader = PyPDFLoader("sample.pdf")

for doc in loader.lazy_load():
    print(doc.page_content)

Here, each page is loaded only when the loop runs.
This reduces memory usage.
It is useful for very large files.

Key Difference

load() loads everything immediately.
lazy_load() loads content only when required.

When to Use load()

Use load() for small files.
Use load() when memory is not a concern.
Use load() when you need all documents at once.

When to Use lazy_load()

Use lazy_load() for large PDFs.
Use lazy_load() when memory efficiency is important.
Use lazy_load() in streaming or production systems.

Interview Point

load() returns a list.
lazy_load() returns an iterator.
lazy loading improves performance for large datasets.

Short Notes Summary

load() loads entire file into memory.
lazy_load() loads file step by step.
load() is simple but memory heavy.
lazy_load() is efficient and scalable.
lazy_load() is preferred for large documents.

Conclusion

Both load() and lazy_load() are important.
The choice depends on file size and memory requirements.
For small practice files, load() is fine.
For real-world RAG systems with large documents, lazy_load() is better.




============================================================================================================


🌐 WebBaseLoader in LangChain - Concept & Short Notes

WebBaseLoader is used to load data from websites.
It fetches webpage content using a URL.
It extracts readable text from HTML pages.
It converts webpage content into Document objects.

📌 Why We Use WebBaseLoader

LLMs cannot directly read websites.
Websites contain HTML, CSS, and scripts.
WebBaseLoader extracts only useful text.
It helps build RAG systems from online content.

🧠 Basic Working

Website URL
   ↓
WebBaseLoader
   ↓
Extract Text
   ↓
Document Objects

📦 Basic Example

from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://example.com")
documents = loader.load()

print(documents[0].page_content)

📄 What It Returns

It returns a list of Document objects.
Each Document contains:
- page_content → extracted webpage text
- metadata → source URL

⚡ load() vs lazy_load()

load() → loads full webpage at once.
lazy_load() → loads content step by step.
lazy_load() is memory efficient.

🎯 Use Cases

✔️ Build chatbot from blog content
✔️ Load documentation websites
✔️ Extract online research material
✔️ Create Q&A system from web articles

⚠️ Common Issues

❌ Some websites block bots.
❌ JavaScript-heavy sites may not load fully.
❌ Internet connection required.
❌ Dynamic content may not appear.

🔎 Important Points for Interview

WebBaseLoader loads content from URLs.
It extracts readable text from HTML.
It converts web data into Document format.
It is used in RAG pipelines.
Metadata contains the source link.

🧩 Where It Fits in RAG

Website URL
   ↓
WebBaseLoader 🌐
   ↓
Text Splitter ✂️
   ↓
Embeddings 🔢
   ↓
Vector Database 🗄️
   ↓
Retriever 🔎
   ↓
LLM 🤖

📘 Short Summary

WebBaseLoader helps LangChain read websites.
It extracts useful content from web pages.
It converts web text into Document objects.
It is useful for online knowledge-based RAG systems.
