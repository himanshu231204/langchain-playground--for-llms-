from langchain_ollama import ChatOllama
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
    response = requests.get(url)
    return response.json()


@tool
def convert(base_currency:int, conversion_rate:Annotated[float, InjectedToolArg]) -> float:
    """ this function will convert the base currency to target currency and return the converted amount"""
    return base_currency * conversion_rate

print(convert.args)

