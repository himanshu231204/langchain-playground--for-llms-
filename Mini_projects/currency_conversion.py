from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage ,ToolMessage
from langchain_community.tools import tool
from langchain_core.tools import InjectedToolArg
from typing import Annotated
import requests,json


llm = ChatOllama(
    model="qwen3.5:397b-cloud",  
    temperature=0.2
)


@tool
def get_conversion_factors(base_currency:str, target_currency:str) -> float:
    """ this function will convert the base currency to target currency and return the converted amount"""
    url=f' https://v6.exchangerate-api.com/v6/437eb96292d41576c190633b/pair/{base_currency}/{target_currency}'
    response = requests.get(url) # make the API request to get the conversion rate
    return response.json()


@tool
def convert(base_currency:int, conversion_rate:Annotated[float, InjectedToolArg]) -> float:
    """ this function will convert the base currency to target currency and return the converted amount"""
    return base_currency * conversion_rate

#print(convert.args)

#print(get_conversion_factors.invoke({"base_currency": "USD", "target_currency": "INR"}))

#print(convert.invoke({"base_currency": 100, "conversion_rate": 82.5}))


#binding the tools with llm

llm_tool = llm.bind_tools([get_conversion_factors, convert])

#tool calls with llm

messages = [HumanMessage("I want to convert 100 USD to INR, please get the conversion rate and then convert the amount for me")]

ai_message = llm_tool.invoke(messages) #invoke the llm with tools

#print(ai_message)
#print(ai_message.tool_calls) #print(ai_message.tool_calls) # get the arguments for the tool calls made by the llm
messages.append(ai_message) #append the ai message to messages list to execute the tool calls and get the results


for tool_call in ai_message.tool_calls:
  # execute the 1st tool and get the value of conversion rate
  if tool_call['name'] == 'get_conversion_factors':
    tool_message1 = get_conversion_factors.invoke(tool_call)
    # fetch this conversion rate
    conversion_rate = json.loads(tool_message1.content)['conversion_rate']
    # append this tool message to messages list
    messages.append(tool_message1)
  # execute the 2nd tool using the conversion rate from tool 1
  if tool_call['name'] == 'convert':
    # fetch the current arg
    tool_call['args']['conversion_rate'] = conversion_rate
    tool_message2 = convert.invoke(tool_call)
    messages.append(tool_message2)
    
    
#print(messages)   

# the final response from llm after executing the tool calls and appending the tool messages to the messages list
final_response = llm_tool.invoke(messages).content
print(final_response) 