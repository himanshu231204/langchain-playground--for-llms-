# 🔗 Tool Binding in LangChain – Notes

> Notes on tool binding — attaching tools to an LLM to enable automatic function calling.

## Table of Contents

- [What is Tool Binding?](#what-is-tool-binding)
- [Why is Tool Binding Needed?](#why-is-tool-binding-needed)
- [How Tool Binding Works](#how-tool-binding-works)
- [Usage in LangChain](#usage-in-langchain)
- [Tool Binding vs Agent](#tool-binding-vs-agent)
- [When to Use Tool Binding](#when-to-use-tool-binding)
- [Advantages](#advantages)

## Related Notes

- [Tools Overview](tools.md)
- [Tool Calling](tools_calling%20.md)
- [Custom Tools](custom_tools.md)
- [Toolkits](toolkit.md)
- [Agent Notes](../Mini_projects/agent_notes.md)

---

## What is Tool Binding?

**Tool Binding** is the process of attaching tools to a Language Model (LLM) so that the model can **call those tools automatically** when needed.

> **Simple definition:** Tool Binding = Connecting tools to an LLM to enable function calling.

---

## Why is Tool Binding Needed?

Normally, an LLM:
- Only generates text
- Cannot perform real-world actions

After tool binding, the LLM can:
- Perform calculations
- Search the web
- Query databases
- Call APIs
- Execute custom logic

It extends the capability of the LLM beyond text generation.

---

## How Tool Binding Works

```
User Query
    │
    ▼
LLM analyzes the request
    │
    ▼
LLM decides if a tool is required
    │
    ▼ (if yes)
LLM generates a structured tool call
    │
    ▼
Tool executes
    │
    ▼
Result returned to LLM
    │
    ▼
LLM generates final response
```

**Internal mechanics:**

1. Tools are converted into **function schemas** (JSON)
2. Schemas are sent to the LLM
3. LLM outputs structured JSON tool calls
4. LangChain executes the tool automatically

---

## Usage in LangChain

```python
from langchain_ollama import ChatOllama
from langchain_core.tools import tool

@tool
def add_numbers(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

@tool
def get_weather(city: str) -> str:
    """Get current weather for a city."""
    return f"The weather in {city} is sunny, 25°C"

llm = ChatOllama(model="llama3")

# Bind tools to the LLM
llm_with_tools = llm.bind_tools([add_numbers, get_weather])

# Now the LLM can automatically call these tools
response = llm_with_tools.invoke("What is 5 + 3?")
```

After binding, the LLM:
- Is aware of available tools
- Can generate tool calls automatically

---

## Tool Binding vs Agent

| Feature | Tool Binding | Agent |
|---------|-------------|-------|
| Reasoning loop | ❌ Single step | ✅ Multi-step |
| Complexity | Simple | Complex |
| Speed | Faster | Slower |
| Tool calls | Once | Multiple times |
| Use case | Simple function calling | Complex workflows |

> Use Tool Binding for lightweight, single-step function calling. Use Agents for multi-step reasoning.
>
> See [Agent Notes](../Mini_projects/agent_notes.md) for agent patterns.

---

## When to Use Tool Binding

Use tool binding when:

- ✅ You need simple tool usage
- ✅ No complex reasoning loop required
- ✅ Single-step function calling is enough
- ✅ You want lightweight architecture
- ✅ Building production APIs with specific tool calls

---

## Advantages

- ✅ Simple architecture
- ✅ Fast execution
- ✅ Lower overhead than agents
- ✅ Easy to implement
- ✅ Good for production APIs

---

> **Interview definition:** Tool binding is the process of attaching tools to an LLM so that it can automatically call those tools using function-calling capabilities during response generation.
