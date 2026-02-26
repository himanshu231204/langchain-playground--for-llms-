from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage 
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool 
from langchain_community.tools import DuckDuckGoSearchRun





llm = ChatOllama(
    model="qwen3.5:397b-cloud",  
    temperature=0.2
)


# custom the tool
@tool
def addNums(a: int, b: int) -> int:
    """given two numbers, return their sum"""
    return a + b


# inbuilt tool
search_tool = DuckDuckGoSearchRun()

#invoke the tool using 

print(addNums.invoke({"a": 2, "b": 3}))


# tool binding with llm

llm_tool =llm.bind_tools([addNums, search_tool])



query=HumanMessage('Impoetant discussion of Ai submit in india, please search for the news and give me a summary, and also calculate 2+3 for me')

message=[query]
print(llm_tool.invoke(message))
