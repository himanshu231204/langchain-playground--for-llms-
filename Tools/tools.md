# 🔧 Tools in LangChain – Notes

> Notes on LangChain tools — functions that extend LLM capabilities beyond text generation.

## Table of Contents

- [What is a Tool?](#what-is-a-tool)
- [Why Are Tools Needed?](#why-are-tools-needed)
- [How a Tool Works](#how-a-tool-works)
- [Basic Structure of a Tool](#basic-structure-of-a-tool)
- [Types of Tools](#types-of-tools)
- [Tool vs Chain](#tool-vs-chain)
- [Tool vs Function Calling](#tool-vs-function-calling)
- [Tool and Agent Relationship](#tool-and-agent-relationship)
- [Tools in RAG Systems](#tools-in-rag-systems)
- [When to Use Tools](#when-to-use-tools)

## Related Notes

- [Tool Binding](tool_binding.md)
- [Tool Calling](tools_calling%20.md)
- [Custom Tools](custom_tools.md)
- [Toolkits](toolkit.md)
- [Agent Notes](../Mini_projects/agent_notes.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## What is a Tool?

A **Tool** in LangChain is a function that an LLM can call to perform actions **outside normal text generation**.

> **Definition:** Tool = A function that extends the capability of an LLM beyond text generation.

Normally, an LLM can only generate text. Real-world applications require:
- Searching the web
- Performing calculations
- Querying databases
- Calling APIs
- Reading files

Tools allow the LLM to perform these external actions.

---

## Why Are Tools Needed?

LLMs have limitations:

| Limitation | Tool Solution |
|------------|---------------|
| No real-time data | Live data fetching |
| Math mistakes | Accurate computation tools |
| No external system access | API integration |
| No database access | Database query tools |
| No file system access | File operation tools |

---

## How a Tool Works

```
User Question
      │
      ▼
LLM decides whether a tool is required
      │
      ▼  (if needed)
LLM calls the tool with arguments
      │
      ▼
Tool executes and returns output
      │
      ▼
LLM generates final answer using tool result
```

> ⚠️ **The LLM decides when and which tool to use** based on the tool's description.

---

## Basic Structure of a Tool

A Tool in LangChain has three key parts:

| Part | Description | Why It Matters |
|------|-------------|----------------|
| `name` | Unique identifier | Used to reference the tool |
| `description` | Explains when to use it | **LLM reads this to decide** |
| `function` | The actual Python logic | Performs the action |

> ⚠️ **The description is critical** — it is how the LLM decides whether to use the tool.

---

## Types of Tools

### A) Built-in Tools

Pre-built tools provided by LangChain:

| Tool | Description |
|------|-------------|
| Web search | Search the internet |
| Calculator | Perform math operations |
| Python REPL | Execute Python code |
| Wikipedia | Query Wikipedia |
| HTTP request tools | Make web API calls |

### B) Custom Tools

User-defined functions wrapped as tools. See [Custom Tools](custom_tools.md) for full notes.

---

## Tool vs Chain

| | Chain | Tool |
|-|-------|------|
| Execution | Fixed sequence of steps | Dynamic, called only when needed |
| Decision | Always runs | LLM decides to call it |
| Design | Static pipeline | Dynamic capability |
| Use case | Multi-step workflows | External actions |

> **Chain = Static pipeline** | **Tool = Dynamic callable capability**

---

## Tool vs Function Calling

| | Function Calling | Tool |
|-|-----------------|------|
| What it is | Built-in model capability | LangChain abstraction |
| Level | Model level | Framework level |
| How it works | Model outputs structured JSON | LangChain wraps and executes it |

> Function Calling = Model capability | Tool = LangChain wrapper around that capability

---

## Tool and Agent Relationship

```
Agent = Decision Maker
Tool  = Action Executor
```

The **Agent**:
- Decides which tool to use
- Decides when to use it
- Decides how many times to use it
- Stops when the task is complete

| Without Agent | With Agent |
|--------------|-----------|
| You must manually call tools | LLM automatically manages tool usage |
| Single, pre-defined calls | Dynamic, multi-step tool usage |

> See [Agent Notes](../Mini_projects/agent_notes.md) for how agents orchestrate tools.

---

## Tools in RAG Systems

In a RAG system, possible tools include:

- Document loader
- Retriever
- Vector database query
- Summarization module

**Example use case:**
```
User: "Summarize this YouTube video"

Agent:
  Step 1: Call transcript loader tool
  Step 2: Call retriever tool
  Step 3: Call summarization chain
  → Returns summary
```

---

## When to Use Tools

Use tools when:

- External information is required
- Real-time data is needed
- Accurate math is required
- API integration is needed
- Database access is required
- File system interaction is required

---

> **Key interview points:**
> - Tools extend LLM capabilities
> - Tools contain `name`, `description`, and `function`
> - Description guides LLM decision-making
> - Tools are often used with Agents
> - Tools enable real-world interaction
