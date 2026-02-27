from langchain_ollama import ChatOllama
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun

# Model initialization
llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

# tool initialization

#search tool
search_tool = DuckDuckGoSearchRun()

#custom tool

@tool
def get_weather(city:str) -> str:
    """ this function will return the current weather of the city provided as input"""
    url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'
    response = requests.get(url)
    return response.json()


#using the react_agent and agent_executor to bind the tools with llm and execute the tool calls

from langchain.agents import create_react_agent
from langchain.agents import AgentExecutor
from langchain import hub

# step-2
#pull the ReAct prompt template from the hub

prompt=hub.pull('hwchase17/react')  #pulling the ReAct prompt template from the hub

# step-3
# creating the ReAct agent using the prompt template and llm

agent=create_react_agent(llm=llm, prompt=prompt, tools=[search_tool, get_weather])


# step-4
#wrap it with AgentExecutor to execute the tool calls

agent_executor=AgentExecutor(agent=agent, tools=[search_tool, get_weather], verbose=True) # verbose=true will show the thought process of the agent and the tool calls made by the agent


#step-5
#agent call

response=agent_executor.invoke("what is the capital of India and what is the current weather there?")

print(response['output'])
print(response['tool_uses'])