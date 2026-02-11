from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

print(llm.invoke("What is the capital of India?"))
