# 🗃️ Structured Output Parser – Notes

> Notes on the `StructuredOutputParser` — a schema-based parser that returns fixed-field dictionaries.

> **Note:** `StructuredOutputParser` is an older LangChain abstraction for schema-based outputs. It has largely been superseded by [`JsonOutputParser`](jsonoutput_parser.md) and [`PydanticOutputParser`](PydanticOutputParser.md) in newer versions.

## Table of Contents

- [What is Structured Output Parser?](#what-is-structured-output-parser)
- [Why Do We Need Structured Output?](#why-do-we-need-structured-output)
- [Types of Structured Output Parsers](#types-of-structured-output-parsers)
- [StructuredOutputParser: Core Concept](#structuredoutputparser-core-concept)
- [Usage Example](#usage-example)
- [When to Use It](#when-to-use-it)
- [Limitations](#limitations)
- [Comparison with Other Parsers](#comparison-with-other-parsers)

## Related Notes

- [Output Parsers Overview](notes1.md)
- [String Output Parser](stringoutputParser.md)
- [JSON Output Parser](jsonoutput_parser.md)
- [Pydantic Output Parser](PydanticOutputParser.md)
- [Structured Output Guide](../Structured%20Output/structured.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## What is Structured Output Parser?

A **Structured Output Parser** forces an LLM to return output in a **pre-defined structure** (schema) with:

- Fixed fields
- Fixed data types
- Validated output

It ensures the model output is **machine-readable and reliable**.

---

## Why Do We Need Structured Output?

Free-text output is:
- Unpredictable
- May miss fields
- May change format

Real applications (APIs, forms, agents) need:
- Consistent keys
- Correct data types
- Validation

👉 Structured Output Parsers solve this.

---

## Types of Structured Output Parsers in LangChain

| Parser | Schema Definition | Output | Validation |
|--------|-------------------|--------|------------|
| [`StructuredOutputParser`](Structured%20Output%20Parser.md) | `ResponseSchema` | `dict` | ❌ |
| [`JsonOutputParser`](jsonoutput_parser.md) | Format instructions | `dict` | ⚠️ Partial |
| [`PydanticOutputParser`](PydanticOutputParser.md) | Pydantic model | Object | ✅ |

---

## StructuredOutputParser: Core Concept

### What it does

1. Defines expected fields using `ResponseSchema`
2. Injects formatting instructions into the prompt
3. Parses LLM output into a Python dictionary

---

## Usage Example

```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama

schemas = [
    ResponseSchema(name="topic", description="Main topic"),
    ResponseSchema(name="summary", description="Short explanation"),
    ResponseSchema(name="difficulty", description="Easy / Medium / Hard"),
]

parser = StructuredOutputParser.from_response_schemas(schemas)

format_instructions = parser.get_format_instructions()

prompt = PromptTemplate(
    template="Explain {topic}\n{format_instructions}",
    input_variables=["topic"],
    partial_variables={"format_instructions": format_instructions}
)

llm = ChatOllama(model="llama3")
chain = prompt | llm | parser

result = chain.invoke({"topic": "Black Holes"})
# → {"topic": "Black Hole", "summary": "...", "difficulty": "Medium"}
print(type(result))  # → <class 'dict'>
```

---

## When to Use It

Use `StructuredOutputParser` when you need:

- Fixed fields in the output
- Consistent format without strict type validation
- Legacy LangChain compatibility

**Examples:**
- Question–answer format
- Summary + keywords
- Explanation + difficulty level
- Tool input formatting

---

## Limitations

- ❌ Does **not strictly validate data types**
- ❌ Model may still hallucinate values
- ❌ Less powerful than `PydanticOutputParser`

👉 For strict control → [`PydanticOutputParser`](PydanticOutputParser.md)

---

## Comparison with Other Parsers

| Parser | Structure | Validation | Use Case |
|--------|-----------|------------|----------|
| `StrOutputParser` | ❌ | ❌ | Simple text |
| `JsonOutputParser` | ⚠️ | ❌ | Loose JSON |
| `StructuredOutputParser` | ✅ | ❌ | Fixed fields |
| `PydanticOutputParser` | ✅ | ✅ | Production |

### Memory Trick 🧠

- **Text → `StrOutputParser`**
- **JSON → `JsonOutputParser`**
- **Fields → `StructuredOutputParser`**
- **Types → `PydanticOutputParser`**

> **One-line definition:** Structured Output Parser enforces a predefined response schema on LLM output, returning structured data as a dictionary.
