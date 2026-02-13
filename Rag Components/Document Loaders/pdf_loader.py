from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

#create a pdf loader object
loader=PyPDFLoader('sample.pdf')

#load the documents
doc=loader.load()
print(doc)

print(len(doc)) #output: 2 (2 pages in the pdf)

#content of the first document & metadata of the first document
print(doc[0].page_content)
print(doc[1].metadata) #output: page_content='This is the content of the first page
