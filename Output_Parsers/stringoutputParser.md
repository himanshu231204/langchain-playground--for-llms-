# 📝 StrOutputParser – Notes

> Notes on the `StrOutputParser` — LangChain's simplest output parser for extracting plain text from LLM responses.

## Table of Contents

- [What is StrOutputParser?](#what-is-stroutputparser)
- [Why Do We Need It?](#why-do-we-need-it)
- [How It Works](#how-it-works)
- [Usage Example](#usage-example)
- [Role in Multi-Step Chains](#role-in-multi-step-chains)
- [Limitations](#limitations)
- [Comparison with Other Parsers](#comparison-with-other-parsers)

## Related Notes

- [Output Parsers Overview](notes1.md)
- [JSON Output Parser](jsonoutput_parser.md)
- [Pydantic Output Parser](PydanticOutputParser.md)
- [Structured Output Parser](Structured%20Output%20Parser.md)
- [Chains Overview](../Chain/chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## What is StrOutputParser?

`StrOutputParser` is an **output parser** in LangChain that converts an LLM's response into a **plain Python string**.

> **One-line definition:** `StrOutputParser` converts the LLM response into a plain string for easy reuse and chaining.

---

## Why Do We Need It?

LLMs usually return outputs as `AIMessage`, `ChatMessage`, or other structured objects. In most pipelines, we want:

- Clean text
- Easy chaining
- Direct string manipulation

`StrOutputParser` extracts **only the text content**.

Without `StrOutputParser`, LLM output:
- Is harder to reuse
- Cannot be directly passed to the next prompt
- May break LCEL chains due to type mismatch

---

## How It Works

Internally it:
1. Takes the **LLM response object**
2. Extracts `.content` from it
3. Returns it as a **plain string**

---

## Usage Example

```python
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")
parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "{question}")
])

chain = prompt | llm | parser

result = chain.invoke({"question": "What is LangChain?"})
print(result)  # → "This is the generated answer"
print(type(result))  # → <class 'str'>
```

---

## Role in Multi-Step Chains

```
PromptTemplate → LLM → StrOutputParser → String
                                          │
                                          ▼
                                    Next PromptTemplate
```

This allows:
- Reuse of output in the next step
- Passing text to another prompt
- Storing results in variables or databases

In multi-step pipelines:
1. Step 1 LLM generates text → `StrOutputParser` extracts string
2. Step 2 prompt receives that string as input
3. Without it → **type mismatch errors**

---

## Limitations

- Returns **only plain text** — cannot enforce structure
- No validation of output content

For structured output, use:
- [`JsonOutputParser`](jsonoutput_parser.md) — for dictionary output
- [`PydanticOutputParser`](PydanticOutputParser.md) — for schema-validated output

---

## Comparison with Other Parsers

| Parser | Output Type | Validation | Use Case |
|--------|-------------|------------|----------|
| `StrOutputParser` | `str` | ❌ | Simple text, chaining |
| `JsonOutputParser` | `dict` | ⚠️ Partial | Structured data |
| `PydanticOutputParser` | Pydantic object | ✅ | Schema-validated data |

### Key Rules

- **LLM output** → object (`AIMessage`)
- **StrOutputParser** → string
- **PromptTemplate** → requires dictionary

> **Memory trick:** Text needed → `StrOutputParser`; Structure needed → `JsonOutputParser` or `PydanticOutputParser`
