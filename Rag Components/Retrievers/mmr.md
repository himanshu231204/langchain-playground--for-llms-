========================================
MMR (Maximal Marginal Relevance)
LangChain Retriever Notes
========================================

1. What is MMR?

MMR = Maximal Marginal Relevance

It is a retrieval technique used in LangChain
to return documents that are:
- Relevant to the query
- Diverse from each other

----------------------------------------

2. Problem with Normal Similarity Search

Normal similarity search:
- Finds top-k most similar documents to query
- Uses cosine similarity

Problem:
- Top results may be very similar to each other
- Context becomes repetitive
- Wastes LLM context window

----------------------------------------

3. What MMR Does

MMR balances two things:
1) Relevance to the query
2) Diversity among selected documents

It avoids returning duplicate-like chunks.

----------------------------------------

4. Conceptual Formula

MMR Score =

λ × (Similarity to Query)
- (1 - λ) × (Similarity to Selected Docs)

Where:
λ (lambda) controls balance.

If:
λ = 1   → Pure similarity search
λ = 0   → Only diversity
λ = 0.5 → Balanced

----------------------------------------

5. Why Important in RAG?

In RAG systems:
- Repetitive chunks reduce answer quality
- Context window gets wasted

MMR ensures:
✔ Better topic coverage
✔ Less duplication
✔ Improved LLM answers

----------------------------------------

6. How to Use in LangChain

retriever = vectorstore.as_retriever(
    search_type="mmr",
    search_kwargs={
        "k": 4,
        "lambda_mult": 0.5
    }
)

Parameters:
k → number of final documents
lambda_mult → controls diversity vs relevance

----------------------------------------

7. When to Use MMR?

Use MMR when:
- Documents are highly similar
- You want broader coverage
- Building RAG applications

----------------------------------------

8. Quick Interview Answer

MMR improves retrieval quality by balancing
relevance and diversity, reducing redundancy
in retrieved documents for better LLM output.

========================================
END
========================================