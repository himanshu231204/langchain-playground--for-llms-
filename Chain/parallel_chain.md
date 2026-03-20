# ⚡ Parallel Chain in LangChain

> Notes on running multiple LLM tasks simultaneously using `RunnableParallel`.

## Table of Contents

- [What is a Parallel Chain?](#what-is-a-parallel-chain)
- [Flow Diagram](#flow-diagram)
- [Why Parallel Chains are Needed](#why-parallel-chains-are-needed)
- [Implementation in LangChain](#implementation-in-langchain)
- [Model Selection Rule](#model-selection-rule)
- [Best Practice: Hybrid Design](#best-practice-hybrid-design)
- [Common Mistakes](#common-mistakes)

## Related Notes

- [Simple & Sequential Chain](chain.md)
- [Conditional Chain](conditional_Chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)
- [Output Parsers](../Output_Parsers/notes1.md)

---

## What is a Parallel Chain?

A **Parallel Chain** runs multiple independent LLM tasks **at the same time** using the same or different LLMs. Each branch works independently, and their outputs are merged at the end.

> **One input → many tasks → run simultaneously → merge results**

---

## Flow Diagram

```
                ┌───────────────┐
                │   Input Doc   │
                │ (Raw Content) │
                └───────┬───────┘
                        │
          ┌─────────────┴─────────────┐
          │                           │
          ▼                           ▼
   ┌───────────────┐          ┌───────────────┐
   │   Module 1    │          │   Module 2    │
   │   (Notes)     │          │    (Quiz)     │
   │  LLM Role A   │          │  LLM Role B   │
   └───────┬───────┘          └───────┬───────┘
           │                           │
           ▼                           ▼
       Notes Output                Quiz Output
           │                           │
           └─────────────┬─────────────┘
                         ▼
                ┌─────────────────┐
                │   Merge Module  │
                │ (Combine Result)│
                └────────┬────────┘
                         ▼
                ┌─────────────────┐
                │   Final Output  │
                │  (Notes + Quiz) │
                └─────────────────┘
```

---

## Why Parallel Chains are Needed

- **Reduces latency** by running tasks simultaneously
- **Separates responsibilities** (notes, quiz, summary, analysis)
- **Builds scalable GenAI pipelines**
- **Improves modularity and clarity**

---

## Implementation in LangChain

LangChain provides `RunnableParallel` to execute multiple chains in parallel:

```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel(
    notes=prompt_notes | model | parser,
    quiz=prompt_quiz | model | parser
)

result = chain.invoke({"input": "your document content"})
# result = {"notes": "...", "quiz": "..."}
```

> See [Runnables (LCEL)](../Runnables/Runnables.md) for full details on `RunnableParallel`.

---

## Model Selection Rule

> ⚠️ **Very important for stable execution**

| LLM Type | Parallel Execution |
|----------|--------------------|
| Cloud LLMs (Gemini, OpenAI, Anthropic) | ✅ Safe |
| Local LLMs (Ollama) on Windows | ❌ Not reliable |

Parallel chains create **real concurrency** (threads / async execution), not just logical branching.

---

## Best Practice: Hybrid Design

Use cloud LLMs for parallel tasks and local LLMs only for sequential merging:

```
Input
  |-- Gemini → Task A  (parallel)
  |-- Gemini → Task B  (parallel)
  |
  └-- Ollama → Merge / Format  (sequential)
```

---

## Common Mistakes

- ❌ Using Ollama inside `RunnableParallel` on Windows → causes connection errors (`WinError 10061`)
- ❌ Piping Ollama after `RunnableParallel` — prefer cloud LLMs for parallel steps

---

## Summary

> A Parallel Chain runs multiple GenAI tasks simultaneously and should be used with scalable cloud-based LLMs for stable execution.

| | Simple Chain | Sequential Chain | Parallel Chain |
|-|-------------|-----------------|---------------|
| Execution | Single step | Step by step | Simultaneous |
| Use case | One-shot | Multi-step | Multi-task |
| Speed benefit | — | — | ✅ Faster |
