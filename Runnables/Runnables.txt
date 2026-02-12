These notes combine **official documentation ideas + practical usage + comparisons** and are **detailed and thorough** for deep learning or revision. 📘

---

✅ What Runnables are
✅ Runnable core interface methods
✅ Common Runnable types
✅ Runnable composition (Sequential / Parallel / Branch)
✅ How Agents and Chains relate
✅ Runnable vs Chain vs LCEL
✅ Streaming, Async, Batching
✅ Internal mechanics & practical tips
---
# **Runnables in LangChain — Detailed Notes (.txt format)**

---

## **1) What Is a Runnable?**

**Definition:**
A **Runnable** is the **core standard primitive in LangChain** — a *generic executable unit* that takes an input, does something, and returns an output.
It defines a **uniform interface** that all core components (LLMs, prompts, output parsers, retrievers, tools, functions, chains) follow. ([LangChain Reference][1])

**Why LangChain uses Runnables:**
✔ Provides a single consistent API for many components
✔ Makes chaining or composing steps easy
✔ Adds support for streaming, batching, async execution
✔ Enables flexible workflows (parallel execution, branching, conditional logic)
✔ Helps build complex AI flows modularly instead of hard-coding sequences. ([LangChain Reference][1])

---

## **2) Runnable Core Interface**

Every Runnable supports:

```
.invoke(input)     → run once → returns result
.ainvoke(input)    → async invoke
.batch(inputs)    → run multiple inputs
.abatch(inputs)   → async batch
.stream(input)    → streaming output
.astream(input)   → async streaming
```

These methods provide a **uniform way to execute logic** regardless of what the runnable actually is. ([LangChain Reference][2])

**Key idea:**
Runnables don’t just run. They support **batching, streaming, and async operations** by default.

---

## **3) Main Types of Runnables**

Here’s a rundown of the most common Runnable primitives:

---

### **3.1 RunnableLambda**

Converts a normal Python/JS function into a Runnable such that it can be part of a chain.

Example idea:

```python
from langchain_core.runnables import RunnableLambda
add_one = RunnableLambda(lambda x: x + 1)
result = add_one.invoke(10)  # → 11
```

Wraps custom logic as a runnable unit. ([LangChain Reference][3])

---

### **3.2 RunnableSequence**

A **sequence/chain** of steps executed one after the other.

Instead of writing:

```
step1(data)
step2(step1_output)
step3(step2_output)
```

You write:

```
chain = prompt | llm | parser
```

This creates a **RunnableSequence**: input flows through steps. ([LangChain Reference][4])

---

### **3.3 RunnableParallel**

Runs multiple runnables **in parallel on the same input**, and returns a mapping of results.

Example concept:

```
{
  "summary": summary_chain,
  "sentiment": sentiment_chain
}
```

Input goes into both branches simultaneously. ([LangChain Reference][5])

---

### **3.4 RunnableBranch**

A **conditional runnable** that routes execution based on a test.

Example concept:

```
if length > 300:
    use long-summary
else:
    use short-summary
```

This is similar to `if-else` logic inside a pipeline. ([linkedin.com][6])

---

### **3.5 RunnablePassthrough**

Does nothing — simply passes the input forward unchanged.

Useful for:

* Debugging
* Serving as placeholder logic
* Combining with parallel execution for keys that don’t transform input. ([Medium][7])

---

### **3.6 (Other Advanced Types)**

These are not always required but useful:

✔ RunnableGenerator — for custom streaming logic
✔ RunnableWithFallbacks — fallback behavior
✔ RunnableWithMessageHistory — manage conversation history
✔ RunnableWithRetry — add retry logic
✔ RunnableWithTimeout — enforce execution limits ([Medium][8])

---

## **4) Composition — Building Workflows**

Runnables shine because you can **compose them easily**.

### **4.1 Sequential Composition**

Connect runnables end-to-end:

```
prompt | model | parser
```

Equivalent to:

```
parser(model(prompt(input)))
```

---

### **4.2 Parallel Composition**

