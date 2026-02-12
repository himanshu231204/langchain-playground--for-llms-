from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_core.runnables import RunnableBranch , RunnableParallel, RunnableLambda,RunnableSequence,RunnablePassthrough


def word_count(text): return len(text.split())

llm = ChatOllama(
    model="mistral",
    temperature=0.2
)


prompt=PromptTemplate(
    template='write a song about{topic}',
input_variables=['topic'] 
)
pareser=StrOutputParser()

song_generator_chain=RunnableSequence(prompt, llm, pareser)

parallel_chain=RunnableParallel({
    'song':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

final_chain=RunnableSequence(song_generator_chain, parallel_chain)

print(final_chain.invoke({"topic":" A dog and a cat"}))
 