# 📦 Output Parsers – Overview & Notes

> Overview of all output parsers in LangChain, including the pipe chain pattern and why Ollama is used for local development.

## Table of Contents

- [What is an Output Parser?](#what-is-an-output-parser)
- [Why Do We Need Output Parsers?](#why-do-we-need-output-parsers)
- [Types of Output Parsers](#types-of-output-parsers)
- [LangChain Pipe Chain](#langchain-pipe-chain)
- [Why Use Ollama](#why-use-ollama)

## Related Notes

- [String Output Parser](stringoutputParser.md)
- [JSON Output Parser](jsonoutput_parser.md)
- [Pydantic Output Parser](PydanticOutputParser.md)
- [Structured Output Parser](Structured%20Output%20Parser.md)
- [Structured Output Guide](../Structured%20Output/structured.md)
- [Chains Overview](../Chain/chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## What is an Output Parser?

An **Output Parser** converts raw LLM text into structured data. It ensures the AI output is clean, validated, and in the required format (JSON, dict, Pydantic object, list, etc.).

```
Raw LLM Text → Output Parser → Clean Structured Data
```

---

## Why Do We Need Output Parsers?

- LLMs return **unstructured text** by default
- Applications need **consistent and machine-readable** output
- Output Parsers prevent errors caused by incorrect formatting
- They enforce structure (like JSON) and validate data

---

## Types of Output Parsers

```
          +----------------------+
          |      User Input      |
          +----------------------+
                      │
                      ▼
          +----------------------+
          |     LLM Output       |
          |   (raw unstructured) |
          +----------------------+
                      │
                      ▼
           +----------------------+
           |    OUTPUT PARSER     |
           | (JSON/Pydantic/etc.) |
           +----------------------+
                      │
                      ▼
         +---------------------------+
         |   Clean Structured Data   |
         |  (JSON, dict, object etc) |
         +---------------------------+
```

| Parser | Output | Validation | Use Case |
|--------|--------|------------|----------|
| `StrOutputParser` | `str` | ❌ | Simple text, chaining |
| `JsonOutputParser` | `dict` | ⚠️ Partial | APIs, automation |
| `StructuredOutputParser` | `dict` | ❌ | Fixed fields |
| `PydanticOutputParser` | Pydantic object | ✅ | Production, type-safe |

### a) StrOutputParser

Returns raw text only. Use when no structure is needed.

> See [String Output Parser](stringoutputParser.md) for full notes.

### b) JsonOutputParser

Ensures the model output is valid JSON. Good for APIs, automation workflows, extraction tasks.

> See [JSON Output Parser](jsonoutput_parser.md) for full notes.

### c) PydanticOutputParser

Validates output using a Pydantic model. Best for production use cases.

> See [Pydantic Output Parser](PydanticOutputParser.md) for full notes.

### d) StructuredOutputParser

Schema-based output using `ResponseSchema`. Returns a dictionary.

> See [Structured Output Parser](Structured%20Output%20Parser.md) for full notes.

---

## LangChain Pipe Chain

```python
chain = template1 | model | parser | template2 | model | parser
```

**One-line meaning:** Output of one step → input of next step.

**Flow:**
```
Prompt → AI → Clean → New Prompt → AI → Final Clean
```

**Components:**

| Component | Role |
|-----------|------|
| `template` | Makes prompt |
| `model` | Generates answer |
| `parser` | Cleans / structures output |

**`|` (Pipe) operator:** Passes data left → right.

**Use case:** Multi-step thinking, refinement, summarization.

> **Memory trick:** Ask → Answer → Clean → Re-ask → Answer → Final

---

## Why Use Ollama

| Benefit | Description |
|---------|-------------|
| ✔ No API key | No login required |
| ✔ No billing | Zero cost |
| ✔ Works offline | Full local development |
| ✔ Open-source | Free models |
| ✔ Fast local testing | Best for learning LangChain |

> We use Ollama to run open-source LLMs locally so we can learn chains, parsers, RAG, and agents without authentication or cost issues.

**LangChain concepts ≠ Cloud models**  
**LangChain concepts = Pipelines + Logic**  
Ollama lets us focus on **logic**, not tokens.

**Comparison:**

| | HuggingFace / Gemini | Ollama |
|-|--------------------|--------|
| API key | Required | None |
| Quota | Yes | None |
| Auth | Required | None |
| Cost | Pay per use | Free |
| Control | Limited | Full |
