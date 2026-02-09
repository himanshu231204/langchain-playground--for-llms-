from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser


# Define the prompt template
prompt= PromptTemplate(
    template=" What is the capital of {country}?" ,
    input_variables=["country"]
)
# Define the LLM model
model = ChatOllama(
    model="mistral",
    temperature=0.2
)

#Create the chain by connecting the prompt and the model
parser= StrOutputParser()
chain = prompt | model | parser #(prompt | model) | stroutputparser)

#Invoke the chain with input

result = chain.invoke({"country": "India"})
print(result)

#to visualize the chain

chain.get_graph().print_ascii()