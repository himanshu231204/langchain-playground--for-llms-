from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="qwen3.5:397b-cloud",  
    temperature=0.2
)