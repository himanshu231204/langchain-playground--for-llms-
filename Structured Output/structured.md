# 🏗️ Structured Output – TypedDict vs Pydantic vs JSON Schema

> A decision guide for choosing the right structured output approach in LangChain and Python applications.

## Table of Contents

- [Overview](#overview)
- [TypedDict](#typeddict)
- [Pydantic](#pydantic)
- [JSON Schema](#json-schema)
- [Quick Decision Guide](#quick-decision-guide)
- [Comparison Table](#comparison-table)

## Related Notes

- [Pydantic Output Parser](../Output_Parsers/PydanticOutputParser.md)
- [JSON Output Parser](../Output_Parsers/jsonoutput_parser.md)
- [Structured Output Parser](../Output_Parsers/Structured%20Output%20Parser.md)
- [Output Parsers Overview](../Output_Parsers/notes1.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## Overview

In LangChain and Python applications, there are three main approaches for defining structured output schemas:

| Approach | Library | Validation | Use Case |
|----------|---------|------------|----------|
| `TypedDict` | Python stdlib | Static only | Internal, trusted data |
| `Pydantic` | `pydantic` | ✅ Runtime | External data, APIs |
| `JSON Schema` | Standard format | Varies | External contracts |

---

## TypedDict

`TypedDict` provides **type hints** for dictionaries without runtime validation.

```python
from typing import TypedDict

class TopicOutput(TypedDict):
    topic: str
    summary: str
    difficulty: str
```

**Use TypedDict when:**

- You only need type hints (basic structure enforcement)
- You trust the data source and don't need runtime validation
- Usage is internal and you rely on static type checking

**Limitations:**

- No runtime validation
- No automatic type conversion
- No field constraints

---

## Pydantic

`Pydantic` provides **runtime validation**, automatic type conversion, and rich schema features.

```python
from pydantic import BaseModel, Field

class TopicOutput(BaseModel):
    topic: str = Field(description="The topic name")
    summary: str = Field(description="A brief explanation")
    difficulty: str = Field(description="Easy / Medium / Hard")
```

**Use Pydantic when:**

- You receive external or untrusted data (e.g., JSON from APIs)
- You need runtime validation, default values, automatic type conversion (`"100"` → `100`)
- You want nested models, field constraints, serialization to JSON/dict

**Advantages:**

- ✅ Runtime validation
- ✅ Automatic type coercion
- ✅ Rich field constraints (`min_length`, `ge`, `le`, etc.)
- ✅ `.model_dump()` for easy serialization
- ✅ Integrates directly with `PydanticOutputParser`

> See [PydanticOutputParser](../Output_Parsers/PydanticOutputParser.md) for how Pydantic integrates with LangChain output parsing.

---

## JSON Schema

**JSON Schema** is a standard, language-agnostic format for defining the structure and constraints of JSON data.

```json
{
  "type": "object",
  "properties": {
    "topic": { "type": "string" },
    "summary": { "type": "string" },
    "difficulty": { "type": "string", "enum": ["Easy", "Medium", "Hard"] }
  },
  "required": ["topic", "summary", "difficulty"]
}
```

**Use JSON Schema when:**

- You need a schema in standard JSON format (for APIs, external contracts)
- You may not want to import extra Python-library dependencies
- You need validation of raw JSON data across multiple environments or languages

---

## Quick Decision Guide

```
Is the data trusted and usage is internal?
  └─ Yes → TypedDict

Do you receive external data or need runtime validation?
  └─ Yes → Pydantic

Do you need a portable schema for external systems or APIs?
  └─ Yes → JSON Schema
```

---

## Comparison Table

| Feature | TypedDict | Pydantic | JSON Schema |
|---------|-----------|---------|-------------|
| Runtime validation | ❌ | ✅ | Varies |
| Type conversion | ❌ | ✅ | ❌ |
| Default values | ❌ | ✅ | ✅ |
| Field constraints | ❌ | ✅ | ✅ |
| Language agnostic | ❌ Python only | ❌ Python only | ✅ |
| Import required | `typing` (stdlib) | `pydantic` | None |
| LangChain integration | Limited | ✅ (`PydanticOutputParser`) | ✅ (`JsonOutputParser`) |

---

## Summary

- **TypedDict** → Type hints, internal use, trust your data
- **Pydantic** → External data, runtime safety, production use
- **JSON Schema** → Portable contracts for external systems
