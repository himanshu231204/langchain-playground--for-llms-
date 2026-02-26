=========================================
TOOL CALLING IN LANGCHAIN - REVISION NOTES
=========================================

1) What is Tool Calling?

Tool Calling is the process where a Language Model (LLM)
decides to call an external tool instead of generating
a direct text response.

Simple Definition:
Tool Calling = The ability of an LLM to generate structured
requests to execute external functions (tools).

------------------------------------------------

2) Why Tool Calling is Needed?

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

Tool calling allows the LLM to perform real-world actions.

------------------------------------------------

3) How Tool Calling Works (High-Level Flow)

Step 1: User asks a question
Step 2: LLM analyzes the request
Step 3: LLM decides that a tool is required
Step 4: LLM outputs a structured tool call (JSON format)
Step 5: Application executes the tool
Step 6: Tool result is sent back to LLM
Step 7: LLM generates final natural language answer

------------------------------------------------

4) Important Concept

When tool calling is enabled:

The model may return:
- content = "" (empty text)
- tool_calls = [ ... ]

This means:
The model wants tools to be executed first.

It does NOT mean the model failed.

------------------------------------------------

5) Tool Calling vs Tool Binding

Tool:
- A callable function

Tool Binding:
- Attaching tools to an LLM

Tool Calling:
- The actual runtime decision where the LLM
  generates a structured request to use a tool

------------------------------------------------

6) Tool Calling vs Agents

Tool Calling:
- Single-step execution
- Model outputs tool request once
- No reasoning loop

Agent:
- Multi-step reasoning
- Can call tools multiple times
- Has iterative decision process

Tool calling is simpler than agents.

------------------------------------------------

7) What Does a Tool Call Contain?

A tool call usually includes:

- name → Tool name
- args → Arguments for the tool
- id → Unique identifier
- type → "tool_call"

Example structure:

{
  "name": "add_numbers",
  "args": {"a": 2, "b": 3}
}

------------------------------------------------

8) Models That Support Tool Calling

Tool calling works only if the model supports:
- Function calling
- Structured JSON output
- Tool schemas

Examples:
- GPT-4o
- Claude 3.5
- Gemini 1.5
- Qwen 3.5 (tools version)

------------------------------------------------

9) Advantages of Tool Calling

- Extends LLM capability
- Enables real-time interaction
- Improves accuracy
- Allows automation
- Production-ready architecture

------------------------------------------------

10) Interview Definition

“Tool calling is the capability of a language model
to generate structured function requests that allow
external tools to be executed during response generation.”

------------------------------------------------

END OF NOTES
=========================================