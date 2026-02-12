from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableBranch , RunnableParallel, RunnableLambda,RunnableSequence


llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

prompt1= PromptTemplate(
    template='generate a tweet about{topic}', 
    input_variables=['topic']   
)

prompt2= PromptTemplate(
    template='generate a linkdin post about{topic}', 
    input_variables=['topic']   
)

parser=StrOutputParser()

Parall_chain=RunnableParallel(
    {
        'tweet':RunnableSequence(prompt1, llm, parser),
        'linkdin':RunnableSequence(prompt2, llm, parser)
    }
)

print(Parall_chain.invoke({"topic":"Machine Learning and its applications"}))

#workflow
Parall_chain.get_graph().print_ascii()