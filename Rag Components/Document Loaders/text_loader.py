from langchain_community.document_loaders import TextLoader

#create a text loader object

loader=TextLoader('C:\\Users\\himan\\Desktop\\GenAI_LLM\\Rag Components\\rag_notes.txt', encoding='utf-8')

#load the documents
documents=loader.load()
print(documents)