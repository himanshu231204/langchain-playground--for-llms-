# 📞 Tool Calling in LangChain – Notes

> Notes on tool calling — the runtime mechanism by which an LLM generates structured requests to execute external functions.

## Table of Contents

- [What is Tool Calling?](#what-is-tool-calling)
- [Why Tool Calling is Needed?](#why-tool-calling-is-needed)
- [How Tool Calling Works](#how-tool-calling-works)
- [Important Concept](#important-concept)
- [What a Tool Call Contains](#what-a-tool-call-contains)
- [Models That Support Tool Calling](#models-that-support-tool-calling)
- [Tool Calling vs Tool Binding vs Agents](#tool-calling-vs-tool-binding-vs-agents)
- [Advantages](#advantages)

## Related Notes

- [Tools Overview](tools.md)
- [Tool Binding](tool_binding.md)
- [Custom Tools](custom_tools.md)
- [Toolkits](toolkit.md)
- [Agent Notes](../Mini_projects/agent_notes.md)

---

## What is Tool Calling?

**Tool Calling** is the process where a Language Model (LLM) **decides to call an external tool** instead of generating a direct text response.

> **Simple definition:** Tool Calling = The ability of an LLM to generate structured requests to execute external functions (tools).

---

## Why Tool Calling is Needed?

LLMs alone can:
- Generate text
- Answer questions
- Explain concepts

But they cannot:
- Fetch real-time data
- Perform accurate calculations
- Query databases
- Call APIs
- Execute code

Tool calling allows the LLM to perform these real-world actions.

---

## How Tool Calling Works

```
Step 1: User asks a question
Step 2: LLM analyzes the request
Step 3: LLM decides that a tool is required
Step 4: LLM outputs a structured tool call (JSON format)
Step 5: Application executes the tool
Step 6: Tool result is sent back to the LLM
Step 7: LLM generates final natural language answer
```

---

## Important Concept

When tool calling is enabled, the model may return:

```python
response.content = ""          # empty — no direct text answer
response.tool_calls = [...]    # structured tool call request
```

> ⚠️ **This does NOT mean the model failed.** It means the model wants a tool to be executed first before it can answer.

This is normal and expected behavior when the model determines a tool is needed.

---

## What a Tool Call Contains

A tool call includes:

```python
{
    "name": "add_numbers",         # Tool to call
    "args": {"a": 2, "b": 3},     # Arguments for the tool
    "id": "call_abc123",           # Unique identifier
    "type": "tool_call"
}
```

---

## Models That Support Tool Calling

Tool calling works only if the model supports **function calling** and can output structured JSON:

| Model | Supports Tool Calling |
|-------|----------------------|
| GPT-4o | ✅ |
| Claude 3.5 | ✅ |
| Gemini 1.5 | ✅ |
| Qwen (tools version) | ✅ |
| Ollama (some models) | ⚠️ Depends on model |

---

## Tool Calling vs Tool Binding vs Agents

| Concept | What it is | When it happens |
|---------|-----------|----------------|
| **Tool** | A callable function | Defined before runtime |
| **Tool Binding** | Attaching tools to LLM | Setup phase |
| **Tool Calling** | LLM generating a tool call request | **At runtime** |
| **Agent** | Multi-step tool calling loop | Complex workflows |

### Flow relationship

```
Tool (defined)
    │
Tool Binding (attached to LLM)
    │
Tool Calling (LLM decides to use it at runtime)
    │
Agent (orchestrates multiple tool calls)
```

---

## Advantages

- ✅ Extends LLM capability
- ✅ Enables real-time interaction
- ✅ Improves accuracy (uses actual tools for math, data, etc.)
- ✅ Allows automation
- ✅ Production-ready architecture

---

> **Interview definition:** Tool calling is the capability of a language model to generate structured function requests that allow external tools to be executed during response generation.
