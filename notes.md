# 🧠 LangChain Core Concepts – Notes

> Core reference notes covering Chat Models, Prompts, and Chat Messages in LangChain.

## Table of Contents

- [Chat Model Parameters](#chat-model-parameters)
- [Prompts in LangChain](#prompts-in-langchain)
- [Chat Message Types](#chat-message-types)
- [ChatPromptTemplate](#chatprompttemplate)
- [Message Placeholders](#message-placeholders)

## Related Notes

- [Chat History](Messages/chat_history.md)
- [Chains Overview](Chain/chain.md)
- [Runnables (LCEL)](Runnables/Runnables.md)
- [Output Parsers](Output_Parsers/notes1.md)

---

## Chat Model Parameters

### Gemini (and other LLMs)

| Parameter | Description |
|-----------|-------------|
| `temperature` | Controls creativity: `0` = factual, `1+` = creative |
| `max_completion_tokens` | Limits output length (number of tokens) |

- ✅ Low temperature → accurate and deterministic responses  
- ✅ High temperature → imaginative and varied responses  
- ✅ More tokens → longer replies  

---

## Prompts in LangChain

**Prompts** are input instructions given to LLMs. They define what the model should respond to and how.

Prompts can be **static** or **dynamic**.

### 📘 Static Prompts

Fixed, unchanging text sent to the model.

```text
"Explain photosynthesis in simple terms."
```

- ✅ Simple and consistent  
- ❌ Not flexible for user input  

### ⚙️ Dynamic Prompts

Use placeholders filled at runtime.

```text
"Explain {topic} in simple terms."
```

- ✅ Flexible and reusable  
- ❌ Requires correct variable formatting  

### 🧩 Usage in LangChain

- Managed with `PromptTemplate` or `ChatPromptTemplate`
- Often used in [chains](Chain/chain.md) or retrieval ([RAG](Rag%20Components/rag_notes.md)) setups
- Supports combining system (static) + user (dynamic) prompts

---

## Chat Message Types

In a chat-based AI system (like Gemini or OpenAI), every message belongs to one of three main types.

| Message Type | Represents | Purpose | Example |
|--------------|------------|---------|---------|
| `SystemMessage` | AI setup / role | Defines behavior | `"You are a helpful assistant."` |
| `HumanMessage` | User input | Captures query | `"Explain AIMessage."` |
| `AIMessage` | Model output | Returns response | `"AIMessage stores model replies."` |

### 1️⃣ SystemMessage

Defines the role, behavior, or context of the AI — like an instruction manual before the conversation starts.

```python
SystemMessage(content="You are a helpful AI assistant.")
```

Used for setting tone, controlling response style, and maintaining consistent behavior.

### 2️⃣ HumanMessage

Represents what the user inputs during the chat.

```python
HumanMessage(content="Explain how chat history works in GenAI.")
```

### 3️⃣ AIMessage

Stores the model's reply, appended to the conversation for context continuity.

```python
AIMessage(content="Chat history helps the model remember previous context...")
```

### 🔁 How They Work Together

```python
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi!"),
    AIMessage(content="Hello! How can I help you today?")
]
```

Each new user input and AI reply is appended to this list, allowing the model to remember context across turns.

> See [chat_history.md](Messages/chat_history.md) for a practical example.

---

## ChatPromptTemplate

`ChatPromptTemplate` creates **dynamic messages** — reusable templates with placeholders filled automatically at runtime.

```python
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain the topic: {topic}")
])

messages = prompt.format_messages(topic="Neural Networks")
```

**Output:**
```
System: "You are a helpful assistant."
Human:  "Explain the topic: Neural Networks"
```

**Why it matters:**

- Makes your chatbot flexible and reusable
- Avoids hardcoding text in multiple places
- Allows easy personalization (name, task, topic)
- Integrates with dynamic user inputs or app data

> `ChatPromptTemplate` = **Dynamic message generator**

---

## Message Placeholders

A **message placeholder** is a variable inside a `ChatPromptTemplate` written inside curly braces `{ }`. It gets replaced with real data when the prompt is formatted.

### Example

```python
from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "Explain the concept of {subject}.")
])

messages = prompt.format_messages(subject="Machine Learning")
```

**Output:**
```
System: "You are a helpful AI assistant."
Human:  "Explain the concept of Machine Learning."
```

### Multiple Placeholders

```python
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful tutor."),
    ("human", "Hi {name}, can you explain {concept}?")
])

messages = prompt.format_messages(name="Himanshu", concept="AI Chatbots")
# → Human: "Hi Himanshu, can you explain AI Chatbots?"
```

**Key points:**

- Placeholders are written as `{variable_name}`
- Filled when you call `.format_messages()`
- Multiple placeholders can exist in one template

> **Summary:** Message placeholders = variables inside templates that make prompts flexible, reusable, and dynamic.