```
{
  "summary": summary_chain,
  "quiz": quiz_chain
}
```

→ both chains run on input
→ combined results returned as dictionary. ([LangChain Reference][5])

---

### **4.3 Mixed Composition**

You can combine sequence + parallel:

```
prompt
  ↓
parallel (summary, sentiment)
  ↓
merge/parser
```

This yields more complex pipelines where results from parallel paths can be aggregated. ([linkedin.com][6])

---

## **5) LCEL — LangChain Expression Language**

LCEL is the **new declarative way** to build pipelines using Runnables.
It uses familiar syntax like `|` (pipe) and `dict` literals to compose runnables more naturally:

```
chain = prompt | llm | parser
```

LCEL is basically a **syntactic sugar** that compiles down to RunnableSequence / RunnableParallel internally. ([langchain-opentutorial.gitbook.io][9])

---

## **6) Runnables vs Old Chains vs Agents**

### **Old Chains**

Traditionally, LangChain had many different Chain classes (LLMChain, SQLDatabaseChain, etc.).
Drawbacks:

* Harder to unify
* Harder to compose
* Limited streaming support

---

### **Runnables**

Unified interface:

* Works with prompt templates
* Works with LLM models
* Works with output parsers
* Works with custom functions

This makes workflows more modular and composable. ([Medium][10])

---

### **Agents**

Agents (higher-level decision systems that call tools) **also use Runnables internally**.

An AgentExecutor itself is a Runnable that:

* receives input
* makes decisions
* runs tools
* returns outputs.
  Thus, the entire agent becomes an executable runnable pipeline.

---

## **7) Streaming, Async & Batching**

Modern AI applications often benefit from partial outputs and parallel processing.

Runnables provide built-in support for:
✔ streaming responses (chunk by chunk)
✔ asynchronous execution
✔ batch execution across multiple inputs
✔ nested streaming + parallelism ([LangChain Reference][2])

This is a big upgrade over older designs where streaming had to be implemented manually.

---

## **8) Practical Usage Patterns**

### **Custom Logic**

Use RunnableLambda to wrap any business logic and drop it into a chain.

---

### **Conditional Logic**

Use RunnableBranch when what you do next depends on the output:

```
if model_response contains long text: summarize
else: keep original
```

---

### **Parallel Tasks**

Use RunnableParallel for tasks like:

* summarization
* sentiment analysis
* keyword extraction
  in one pass.

---

## **9) Benefits of Runnables**

📌 **Modularity** — split work into smaller, reusable steps
📌 **Composability** — easy to connect runnables
📌 **Flexibility** — control logic paths
📌 **Performance benefits** — parallel execution
📌 **Streaming & Async** — built-in support
📌 **Unified interface** — makes everything consistent ([DEV Community][11])

---

## **10) Summary**

```
Runnable = input → do something → output
```

By standardizing the interface across different components, LangChain made building complex AI systems easier, more robust, and more maintainable. ([LangChain Reference][1])

---

## **Recommended Steps to Practice**

✔ Build simple chains using `|` operator
✔ Wrap custom functions with RunnableLambda
✔ Experiment with RunnableParallel
✔ Try conditional flows with RunnableBranch
✔ Use streaming for real-time outputs
✔ Explore async pipelines

---


## 🔷 Types of Runnables in LangChain

In LangChain, **Runnables** are categorized into two main types:

```
1️⃣ Primitive Runnables
2️⃣ Task-Specific Runnables
```

This classification helps you understand:

* Which ones are **low-level building blocks**
* Which ones are **high-level ready-made components**

---

# 🧱 1️⃣ Primitive Runnables

Primitive Runnables are the **core foundational building blocks**.

They don’t perform a specific AI task like summarization or retrieval.
Instead, they provide **execution logic and composition capabilities**.

Think of them like:

> 🏗️ LEGO blocks used to build workflows.

---

## 🔹 Common Primitive Runnables

---

### 1️⃣ RunnableLambda

Wraps a normal Python function into a Runnable.

Purpose:

