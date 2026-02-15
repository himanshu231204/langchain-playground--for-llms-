============================================================
CHROMA DB – INTERNAL ARCHITECTURE (DEEP DIVE)
============================================================

1. OVERVIEW
------------------------------------------------------------
Chroma is not just a simple vector store.
Internally, it is designed as a modular system that handles:

- Document storage
- Embedding storage
- Indexing
- Metadata filtering
- Persistence
- Query processing

It is optimized for LLM and RAG applications.

------------------------------------------------------------

2. HIGH-LEVEL ARCHITECTURE
------------------------------------------------------------

                  User Query
                       ↓
              Embedding Function
                       ↓
              Query Embedding Vector
                       ↓
                Chroma Collection
        ┌───────────────────────────┐
        │ 1. Vector Index           │
        │ 2. Metadata Store         │
        │ 3. Document Store         │
        │ 4. ID Mapping Layer       │
        └───────────────────────────┘
                       ↓
              Similarity Search Engine
                       ↓
                Top-K Results
                       ↓
                     LLM

------------------------------------------------------------

3. MAIN INTERNAL LAYERS
------------------------------------------------------------

A) COLLECTION LAYER
---------------------
A Collection is like a container.
It holds:

- Embeddings
- Documents
- Metadata
- Unique IDs

Each collection works independently.

Example:
collection_name = "ai_notes"

------------------------------------------------------------

B) EMBEDDING STORAGE LAYER
------------------------------------------------------------
Stores high-dimensional vectors.

Example:
[0.123, -0.443, 0.991, ...]

These vectors are stored efficiently in memory
and optionally on disk.

------------------------------------------------------------

C) INDEXING LAYER
------------------------------------------------------------
Purpose:
Fast similarity search.

Chroma internally uses Approximate Nearest Neighbor (ANN).

Why ANN?
Because exact search in high-dimensional space is slow.

Common indexing concepts used:

1) HNSW (Hierarchical Navigable Small World Graph)
2) IVF (Inverted File Index)
3) Brute Force (for small datasets)

ANN trades slight accuracy for huge speed gain.

------------------------------------------------------------

D) METADATA STORE
------------------------------------------------------------
Chroma stores metadata separately.

Example:
{
    "source": "chapter1",
    "author": "Himanshu"
}

Metadata filtering happens BEFORE similarity ranking.

Example:
Search only documents where source="chapter1"

------------------------------------------------------------

E) DOCUMENT STORE
------------------------------------------------------------
Stores original text chunks.

Vector index only stores embeddings.
But final output requires original text.

So Chroma keeps document-text mapping internally.

------------------------------------------------------------

F) ID MAPPING LAYER
------------------------------------------------------------
Each document has a unique ID.

ID connects:
Embedding ↔ Metadata ↔ Original Text

Without ID mapping,
system cannot retrieve correct document.

------------------------------------------------------------

4. QUERY EXECUTION FLOW (STEP-BY-STEP)
------------------------------------------------------------

Step 1: User sends query
Step 2: Query converted into embedding
Step 3: Metadata filtering applied (if any)
Step 4: ANN index searches nearest vectors
Step 5: Top-K IDs selected
Step 6: Retrieve original text using ID mapping
Step 7: Return documents to user / LLM

------------------------------------------------------------

5. PERSISTENCE ARCHITECTURE
------------------------------------------------------------

If persist_directory is set:

Chroma saves:

- Embeddings
- Metadata
- Index structure
- Collection info

On restart:
Chroma reloads everything from disk.

This makes it production-friendly.

------------------------------------------------------------

6. MEMORY MANAGEMENT
------------------------------------------------------------

Chroma handles:

- In-memory storage for fast search
- Disk-based storage for persistence
- Efficient batching during insertion

Large datasets require careful chunk sizing.

------------------------------------------------------------

7. SCALABILITY LIMITS
------------------------------------------------------------

Chroma is great for:

- Local development
- Medium-sized datasets
- Prototyping

For very large distributed systems,
cloud vector DBs (like Pinecone) are preferred.

------------------------------------------------------------

8. MATHEMATICAL CORE
------------------------------------------------------------

Similarity computation usually uses:

Cosine Similarity

cos(theta) = (A . B) / (||A|| * ||B||)

High similarity → Small angular distance

ANN reduces search complexity from:

O(n) → approximately O(log n)

------------------------------------------------------------

9. DESIGN PRINCIPLES
------------------------------------------------------------

Chroma is built with:

- Simplicity
- Developer friendliness
- LLM-first architecture
- Metadata-aware search
- Persistence support

------------------------------------------------------------

10. INTERNAL DATA FLOW SUMMARY
------------------------------------------------------------

Insert Flow:

Document
   ↓
Text Splitter
   ↓
Embedding Function
   ↓
Store in Collection
   ↓
Index Updated

Query Flow:

Query
   ↓
Embedding
   ↓
Metadata Filter
   ↓
ANN Search
   ↓
Retrieve Text
   ↓
Return Top-K

------------------------------------------------------------

11. INTERVIEW READY SUMMARY
------------------------------------------------------------

"Internally, Chroma consists of a collection layer,
embedding storage, ANN-based indexing, metadata store,
and ID mapping system. It performs filtered semantic
similarity search and supports persistence for RAG systems."

------------------------------------------------------------

12. KEY UNDERSTANDING
------------------------------------------------------------

- Collection is the core container.
- ANN indexing enables fast search.
- Metadata filtering improves precision.
- ID mapping connects embeddings to original text.
- Persistence allows production usage.

============================================================
END OF INTERNAL ARCHITECTURE NOTES
============================================================
