from langchain_community.document_loaders import TextLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)


prompt=PromptTemplate(
    template='write a summary of the following text: {text}',
    input_variables=['text']
)

parser=StrOutputParser()





#create a text loader object

loader=TextLoader('sample_data.txt', encoding='utf-8')

#load the documents
documents=loader.load()
print(documents)

#type of documents
print(type(documents)) #output: <class 'list'>

#number of documents
print(len(documents)) #output: 1

#content of the first document
print(documents[0]) #output: page_content='This is a sample text file for testing the TextLoader class.' metadata={'source': 'sample_data.txt'}

#print the page content of the first document
print(documents[0].page_content) #output: This is a sample text file for

#print the metadata of the first document
print(documents[0].metadata) #output: {'source': 'sample_data.txt'}


#chain to summarize the document

chain=prompt | llm | parser

#run the chain on the document

print(chain.invoke({'text': documents[0].page_content})) #output: This is a sample text file for testing the TextLoader class.