from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_openai import ChatOpenAI
from langchain.tools import tool

# 1. LLM
llm = ChatOpenAI(model="gpt-4o")

# 2. Define Tool
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

tools = [multiply]

# 3. Create Agent
agent = create_tool_calling_agent(llm, tools)

# 4. Executor
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

response = agent_executor.invoke(
    {"input": "What is 6 multiplied by 7?"}
)

print(response)