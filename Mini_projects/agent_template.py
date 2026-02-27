from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_openai import ChatOpenAI

# 1. Pull the prompt template
prompt = hub.pull("hwchase17/react")

# 2. Initialize the LLM and Tools
llm = ChatOpenAI(model="gpt-4")
tools = [...] # Your list of tools

# 3. Construct the ReAct agent
agent = create_react_agent(llm, tools, prompt)

# 4. Create the executor
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)