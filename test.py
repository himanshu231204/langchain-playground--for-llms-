import langchain

print(langchain.__version__)
#=======================================================
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="phi",
    streaming=False,   # ⭐ MOST IMPORTANT
    timeout=60,        # ⭐ safety
    temperature=0.2
)

response = llm.invoke("Hello, who are you?")
print(response.content)
