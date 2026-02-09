#Problem Statement:
# Tpoic-->llm--> report-->llm--summary of report

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Define the prompt template
prompt1= PromptTemplate(
    template=" Write a detailed report on {topic}." ,
    input_variables=["topic"]
)

prompt2= PromptTemplate(
    template=" Write the 5 pointer summary of the report on {text}." ,
    input_variables=["text"]
)
# Define the LLM model
model = ChatOllama(
    model="mistral",
    temperature=0.2
)
parser= StrOutputParser()

#Create the chain by connecting the prompt and the model
chain= prompt1 | model | parser| prompt2 | model | parser

#Invoke the chain with input
result = chain.invoke({"topic": "Artificial Intelligence"})
print(result)

#to visualize the chain
chain.get_graph().print_ascii()