# 🗂️ JsonOutputParser – Notes

> Notes on the `JsonOutputParser` — forces LLMs to respond in structured JSON (Python dict) format.

## Table of Contents

- [What is JsonOutputParser?](#what-is-jsonoutputparser)
- [Why Do We Need It?](#why-do-we-need-it)
- [How It Works](#how-it-works)
- [Usage Example](#usage-example)
- [Common Use Cases](#common-use-cases)
- [Limitations](#limitations)
- [Comparison with Other Parsers](#comparison-with-other-parsers)

## Related Notes

- [Output Parsers Overview](notes1.md)
- [String Output Parser](stringoutputParser.md)
- [Pydantic Output Parser](PydanticOutputParser.md)
- [Structured Output Parser](Structured%20Output%20Parser.md)
- [Structured Output Guide](../Structured%20Output/structured.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## What is JsonOutputParser?

`JsonOutputParser` is an **output parser** in LangChain that converts an LLM's response into a **Python dictionary (JSON format)**.

> **One-line definition:** `JsonOutputParser` converts LLM output into structured JSON (Python dict) based on format instructions.

---

## Why Do We Need It?

LLMs naturally return **free-form text** which:

- Is hard to validate
- Is error-prone for automation
- Cannot be reliably parsed downstream

`JsonOutputParser` ensures:

- Predictable structure
- Consistent keys
- Easier downstream processing

---

## How It Works

1. Parser defines the **expected JSON format**
2. Prompt is automatically augmented with format instructions
3. LLM generates output in JSON
4. Parser converts it into a **Python dict**

> ⚠️ **Common mistake:** Forgetting to include `parser.get_format_instructions()` in the prompt. Without it → model returns random text → parser fails.

---

## Usage Example

```python
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")
parser = JsonOutputParser()

prompt = PromptTemplate(
    template="Explain {topic}.\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

chain = prompt | llm | parser

result = chain.invoke({"topic": "Black Holes"})
# → {"summary": "...", "keywords": ["black hole", "gravity"]}
print(type(result))  # → <class 'dict'>
```

---

## Common Use Cases

| Use Case | Expected Output |
|----------|----------------|
| Resume parsing | `{name, skills, experience}` |
| QA systems | `{answer, confidence}` |
| Summaries | `{summary, key_points}` |
| Agents | tool input/output |
| Eligibility bots | `{eligible: true, reason: "..."}` |

---

## Limitations

- ❌ **No strict schema validation** — model may hallucinate keys
- ❌ Model must follow format instructions strictly

For **strict validation**, use:
👉 [`PydanticOutputParser`](PydanticOutputParser.md)

---

## Comparison with Other Parsers

| Parser | Output | Validation | Use Case |
|--------|--------|------------|----------|
| `StrOutputParser` | `str` | ❌ | Simple text |
| `JsonOutputParser` | `dict` | ⚠️ Partial | Automation, APIs |
| `StructuredOutputParser` | `dict` | ❌ | Fixed fields |
| `PydanticOutputParser` | Pydantic object | ✅ | Production |

### Key Rules

- **LLM → text**
- **JsonOutputParser → dict**
- **Prompt must include format instructions**

> **Memory trick:** Structure needed → `JsonOutputParser`; Strict type safety needed → `PydanticOutputParser`
