# 💬 Chat History in LangChain

> Notes and examples on managing chat message history using LangChain message types.

## Table of Contents

- [Overview](#overview)
- [Chat Message Types](#chat-message-types)
- [Building Chat History](#building-chat-history)
- [Example](#example)

## Related Notes

- [Core Concepts & Prompts](../notes.md)
- [Chains Overview](../Chain/chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## Overview

In LangChain, a **chat history** is a list of structured messages passed to the model to maintain conversational context across multiple turns. It uses three core message types: `SystemMessage`, `HumanMessage`, and `AIMessage`.

---

## Chat Message Types

| Type | Role | Purpose |
|------|------|---------|
| `SystemMessage` | AI setup / instructions | Sets the tone, role, and behavior of the model |
| `HumanMessage` | User input | The question or instruction from the user |
| `AIMessage` | Model response | The AI's reply, stored for context continuity |

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
```

---

## Building Chat History

Chat history is maintained as a **list of messages** that grows with each conversation turn:

```python
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi!"),
    AIMessage(content="Hello! How can I help you today?"),
    HumanMessage(content="I want to request a refund for my order #12345."),
    AIMessage(content="Your refund request for order #12345 has been initiated. It will be processed in 3-5 business days.")
]
```

Each new user input and AI reply is **appended** to this list, allowing the model to remember previous context.

---

## Example

```python
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")

chat_history = [
    SystemMessage(content="You are a helpful customer support assistant."),
    HumanMessage(content="I want to request a refund for my order #12345."),
]

response = llm.invoke(chat_history)
chat_history.append(AIMessage(content=response.content))

print(response.content)
```

> **Tip:** Together, these message types make conversations context-aware and help the AI respond more naturally across multiple turns.
