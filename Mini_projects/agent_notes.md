# 🤖 AI Agents in LangChain – Notes

> Notes on LangChain agents — LLMs that reason and use tools to complete multi-step tasks.

## Table of Contents

- [What is an Agent?](#what-is-an-agent)
- [ReAct Pattern](#react-pattern)
- [Key Components](#key-components)
- [Agent Flow](#agent-flow)
- [Creating a ReAct Agent](#creating-a-react-agent)
- [Agent vs Chain vs Tool](#agent-vs-chain-vs-tool)

## Related Notes

- [Tools Overview](../Tools/tools.md)
- [Tool Binding](../Tools/tool_binding.md)
- [Tool Calling](../Tools/tools_calling%20.md)
- [Custom Tools](../Tools/custom_tools.md)
- [Toolkits](../Tools/toolkit.md)
- [Chains Overview](../Chain/chain.md)
- [Conditional Chain](../Chain/conditional_Chain.md)
- [Runnables (LCEL)](../Runnables/Runnables.md)

---

## What is an Agent?

An **Agent** is an LLM that can use tools to reason about problems and take actions.

> **Agent = LLM + Reasoning + Tool selection**

The LLM does not just generate text — it **decides which tool to call**, **calls it**, **observes the result**, and **continues reasoning** until it reaches a final answer.

---

## ReAct Pattern

**ReAct = Reason + Act**

The ReAct pattern is the most common agent architecture. The agent follows this loop:

```
Thought  →  Action  →  Action Input  →  Observation  →  Final Answer
```

| Step | Description |
|------|-------------|
| **Thought** | The agent reasons about what to do next |
| **Action** | The agent selects a tool to call |
| **Action Input** | The argument(s) passed to the tool |
| **Observation** | The result returned by the tool |
| **Final Answer** | The agent's response after reasoning is complete |

---

## Key Components

| Component | Role |
|-----------|------|
| **LLM** | Reasons and decides which tool to use |
| **Tools** | Functions the agent can call |
| **`create_react_agent`** | Creates a ReAct-style agent with tool descriptions injected into the prompt |
| **`AgentExecutor`** | Runs the agent loop, executes tools, handles iteration, returns final response |

---

## Agent Flow

```
User Input
    │
    ▼
Agent Thinks (Reasoning)
    │
    ▼
Select Tool
    │
    ▼
Tool Execution
    │
    ▼
Observation (result)
    │
    ▼
Agent thinks again (if needed)
    │
    ▼
Final Answer
```

---

## Creating a ReAct Agent

```python
from langchain_core.tools import tool
from langchain_ollama import ChatOllama
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor

# 1. Define tools
@tool
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

tools = [add, multiply]

# 2. Initialize LLM
llm = ChatOllama(model="llama3")

# 3. Get ReAct prompt
prompt = hub.pull("hwchase17/react")

# 4. Create agent
agent = create_react_agent(llm=llm, tools=tools, prompt=prompt)

# 5. Create executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 6. Run
result = agent_executor.invoke({"input": "What is 5 + 3 multiplied by 2?"})
print(result["output"])
```

### Important Requirements for Tools

Tools used with agents **must have**:
- `name` — unique identifier
- `function` — the actual logic
- `description` — **how the agent decides which tool to use**

---

## Agent vs Chain vs Tool

| | Chain | Tool | Agent |
|-|-------|------|-------|
| Execution | Fixed steps, always runs | Single callable function | Dynamic, multi-step loop |
| Decision | None (predefined) | LLM decides once | LLM decides at each step |
| Tool usage | ❌ | ✅ Single call | ✅ Multiple calls |
| Complexity | Low | Medium | High |
| Best for | Workflows | Single actions | Complex, open-ended tasks |

---

> **Summary:** An Agent in LangChain combines an LLM with tools and a reasoning loop (ReAct pattern) to autonomously complete complex, multi-step tasks. The `AgentExecutor` manages the loop, while `create_react_agent` sets up the reasoning structure.
