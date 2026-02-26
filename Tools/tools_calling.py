from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import Tool



llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