* Add custom logic
* Preprocessing
* Postprocessing
* Business logic

Example:

```
Input → Python Function → Output
```

---

### 2️⃣ RunnableSequence

Runs multiple Runnables **in order (step-by-step)**.

Created automatically when using:

```
chain = A | B | C
```

Flow:

```
Input → A → B → C → Output
```

---

### 3️⃣ RunnableParallel

Runs multiple Runnables **at the same time** on the same input.

Flow:

```
         ┌─ Chain A
Input ───┤
         └─ Chain B
```

Returns:

```
{
  "A": resultA,
  "B": resultB
}
```

---

### 4️⃣ RunnableBranch

Implements conditional logic (if-else routing).

Flow:

```
Input
  │
  ├─ If condition → Chain A
  └─ Else → Chain B
```

Used for:

* Smart routing
* Tool selection
* Decision systems

---

### 5️⃣ RunnablePassthrough

Does nothing. Just forwards input.

Useful when:

* You need original input preserved
* Combining parallel outputs

---

### 6️⃣ RunnableGenerator

Used for custom streaming behavior.

---

### 7️⃣ Wrapper Runnables

These add execution behavior:

* with_retry()
* with_fallbacks()
* with_timeout()
* with_config()

These modify how a runnable behaves.

---

## 🔹 What Primitive Runnables Do

They control:

✔ Execution order
✔ Parallelism
✔ Branching
✔ Error handling
✔ Streaming
✔ Retry
✔ Async

They are **infrastructure-level components**.

---

# 🎯 2️⃣ Task-Specific Runnables

These are **higher-level Runnables** built to perform specific AI tasks.

They usually wrap models, prompts, retrievers, tools, or chains.

Think of them as:

> 🧠 Functional AI components ready to do real tasks.

---

## 🔹 Examples of Task-Specific Runnables

---

### 1️⃣ Chat Models / LLMs

Example:

* ChatOpenAI
* Other chat models

These are Runnables because:

```
Input (prompt/messages) → Model → Output
```

---

### 2️⃣ Prompt Templates

PromptTemplate and ChatPromptTemplate are Runnables.

They transform structured input into formatted prompts.

```
Input variables → formatted prompt
```

---

### 3️⃣ Output Parsers

StrOutputParser, JSONOutputParser, etc.

They convert model output into:

* String
* JSON
* Structured data

---

### 4️⃣ Retrievers

Vector store retrievers are Runnables.

```
Query → Relevant Documents
```

Used in:

* RAG systems

---

### 5️⃣ Tools

Tools (used in agents) are Runnables.

```
Input → Tool execution → Output
```

---

### 6️⃣ Chains

Modern chains are built using Runnables.

Example:

```
Prompt | LLM | Parser
```

That whole chain is a Runnable.

---

### 7️⃣ Agents

Agents internally use Runnables for:

* Decision making
* Tool calling
* Planning

AgentExecutor itself behaves like a Runnable.

---

# 🆚 Primitive vs Task-Specific Runnables

| Feature                    | Primitive       | Task-Specific |
| -------------------------- | --------------- | ------------- |
| Level                      | Low-level       | High-level    |
| Purpose                    | Execution logic | AI task logic |
| Example                    | RunnableLambda  | ChatOpenAI    |
| Controls flow?             | Yes             | No            |
| Performs AI task?          | No              | Yes           |
| Used to compose pipelines? | Yes             | Yes           |

---

## 🧠 Simple Mental Model

Primitive Runnables = HOW to run
Task-Specific Runnables = WHAT to run

Example:

```
Prompt (task-specific)
   ↓
LLM (task-specific)
   ↓
Parser (task-specific)

Sequence operator | (primitive)
```

---

# 🔥 Real Example

```
clean_text (Primitive)
   ↓
Prompt (Task-specific)
   ↓
LLM (Task-specific)
   ↓
Parser (Task-specific)
   ↓
Branch (Primitive)
```

Primitive Runnables control execution.
Task-Specific Runnables perform AI work.

---



**END of Notes**
