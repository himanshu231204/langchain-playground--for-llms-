# 🛠️ Custom Tools in LangChain – Notes

> Notes on creating custom tools — user-defined functions that extend LLM capabilities for application-specific tasks.

## Table of Contents

- [What is a Custom Tool?](#what-is-a-custom-tool)
- [Why Do We Need Custom Tools?](#why-do-we-need-custom-tools)
- [Basic Structure](#basic-structure)
- [How Custom Tool Works](#how-custom-tool-works)
- [Methods to Create Custom Tools](#methods-to-create-custom-tools)
- [Structured Custom Tools](#structured-custom-tools)
- [Design Guidelines](#design-guidelines)
- [Security Considerations](#security-considerations)
- [Custom Tool vs Built-in Tool vs Chain](#custom-tool-vs-built-in-tool-vs-chain)
- [Real-World Use Cases](#real-world-use-cases)

## Related Notes

- [Tools Overview](tools.md)
- [Tool Binding](tool_binding.md)
- [Tool Calling](tools_calling%20.md)
- [Toolkits](toolkit.md)
- [Agent Notes](../Mini_projects/agent_notes.md)

---

## What is a Custom Tool?

A **Custom Tool** in LangChain is a user-defined function that an LLM (through an Agent) can call to perform a specific task.

> **Definition:** Custom Tool = A developer-defined function wrapped in a tool interface that allows an LLM to perform external actions.

Unlike built-in tools, custom tools are created by the developer to solve application-specific problems.

---

## Why Do We Need Custom Tools?

Built-in tools are limited. Real-world applications require:

- Calling a **private API**
- Querying a **custom database**
- Reading **internal files**
- Performing **business logic**
- Interacting with **company systems**
- Triggering **automation workflows**

Custom tools allow **full flexibility**.

---

## Basic Structure

A custom tool typically includes:

| Part | Description |
|------|-------------|
| `name` | Unique identifier for the tool |
| `description` | Explains when the tool should be used (LLM reads this) |
| `function` | The actual Python function logic |

> ⚠️ **The description is critical** — the LLM reads it to decide whether to use the tool.

---

## How Custom Tool Works

```
User Query
    │
    ▼
Agent analyzes the request
    │
    ▼
If description matches, Agent selects the tool
    │
    ▼
Tool function executes
    │
    ▼
Output returned to LLM
    │
    ▼
LLM generates final answer
```

---

## Methods to Create Custom Tools

### A) Using `@tool` Decorator (Recommended)

The simplest and most Pythonic approach:

```python
from langchain_core.tools import tool

@tool
def get_weather(city: str) -> str:
    """Get current weather information for a city.
    
    Args:
        city: The name of the city to get weather for.
    """
    # Your actual implementation here
    return f"The weather in {city} is sunny, 25°C"
```

### B) Using `Tool` Class Manually

More control over configuration:

```python
from langchain_core.tools import Tool

def get_weather(city: str) -> str:
    return f"The weather in {city} is sunny, 25°C"

weather_tool = Tool(
    name="get_weather",
    func=get_weather,
    description="Use this tool to get current weather information for a city."
)
```

### C) `StructuredTool` (for Multiple Arguments)

Used when function requires structured/multiple inputs:

```python
from langchain_core.tools import StructuredTool
from pydantic import BaseModel

class FlightInput(BaseModel):
    source_city: str
    destination_city: str
    travel_date: str

def search_flights(source_city: str, destination_city: str, travel_date: str) -> str:
    return f"Found 3 flights from {source_city} to {destination_city} on {travel_date}"

flight_tool = StructuredTool.from_function(
    func=search_flights,
    name="search_flights",
    description="Search for available flights between cities.",
    args_schema=FlightInput
)
```

---

## Structured Custom Tools

Use `StructuredTool` when a function needs **multiple inputs** with proper schema validation.

**Example scenario:** A currency conversion tool needs:
- `from_currency`
- `to_currency`
- `amount`

`StructuredTool` allows the LLM to pass all three arguments correctly.

---

## Design Guidelines

- ✅ Keep function logic **clean and modular**
- ✅ Write **clear and specific** descriptions
- ✅ Avoid very long descriptions
- ✅ Handle **exceptions** inside the tool
- ✅ **Validate input** properly
- ❌ Avoid dangerous system-level actions
- ❌ Avoid ambiguous descriptions

---

## Security Considerations

Custom tools can access databases, modify files, execute commands, and trigger external services. Always:

- **Validate inputs** before processing
- **Use authentication** where needed
- **Restrict sensitive operations**
- **Prefer sandbox environments** for untrusted inputs
- **Log tool calls** for auditing

---

## Custom Tool vs Built-in Tool vs Chain

| | Built-in Tool | Custom Tool | Chain |
|-|--------------|------------|-------|
| Created by | LangChain | Developer | Developer |
| Flexibility | Limited | ✅ Unlimited | Limited to design |
| Usage pattern | Dynamic (agent-based) | Dynamic (agent-based) | Static (always runs) |
| Best for | Common tasks | App-specific logic | Fixed workflows |

---

## Real-World Use Cases

| Use Case | Example Tool |
|----------|-------------|
| Private API integration | `call_company_api(endpoint, params)` |
| Database access | `query_user_database(user_id)` |
| Business logic | `calculate_discount(product_id, user_tier)` |
| File operations | `read_report_file(filename)` |
| Automation | `trigger_ci_pipeline(repo, branch)` |
| Financial analysis | `get_stock_price(ticker)` |
| RAG retrieval | `search_knowledge_base(query)` |
