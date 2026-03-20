# ⛓️ Chains in LangChain

> Notes on Simple Chains and Sequential Chains — the building blocks of LangChain pipelines.

## Table of Contents

- [Simple Chain](#simple-chain)
- [Sequential Chain](#sequential-chain)
- [Simple vs Sequential: Comparison](#simple-vs-sequential-comparison)

## Related Notes

- [Parallel Chain](parallel_chain.md)
- [Conditional Chain](conditional_Chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)
- [Output Parsers](../Output_Parsers/notes1.md)
- [Core Concepts & Prompts](../notes.md)

---

## Simple Chain

### What it is

A **Simple Chain** is a straight, single-step pipeline where input flows through a prompt, an LLM, and an output parser.

### Core idea

> **One task → One prompt → One model → One output**

### Flow

```
Input
  │
  ▼
PromptTemplate
  │
  ▼
LLM (Ollama / GPT / Mistral)
  │
  ▼
Output Parser
  │
  ▼
Final Answer
```

### When to use

- Single question–answer tasks
- Text generation
- Summarization
- Basic GenAI experiments

### Key benefits

- ✔ Simple to implement
- ✔ Easy to debug
- ✔ Best for beginners

---

## Sequential Chain

### What it is

A **Sequential Chain** connects multiple chains or steps, where the output of one step becomes the input of the next.

### Core idea

> **Step-by-step reasoning with memory between steps**

### Flow

```
Input
  │
  ▼
Chain / Step 1
  │  (output)
  ▼
Chain / Step 2
  │  (output)
  ▼
Chain / Step 3
  │
  ▼
Final Result
```

### Example use cases

- Topic → Explanation → Summary
- Question → Analysis → Final answer
- Content generation pipelines
- Multi-step GenAI workflows

### Key benefits

- ✔ Structured reasoning
- ✔ Better control over workflow
- ✔ Scales to real applications

---

## Simple vs Sequential: Comparison

| Feature | Simple Chain | Sequential Chain |
|---------|-------------|-----------------|
| Steps | Single | Multiple |
| Complexity | Low | Medium |
| Use case | One-shot tasks | Multi-step logic |
| Scalability | Limited | High |
| Production use | Rare | Common |

---

## One-line Revision

- **Simple Chain:** A single, linear GenAI pipeline for one task.
- **Sequential Chain:** A multi-step GenAI pipeline where each step feeds the next.

> **Simple Chains help you learn. Sequential Chains help you build real GenAI systems.**

---

## See Also

- [Parallel Chain](parallel_chain.md) — run multiple tasks simultaneously
- [Conditional Chain](conditional_Chain.md) — IF/ELSE routing between chains
- [Runnables (LCEL)](../Runnables/Runnables.md) — the underlying primitive powering chains
