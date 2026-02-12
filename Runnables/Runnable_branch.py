#🔀 RunnableBranch is a conditional runnable that routes input to different chains based on a condition (like an if-else inside a LangChain pipeline).

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableBranch , RunnableParallel, RunnableLambda,RunnableSequence,RunnablePassthrough




llm = ChatOllama(
    model="mistral",
    temperature=0.2
)

prompt1=PromptTemplate(
    template='write a detailed report on{topic}',
    input_variables=['topic']
)

prompt2=PromptTemplate(
    template=' summarize the following text \n  {text}',
    input_variables=['text'] 
)


pareser=StrOutputParser()

report_chain=RunnableSequence(prompt1, llm, pareser)
summary_chain=RunnableSequence(prompt2, llm, pareser)

Branch_cahin=RunnableBranch(
    (lambda x: len(x.split()) > 100, summary_chain),
    RunnablePassthrough() #default case if the condition is not met, it will return the original text without summarization
)

finally_chain=RunnableSequence(report_chain, Branch_cahin)

print(finally_chain.invoke({"topic":" The impact of Artificial Intelligence on various industries and its potential future developments. "}))