from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableBranch , RunnableParallel, RunnableLambda,RunnableSequence,RunnablePassthrough


llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

prompt1=PromptTemplate(
    template='write a 5 line samll poem{topic}',
    input_variables=['topic']   
)

prompt2=PromptTemplate(
    template='Explain the meaning of the poem in simple words , to 5 year child text:\n{text}',
    input_variables=['text']   
)

pareser=StrOutputParser()

# using runnablesequence to create a chain of operations

poem_chain=RunnableSequence(prompt1, llm, pareser)

paralle_chain=RunnableParallel({
    'poem':RunnablePassthrough(),
    'explanation':RunnableSequence(poem_chain, prompt2, llm, pareser)
})

final_chain=RunnableSequence(poem_chain, paralle_chain)

print(final_chain.invoke({"topic":" Summer and its beauty"}))