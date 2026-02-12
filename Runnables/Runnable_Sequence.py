from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableBranch , RunnableParallel, RunnableLambda,RunnableSequence


llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

prompt=PromptTemplate(
    template='write a 5 line samll poem{topic}',
    input_variables=['topic']   
)

prompt2=PromptTemplate(
    template='Explain the meaning of the poem in simple words , to 5 year child text:\n{text}',
    input_variables=['text']   
)

pareser=StrOutputParser()

# using runnablesequence to create a chain of operations

chain=RunnableSequence(prompt, llm, pareser,  prompt2, llm, pareser)

print(chain.invoke({"topic":" about the beauty of nature"}))