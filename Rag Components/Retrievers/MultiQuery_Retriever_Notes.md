==================================================
MultiQuery Retriever – LangChain Notes
==================================================

1. What is MultiQuery Retriever?

MultiQueryRetriever is an advanced retriever in LangChain
that generates multiple variations of a user query using an LLM
and retrieves documents for each variation.

It improves recall in RAG systems.

--------------------------------------------------

2. Why Do We Need It?

Problem with normal retrieval:
- Vector search depends heavily on query wording.
- If document wording differs, relevant docs may not be retrieved.

Example:
Query: "Benefits of LangChain"

But documents may contain:
- "Advantages of LangChain"
- "Why use LangChain?"
- "Features of LangChain"

Normal retriever may miss them.

--------------------------------------------------

3. How MultiQuery Works

Step 1: Take original user query.
Step 2: Use LLM to generate multiple rephrased queries.
Step 3: Perform retrieval for each generated query.
Step 4: Merge results.
Step 5: Remove duplicate documents.

--------------------------------------------------

4. Internal Flow

User Query
    ↓
LLM generates multiple query variations
    ↓
Each query → Vector Search
    ↓
Combine results
    ↓
Remove duplicates
    ↓
Final retrieved documents

--------------------------------------------------

5. Key Benefit

✔ Improves Recall (finds more relevant documents)
✔ Handles synonyms and rephrasing
✔ Better coverage of knowledge base

--------------------------------------------------

6. Drawback

❌ Extra LLM call (slower than normal retrieval)
❌ Slightly higher cost
❌ Not needed for very small datasets

--------------------------------------------------

7. Difference: MMR vs MultiQuery

MMR:
- Improves diversity of retrieved documents
- Reduces redundancy
- Does NOT expand query meaning

MultiQuery:
- Expands query meaning
- Improves recall
- Uses LLM internally

--------------------------------------------------

8. When To Use?

Use MultiQuery when:
- Knowledge base is large
- Query wording may vary
- Synonyms matter
- High recall is important

--------------------------------------------------

9. Interview Definition

MultiQueryRetriever improves retrieval performance
by generating multiple semantically different queries
from the original query using an LLM, and combining
the retrieved results to improve recall.

--------------------------------------------------

END
==================================================