# 🧰 Toolkits in LangChain – Notes

> Notes on toolkits — structured collections of related tools for domain-specific interactions.

## Table of Contents

- [What is a Toolkit?](#what-is-a-toolkit)
- [Why Do We Need Toolkits?](#why-do-we-need-toolkits)
- [Toolkit vs Tool](#toolkit-vs-tool)
- [What Does a Toolkit Contain?](#what-does-a-toolkit-contain)
- [How Toolkit Works with Agents](#how-toolkit-works-with-agents)
- [Common Toolkits in LangChain](#common-toolkits-in-langchain)
- [When to Use a Toolkit](#when-to-use-a-toolkit)
- [Advantages](#advantages)

## Related Notes

- [Tools Overview](tools.md)
- [Tool Binding](tool_binding.md)
- [Tool Calling](tools_calling%20.md)
- [Custom Tools](custom_tools.md)
- [Agent Notes](../Mini_projects/agent_notes.md)

---

## What is a Toolkit?

A **Toolkit** in LangChain is a **collection (group) of related tools** that are designed to work together for a specific purpose.

> **Simple definition:** Toolkit = A structured bundle of multiple related tools.

---

## Why Do We Need Toolkits?

In real-world applications, one tool is usually not enough.

**Example:** If you want database interaction, you may need:
- Query tool
- List tables tool
- Get schema tool
- Insert data tool

Instead of creating each tool manually, LangChain provides them grouped as a **Toolkit**.

---

## Toolkit vs Tool

| | Tool | Toolkit |
|-|------|---------|
| Scope | Single function | Collection of multiple tools |
| Purpose | One specific task | A domain or system |
| Example | `search` tool | Full Database Toolkit (query + schema + table listing) |
| Usage | Used directly | Provides tools via `get_tools()` |

---

## What Does a Toolkit Contain?

A Toolkit typically contains:

- Multiple `Tool` objects
- Configuration logic
- Helper methods
- Environment integration

It provides a method like `get_tools()` that returns the list of tools inside:

```python
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tools = toolkit.get_tools()
# → [list_tables_tool, get_schema_tool, run_query_tool, ...]
```

---

## How Toolkit Works with Agents

```
User Query
    │
    ▼
Agent receives toolkit tools via get_tools()
    │
    ▼
Agent selects appropriate tool from toolkit
    │
    ▼
Tool executes
    │
    ▼
Final answer generated
```

> ⚠️ The Agent does **not** know about "toolkit" as a concept. It only receives the flat list of tools from `get_tools()`.

---

## Common Toolkits in LangChain

| Toolkit | Purpose |
|---------|---------|
| `SQLDatabaseToolkit` | Interact with SQL databases |
| `PythonToolkit` | Execute Python code |
| `FileManagementToolkit` | File system operations |
| `GitHubToolkit` | Interact with GitHub repositories |
| `OpenAPIToolkit` | Call REST APIs from OpenAPI spec |

### SQL Toolkit Example

The `SQLDatabaseToolkit` may include:

```
- list_tables_tool     → Lists all tables
- get_schema_tool      → Gets table schema
- run_query_tool       → Executes SQL queries
```

Instead of manually building these, the toolkit prepares them automatically.

---

## When to Use a Toolkit

Use a Toolkit when:

- ✅ You are working with **complex systems** (databases, APIs, file systems)
- ✅ Multiple related tools are needed
- ✅ You want **structured integration**
- ✅ You want **production-level design**
- ✅ You want **clean modular architecture**

Use [Custom Tools](custom_tools.md) when you need to build application-specific one-off tools.

---

## Advantages

- ✅ Cleaner architecture
- ✅ Modular design
- ✅ Reusability
- ✅ Faster development
- ✅ Domain specialization
- ✅ Production-ready patterns

---

> **Interview definition:** A Toolkit in LangChain is a structured collection of related tools that work together to enable domain-specific interactions such as databases, files, APIs, or code execution.
