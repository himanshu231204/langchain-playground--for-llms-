from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool



llm = ChatOllama(
    model="mistral",
    temperature=0.2
)


# craeating the tool
@tool
def addNums(a: int, b: int) -> int:
    """given two numbers, return their sum"""
    return a + b


#invoke the tool using 

print(addNums.invoke({"a": 2, "b": 3}))


# tool binding with llm