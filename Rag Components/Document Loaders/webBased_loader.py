import os
os.environ["USER_AGENT"] = "Mozilla/5.0"

from langchain_community.document_loaders import WebBaseLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(model="mistral", temperature=0.2)

prompt = PromptTemplate(
    template="Answer the following question:\n{question}\n\nFrom this text:\n{text}",
    input_variables=["question", "text"]
)

parser = StrOutputParser()

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
loader = WebBaseLoader(url)

doc = loader.load()

print("Document loaded successfully")



chain = prompt | llm | parser

result = chain.invoke({
    "question": "Who developed Python?",
    "text":doc[0].page_content[:1000] #taking only the first 1000 characters of the document for the question answering task
})

print(result)
