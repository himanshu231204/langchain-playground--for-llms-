==============================
TEXT SPLITTER – LANGCHAIN
==============================

1) What is Text Splitter?
--------------------------
Text Spliter breaks large documents into smaller chunks 
before sending them to embeddings or LLM.

Why needed?
- LLM has token limit
- Better embedding quality
- Better retrieval in RAG
- Prevent context loss


2) Role in RAG Pipeline
--------------------------
Raw Docs → Text Splitter → Chunks → Embeddings → Vector DB → Retriever → LLM


3) Important Parameters
--------------------------
chunk_size     = Size of each chunk
chunk_overlap  = Overlapping text between chunks
separator      = Symbol used for splitting


4) Types of Text Splitters
===========================

A) CharacterTextSplitter
--------------------------
- Splits based on character count
- Simple and basic
- May cut sentences randomly

Best for:
- Small or simple text


B) RecursiveCharacterTextSplitter (Most Recommended)
-----------------------------------------------------
- Splits hierarchically
- Order:
    "\n\n" → "\n" → " " → ""
- Maintains meaning better

Best for:
- RAG systems
- General purpose chunking


C) TokenTextSplitter
-----------------------
- Splits based on tokens (not characters)
- Good when strict token limit is required

Best for:
- OpenAI or token-based models


D) MarkdownHeaderTextSplitter
--------------------------------
- Splits using markdown headers
- Keeps structure intact

Best for:
- README files
- Technical docs


5) Chunk Overlap Concept
--------------------------
Example:
chunk_size = 500
chunk_overlap = 100

Chunk1 → 0–500
Chunk2 → 400–900

Why overlap?
- Prevent context break
- Improve retrieval continuity


6) Choosing Chunk Size
--------------------------
Small models → 300–500 tokens
Large models → 500–1000 tokens
More overlap → Better retrieval but more storage


7) Key Interview Points
--------------------------
- Chunking affects retrieval quality
- Recursive splitter is most used
- Overlap prevents information loss
- Token splitting is useful for strict limits


==============================
CORE IDEA:
Better chunking → Better retrieval → Better RAG performance
==============================


========================================
LENGTH-BASED TEXT SPLITTING – LANGCHAIN
========================================

1) What is Length-Based Text Splitting?
----------------------------------------
It splits text based on fixed size 
(length = characters or tokens).

It does NOT consider meaning or structure.
It only checks size.

Example:
If chunk_size = 500
Text will be divided every 500 characters.


2) Why Use Length-Based Splitting?
----------------------------------------
- Control LLM token limit
- Simple and fast
- Useful for quick testing
- Works when structure is not important


3) Types of Length-Based Splitters
====================================

A) Character-Based Splitting
--------------------------------
Splitter: CharacterTextSplitter

- Splits based on character count
- Uses chunk_size and chunk_overlap

Important Parameters:
- chunk_size
- chunk_overlap
- separator

Problem:
- Can break sentences in middle


B) Token-Based Splitting
---------------------------
Splitter: TokenTextSplitter

- Splits based on token count
- Better for OpenAI models
- More accurate for LLM limits


4) Important Parameters
--------------------------------
chunk_size:
    Maximum size of each chunk

chunk_overlap:
    Repeated text between chunks
    Prevents context loss


5) Example Concept
--------------------------------
chunk_size = 100
chunk_overlap = 20

Chunk1 → 0–100
Chunk2 → 80–180
Chunk3 → 160–260


6) Advantages
--------------------------------
✔ Simple to implement
✔ Easy to control size
✔ Good for strict limits


7) Disadvantages
--------------------------------
✘ Ignores semantic meaning
✘ May break sentences
✘ Not ideal for structured docs


8) When to Use?
--------------------------------
- Quick prototype
- Non-structured text
- Strict token control needed


========================================
CORE IDEA:
Length-Based Splitting = Fixed Size Splitting
Focus is on SIZE, not meaning.
========================================
