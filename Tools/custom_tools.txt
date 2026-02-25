=========================================
CUSTOM TOOLS IN LANGCHAIN - COMPLETE NOTES
=========================================

1) What is a Custom Tool?

A Custom Tool in LangChain is a user-defined function that an LLM (through an Agent)
can call to perform a specific task.

Unlike built-in tools, custom tools are created by the developer
to solve application-specific problems.

Definition:
Custom Tool = A developer-defined function wrapped in a tool interface
that allows an LLM to perform external actions.

------------------------------------------------

2) Why Do We Need Custom Tools?

Built-in tools are limited.
Real-world applications require specific logic such as:

- Calling a private API
- Querying a custom database
- Reading internal files
- Performing business logic
- Interacting with company systems
- Triggering automation workflows

Custom tools allow full flexibility.

------------------------------------------------

3) Basic Structure of a Custom Tool

A custom tool typically includes:

- name → Unique identifier
- description → Explains when the tool should be used
- function → The actual Python function logic

Important:
The description is critical because the LLM reads it
to decide whether to use the tool.

------------------------------------------------

4) How Custom Tool Works (Execution Flow)

User Query
    ↓
Agent analyzes the request
    ↓
If description matches, Agent selects the tool
    ↓
Tool function executes
    ↓
Output returned to LLM
    ↓
LLM generates final answer

------------------------------------------------

5) Methods to Create Custom Tools in LangChain

A) Using @tool decorator
   - Simple and recommended method

B) Using Tool class manually
   - More control over configuration

C) StructuredTool (for multiple arguments)
   - Used when function requires structured inputs

------------------------------------------------

6) Simple Example (Conceptual)

Suppose we create a custom weather tool.

Function:
- Takes city name
- Returns temperature

Tool Name: get_weather
Description:
"Use this tool to get current weather information for a city."

When user asks:
"What is the weather in Delhi?"

Agent:
- Detects weather request
- Calls get_weather tool
- Returns result

------------------------------------------------

7) Custom Tool vs Built-in Tool

Built-in Tool:
- Predefined by LangChain
- Limited to available integrations

Custom Tool:
- Created by developer
- Unlimited flexibility
- Can connect to any API or logic

------------------------------------------------

8) Custom Tool vs Chain

Chain:
- Fixed execution steps
- Predefined workflow

Custom Tool:
- Dynamically used by Agent
- Called only when required

Chain = Static logic
Tool = Dynamic callable capability

------------------------------------------------

9) When to Use Custom Tools?

Use custom tools when:

- You need private API integration
- You want database access
- You want business rule execution
- You need file system operations
- You want automation triggers
- You want domain-specific functionality

------------------------------------------------

10) Structured Custom Tools

If a function needs multiple inputs,
StructuredTool is used.

Example:
Function requires:
- source_city
- destination_city
- travel_date

StructuredTool allows proper schema validation.

------------------------------------------------

11) Important Design Guidelines

- Keep function logic clean and modular
- Write clear and specific descriptions
- Avoid very long descriptions
- Handle exceptions inside the tool
- Validate input properly
- Avoid dangerous system-level actions

------------------------------------------------

12) Security Considerations

Custom tools can:

- Access databases
- Modify files
- Execute commands
- Trigger external services

So:
- Always validate inputs
- Use authentication where needed
- Restrict sensitive operations
- Prefer sandbox environments

------------------------------------------------

13) Interview Key Points

- Custom tools extend LLM capability.
- They are user-defined functions wrapped as tools.
- Description guides LLM decision-making.
- Tools are mainly used with Agents.
- StructuredTool is used for multi-argument functions.
- Custom tools enable real-world integration.

------------------------------------------------

14) Real-World Use Cases

- Chatbot with internal company database access
- AI assistant that books tickets
- Code execution assistant
- Automated DevOps agent
- Financial analysis assistant
- RAG system with custom retrieval logic

------------------------------------------------

END OF NOTES
=========================================