# 🔄 Runnables in LangChain (LCEL)

> Comprehensive notes on the Runnable interface — the core primitive powering LangChain Expression Language (LCEL).

## Table of Contents

- [What Is a Runnable?](#what-is-a-runnable)
- [Runnable Core Interface](#runnable-core-interface)
- [Primitive Runnables](#primitive-runnables)
- [Task-Specific Runnables](#task-specific-runnables)
- [Composition](#composition)
- [LCEL — LangChain Expression Language](#lcel--langchain-expression-language)
- [Runnables vs Old Chains vs Agents](#runnables-vs-old-chains-vs-agents)
- [Streaming, Async & Batching](#streaming-async--batching)
- [When to Use TypedDict / Pydantic / JSON Schema](#when-to-use-typeddict--pydantic--json-schema)

## Related Notes

- [Chains Overview](../Chain/chain.md)
- [Parallel Chain](../Chain/parallel_chain.md)
- [Conditional Chain](../Chain/conditional_Chain.md)
- [Output Parsers](../Output_Parsers/notes1.md)
- [RAG Retrievers](../Rag%20Components/Retrievers/retriver.md)
- [Agent Notes](../Mini_projects/agent_notes.md)

---

## What Is a Runnable?

A **Runnable** is the **core standard primitive in LangChain** — a generic executable unit that takes an input, does something, and returns an output.

It defines a **uniform interface** that all core components follow: LLMs, prompts, output parsers, retrievers, tools, functions, and chains.

**Why LangChain uses Runnables:**

- ✔ Provides a single consistent API for many components
- ✔ Makes chaining or composing steps easy
- ✔ Adds support for streaming, batching, and async execution
- ✔ Enables flexible workflows (parallel, branching, conditional)
- ✔ Helps build complex AI flows modularly

---

## Runnable Core Interface

Every Runnable supports:

```python
.invoke(input)     # run once → returns result
.ainvoke(input)    # async invoke
.batch(inputs)     # run multiple inputs
.abatch(inputs)    # async batch
.stream(input)     # streaming output
.astream(input)    # async streaming
```

---

## Primitive Runnables

Primitive Runnables are the **core foundational building blocks** — they control execution logic and composition.

### RunnableLambda

Wraps a normal Python function into a Runnable.

```python
from langchain_core.runnables import RunnableLambda

add_one = RunnableLambda(lambda x: x + 1)
result = add_one.invoke(10)  # → 11
```

Used for: custom logic, preprocessing, postprocessing, business logic.

---

### RunnableSequence

Runs multiple Runnables **in order**. Created automatically with the `|` pipe operator:

```python
chain = prompt | llm | parser
```

Flow: `Input → A → B → C → Output`

> This is the foundation of [Chains](../Chain/chain.md).

---

### RunnableParallel

Runs multiple Runnables **simultaneously** on the same input:

```python
from langchain_core.runnables import RunnableParallel

chain = RunnableParallel(
    summary=summary_chain,
    sentiment=sentiment_chain
)
# Returns: {"summary": "...", "sentiment": "..."}
```

> See [Parallel Chain](../Chain/parallel_chain.md) for usage patterns.

---

### RunnableBranch

Implements **conditional logic** (IF-ELSE routing):

```python
from langchain_core.runnables import RunnableBranch

branch = RunnableBranch(
    (lambda x: x["sentiment"] == "positive", positive_chain),
    negative_chain  # default
)
```

> See [Conditional Chain](../Chain/conditional_Chain.md) for detailed patterns.

---

### RunnablePassthrough

Does nothing — simply passes input forward unchanged.

```python
from langchain_core.runnables import RunnablePassthrough

chain = RunnablePassthrough() | next_step
```

Useful for: debugging, preserving original input in parallel branches.

---

### RunnableGenerator

Used for custom streaming behavior.

---

### Wrapper Runnables

These modify **how** a runnable behaves:

```python
runnable.with_retry()       # retry on failure
runnable.with_fallbacks()   # fallback behavior
runnable.with_timeout()     # enforce time limits
runnable.with_config()      # override config
```

---

## Task-Specific Runnables

These are **higher-level Runnables** that perform specific AI tasks:

| Type | Examples | Role |
|------|----------|------|
| Chat Models / LLMs | `ChatOllama`, `ChatOpenAI` | Generate text from prompts |
| Prompt Templates | `PromptTemplate`, `ChatPromptTemplate` | Format input into prompts |
| Output Parsers | `StrOutputParser`, `JsonOutputParser` | Parse LLM output |
| Retrievers | Vector store retrievers | Fetch relevant documents |
| Tools | Custom and built-in tools | Execute external actions |
| Chains | `prompt \| llm \| parser` | Full pipelines |
| Agents | `AgentExecutor` | Multi-step decision systems |

> See [Output Parsers](../Output_Parsers/notes1.md) and [RAG Retrievers](../Rag%20Components/Retrievers/retriver.md) for details.

---

## Composition

### Sequential Composition

```python
chain = prompt | model | parser
# equivalent to: parser(model(prompt(input)))
```

### Parallel Composition

```python
chain = RunnableParallel(
    summary=summary_chain,
    quiz=quiz_chain
)
```

### Mixed Composition

```
prompt
  ↓
RunnableParallel (summary, sentiment)
  ↓
merge/parser
```

---

## LCEL — LangChain Expression Language

LCEL is the **declarative way** to build pipelines using Runnables. It uses the `|` operator and dict literals:

```python
chain = prompt | llm | parser
```

LCEL compiles down to `RunnableSequence` / `RunnableParallel` internally. It adds:

- ✔ Streaming support by default
- ✔ Async support by default
- ✔ Easy composition
- ✔ Consistent interface across all components

---

## Runnables vs Old Chains vs Agents

| | Old Chains | Runnables (LCEL) | Agents |
|-|-----------|-----------------|--------|
| Interface | Many different classes | Unified | Unified |
| Streaming | Limited | ✅ Built-in | ✅ Built-in |
| Composition | Hard | ✅ Easy | ✅ Easy |
| Use case | Fixed workflows | Flexible pipelines | Dynamic decision-making |

---

## Streaming, Async & Batching

```python
# Streaming (token-by-token output)
for chunk in chain.stream({"topic": "AI"}):
    print(chunk, end="", flush=True)

# Async
result = await chain.ainvoke({"topic": "AI"})

# Batching
results = chain.batch([{"topic": "AI"}, {"topic": "ML"}])
```

---

## When to Use TypedDict / Pydantic / JSON Schema

| Use Case | Recommended |
|----------|-------------|
| Internal type hints only, trusted data | `TypedDict` |
| External/untrusted data, runtime validation, type conversion | `Pydantic` |
| Schema for external APIs or cross-environment JSON interchange | `JSON Schema` |

### Decision Guide

```
Trust your data & internal use    →  TypedDict
External data & need validation   →  Pydantic
Schema for external systems       →  JSON Schema
```

> See [Structured Output](../Structured%20Output/structured.md) and [Pydantic Output Parser](../Output_Parsers/PydanticOutputParser.md) for more details.

---

## Primitive vs Task-Specific: Summary

| Feature | Primitive Runnables | Task-Specific Runnables |
|---------|--------------------|-----------------------|
| Level | Low-level (infrastructure) | High-level (AI logic) |
| Purpose | Control execution flow | Perform AI tasks |
| Examples | `RunnableLambda`, `RunnableBranch` | `ChatOpenAI`, `StrOutputParser` |
| Controls flow? | Yes | No |
| Performs AI task? | No | Yes |

> **Mental model:** Primitive Runnables = **HOW** to run. Task-Specific Runnables = **WHAT** to run.
