# Directory Loader , loads all the files in a folder and returns a list of documents

from langchain_community.document_loaders import TextLoader, PyPDFLoader, DirectoryLoader
from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)


#create a directory loader object
loader=DirectoryLoader(
    path='Sample Data', #path to the directory containing the files
    glob='*.pdf', #glob pattern to match the files to be loaded, in this case all pdf files in the directory
    loader_cls=PyPDFLoader #loader class to be used for loading the files, in this case PyPDFLoader for pdf files
)

#lazy loading of the documents

doc=loader.lazy_load()

for d in doc:
    print(d.metadata) #output: page_content='This is the content of the first page of the first pdf file.' metadata={'source': 'Sample Data/sample1.pdf'}

"""'''
docs=loader.load()
print(docs) #loads all the pdf files in the Sample Data directory and returns a list of documents
print(len(docs))

#load the first document
print(docs[0]) #output: page_content='This is the content of the first page of the first pdf file.' metadata={'source': 'Sample Data/sample1.pdf'}
"""