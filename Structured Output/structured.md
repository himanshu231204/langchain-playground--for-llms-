When to use TypedDict / Pydantic / JSON Schema

Use TypedDict if:
- You only need type hints (basic structure enforcement).
- You trust the data source and don’t need runtime validation.
- Your usage is internal and you’re fine relying on static checking.

Use Pydantic if:
- You receive external or untrusted data (e.g., JSON from APIs).
- You need runtime validation, default values, automatic type conversion (“100” → 100).
- You want nested models, field constraints, serialization to JSON/dict.

Use JSON Schema if:
- You need a schema in standard JSON format (for APIs, external contracts).
- You may not want to import extra Python-library dependencies.
- You need validation of raw JSON data across multiple environments and want a portable spec.

Quick Decision Guide:
- Trust your data & internal use → TypedDict
- External data & need validation/conversion → Pydantic
- Schema for external systems/JSON interchange → JSON Schema
