from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.messages import HumanMessage ,ToolMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.tools import tool 
from langchain_community.tools import DuckDuckGoSearchRun, DuckDuckGoSearchResults






llm = ChatOllama(
    model="qwen3.5:397b-cloud",  
    temperature=0.2
)


# custom the tool
@tool
def addNums(a: int, b: int) -> int:
    """given two numbers, return their sum"""
    return a + b


# inbuilt tool
search_tool = DuckDuckGoSearchRun()

#invoke the tool using 

print(addNums.invoke({"a": 2, "b": 3}))


# tool binding with llm

llm_tool =llm.bind_tools([addNums, search_tool])



query=HumanMessage('Important discussion of Ai submit in india, please search for the news and give me a summary, and also calculate 2+3 for me you must use the tools I provided you')

message=[query]

#invoke the llm with tools

response = llm_tool.invoke(message)
print("tools calls requested by llm: ",response.tool_calls)

# execute the tool calls and get the results

tool_message=[] # to store the tool calls and results

for call in response.tool_calls:
    tool_name=call["name"]
    tool_args=call["args"]
    tool_id=call["id"]
    
    if tool_name.startswith("addNums"):
        result=addNums.invoke(tool_args)
    elif tool_name.startswith("DuckDuckGoSearchResults"):
        result=search_tool.invoke(tool_args)
    else:
        result="tool not found"
    tool_message.append(
        ToolMessage(
            content=str(result), 
            tool_call_id=tool_id
            )
        )
    
    
    
 #send the tool results back to llm for final response generation
 
final_response=llm_tool.invoke(message+[response]+tool_message)  

print("final response from llm:\n ",final_response.content) 