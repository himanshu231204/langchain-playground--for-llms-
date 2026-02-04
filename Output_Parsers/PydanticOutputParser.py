from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel

model = ChatOllama(
    model="phi",
    temperature=0.2
)

class Person(BaseModel):
    name: str
    age: int
    occupation: str

parser = PydanticOutputParser(pydantic_object=Person)

prompt = PromptTemplate(
    template="""
Return information about the person strictly in this JSON format:

{{
  "name": "string",
  "age": number,
  "occupation": "string"
}}

Rules:
- Fill REAL values
- Do NOT return schema
- Do NOT explain
- Return ONLY JSON

Person name: {name}
""",
    input_variables=["name"]
)

chain = prompt | model | parser

result = chain.invoke({"name": "Rahul Dravid"})
print(result)


"""
PydanticOutputParser expects data, not schema.
Small LLMs often echo schema instructions.
For small models, explicitly force output shape instead of using auto schema instructions.
    """