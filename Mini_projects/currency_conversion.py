from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage ,ToolMessage
from langchain_community.tools import tool
from langchain_core.tools import InjectedToolArg
from typing import Annotated
import requests


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

print(get_conversion_factors.invoke({"base_currency": "USD", "target_currency": "INR"}))

print(convert.invoke({"base_currency": 100, "conversion_rate": 82.5}))


#binding the tools with llm

llm_tool = llm.bind_tools([get_conversion_factors, convert])

#tool calls with llm

message = [HumanMessage("I want to convert 100 USD to INR, please get the conversion rate and then convert the amount for me")]

ai_message = llm_tool.invoke(message) #invoke the llm with tools
print(ai_message,"\n",ai_message.tool_calls) # tool calls requested by llm

