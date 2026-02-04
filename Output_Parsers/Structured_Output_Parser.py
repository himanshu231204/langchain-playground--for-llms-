"""
StructuredOutputParser was an older LangChain abstraction 
for schema-based outputs and has been replaced by JsonOutputParser
and PydanticOutputParser in newer versions.
"""

from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema # type: ignore #types IGNORE: warning
import os
from dotenv import load_dotenv

load_dotenv()

model = ChatOllama(
        model="phi",
        streaming=False,
        timeout=60 ,
        temperature=0.2
        )

schema= [
    ResponseSchema(name="fact_1", description="the name of the topic"),
    ResponseSchema(name="fact_2", description="the name of the topic"),
    ResponseSchema(name="fact_3", description="the name of the topic"),
]

parser= StructuredOutputParser.from_response_schemas(schema)

template= PromptTemplate(
    template="Give me 3 facts about {topic} \n {formate_instructions}",
    input_variables=["topic"],
    partial_variables={"formate_instructions": parser.get_format_instructions()}    
)

chain = template | model | parser
result = chain.invoke({"topic": "black hole"})
print(result)

