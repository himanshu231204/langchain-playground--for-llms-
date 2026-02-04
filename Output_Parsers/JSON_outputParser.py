from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
        model="phi",
        streaming=False,
        timeout=60 ,
        temperature=0.2
        )
parser= JsonOutputParser()
# Prompt Templates
template = PromptTemplate(
    template="Give {topic} \n {formate_instructions}",
    input_variables=["topic"],
    partial_variables={"formate_instructions": parser.get_format_instructions()}
    
)

#prompt=template.format()


#result = model.invoke(prompt)
#parsing the output using the parser
#final_result = parser.parse(result.content)

# we can use the chain to do all the above steps in one go
chain = template | model | parser
result = chain.invoke({"topic": "write a 5 line poem"})
print(result)