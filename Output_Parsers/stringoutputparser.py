# from langchain_huggingface import ChatHuggingFace

# starting with open source models from ollama/llama2

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate

# for string output parser
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

load_dotenv()


"""
llm = ChatHuggingFace(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
)
    """

#  I am getting error "StopIteration in HF chat = model not supported by provider" when
# I try to use the google/gemma-2-2b-it model. This error indicates that the HuggingFaceEndpoint is not able to
# find or use the specified model, which could be due to several reasons such as the model not being available, incorrect repo_id, or issues with authentication.


# ollama model initialization
model = ChatOllama(
        model="phi",
        streaming=False,
        timeout=60 ,
        temperature=0.2
        )



# Prompt Templates
template1 = PromptTemplate(
    template="Write a detailed report on {topic}", input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Write a 5 line summary on the following text:\n{text}",
    input_variables=["text"],
)

# Using StringOutputParser to ensure the output is a string
parser = StrOutputParser()

# forming the chain with the parser

# 🧠 Core Idea (ONE LINE)
# A chain is a pipeline where output of one step becomes input of the next step.

chain = template1 | model | parser | (lambda text: {"text": text}) | template2 | model | parser


"""
(lambda text: {"text": text}) — WHY we used it
This lambda converts LLM string output into the dictionary format required by the next PromptTemplate.
🧠 Core reason 

Because PromptTemplate needs a dictionary, but StrOutputParser gives a string.
    """
# invoking the chain
result = chain.invoke({"topic": "black hole"})
print(result)  # Final summarized string outputcc
