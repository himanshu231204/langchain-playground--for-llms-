# 🔀 Conditional Chain in LangChain

> Notes on implementing IF/ELSE routing in LLM pipelines using `RunnableBranch`.

## Table of Contents

- [Definition](#definition)
- [Core Idea](#core-idea)
- [Why Conditional Chains Are Needed](#why-conditional-chains-are-needed)
- [Architecture](#architecture)
- [Example: Feedback Processing](#example-feedback-processing)
- [Key Components in LangChain](#key-components-in-langchain)
- [Lessons Learned from Common Errors](#lessons-learned-from-common-errors)
- [Conditional vs Sequential Chain](#conditional-vs-sequential-chain)
- [Relation to Agents](#relation-to-agents)

## Related Notes

- [Simple & Sequential Chain](chain.md)
- [Parallel Chain](parallel_chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)
- [Output Parsers](../Output_Parsers/notes1.md)
- [Pydantic Output Parser](../Output_Parsers/PydanticOutputParser.md)

---

## Definition

A **Conditional Chain** is a workflow pattern in which different processing paths (chains) are executed based on a condition or decision made at runtime.

It is similar to **IF–ELSE logic** in traditional programming, but applied to LLM-based pipelines.

> **Interview one-liner:** A Conditional Chain dynamically selects which LLM chain to execute based on runtime conditions, enabling flexible and decision-driven AI workflows.

---

## Core Idea

```
Input → Condition Check → Selected Chain → Output
```

The condition can be:
- A simple rule (keyword, regex, length)
- The output of an LLM (classification, intent detection)
- External signals (API response, database value)

---

## Why Conditional Chains Are Needed

- Avoid running unnecessary chains
- Reduce cost and latency
- Handle multiple user intents in one system
- Build intelligent and flexible AI workflows

---

## Architecture

```
User Input
   │
   ▼
Classifier / Condition Logic
   │
   ├──▶ Chain 1 (Action A)
   │
   └──▶ Chain 2 (Action B)
```

---

## Example: Feedback Processing

**Use case:** Route user feedback based on sentiment

```
Input: User Feedback
Condition: Is feedback Positive or Negative?

IF Positive:
  → Save feedback
  → Send acknowledgment

ELSE (Negative):
  → Raise complaint
  → Notify support team
```

---

## Key Components in LangChain

| Component | Role |
|-----------|------|
| `PromptTemplate` | Frames input for the LLM |
| `ChatOllama` / LLM | Generates classification or content |
| `PydanticOutputParser` | Converts LLM output into typed object |
| `RunnableLambda` | Transforms/maps data between steps |
| `RunnableBranch` | Routes execution based on conditions |

### Correct Design Pattern

```
Classifier Chain
  → RunnableLambda  (mapping step)
  → RunnableBranch  (IF–ELSE routing)
  → Action Chains
```

---

## Lessons Learned from Common Errors

### 1. Structured Output vs Branch Input

- `PydanticOutputParser` returns a typed **object** (not a dictionary)
- `RunnableBranch` conditions expect **dictionary-like** inputs

✅ **Fix:** Always insert a `RunnableLambda` mapping step to convert structured objects into routing dictionaries.

### 2. Why `classifier_chain | branch_chain` Can Fail

- Classifier output = Pydantic object
- Branch expects keys like `"sentiment"`

✅ **Fix:** Never directly pipe a structured output into `RunnableBranch`.

### 3. Feedback Must Be Passed Explicitly

- Branch action prompts require `{feedback}`
- Classifier output does **not** automatically carry the original input

✅ **Fix:** Always forward required fields explicitly through the pipeline.

### 4. Literal Validation Errors Are Not Bugs

- Real-world feedback can be mixed (positive + negative)
- Pydantic `Literal` validation fails if output is outside allowed values

✅ **Fix:** Define clear business rules (e.g., "any complaint = negative").

### 5. LLM Output Is Probabilistic

- LLM may return unexpected labels (e.g., `"mixed"`)

✅ **Fix:** Use strict prompts and fallback logic to constrain outputs.

---

## Conditional vs Sequential Chain

| Feature | Sequential Chain | Conditional Chain |
|---------|-----------------|-------------------|
| Execution order | Fixed | Dynamic |
| Steps executed | All steps always run | Only one branch runs |
| Example | Step1 → Step2 → Step3 | IF–ELSE routing |
| Efficiency | Lower (all steps) | Higher (only needed branch) |

> Conditional Chains are more efficient and cost-aware than Sequential Chains.

---

## Relation to Agents

An **AI Agent** can be considered an advanced form of a Conditional Chain where:

- Conditions are more complex
- Tool selection is dynamic
- Multiple decisions are made iteratively

> See [Agent Notes](../Mini_projects/agent_notes.md) for more on agents.

---

## Advantages

- ✅ Efficient use of LLM calls
- ✅ Scalable design
- ✅ Better user experience
- ✅ Easy to extend with new conditions

## Limitations

- ⚠️ More complex logic than linear chains
- ⚠️ Poorly designed conditions can increase LLM calls
- ⚠️ Requires careful prompt design

---

> **Final takeaway:** Most Conditional Chain errors are **wiring errors**, not logic errors. Correct data flow and explicit mappings are more important than complex prompts.
