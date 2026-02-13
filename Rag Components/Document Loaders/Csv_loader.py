from langchain_community.document_loaders import TextLoader,CSVLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

loader=CSVLoader('Titanic-Dataset.csv')

data=loader.load()

print(len(data)) #output: 891 (number of rows in the csv file)
print(data[0].page_content) #output: PassengerId,Survived,Pclass,Name
