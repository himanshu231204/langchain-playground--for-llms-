#Build a system that analyzes user feedback and conditionally triggers different actions for positive and negative responses.

"""
                 +-----------+
                 | Feedback  |
                 +-----------+
                       |
                       v
            +-------------------------+
            | Analyze Feedback        |
            | (Positive / Negative)   |
            +-------------------------+
                   /         \
                  /           \
                 v             v
        +----------------+   +------------------+
        |   Positive     |   |    Negative      |
        +----------------+   +------------------+
                 |                   |
                 v                   v
        +----------------+   +------------------+
        | Save Feedback  |   | Send Email /     |
        | / Acknowledge  |   | Raise Complaint  |
        +----------------+   +------------------+

    """


from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser #for parsing structured data into Pydantic models
from pydantic import BaseModel, Field
from langchain_core.runnables import RunnableBranch , RunnableParallel, RunnableLambda
from typing import Literal #for defining a field that can only take specific string values (e.g., "positive" or "negative")


model = ChatOllama(
    model="mistral",
    temperature=0.2
)

parser=StrOutputParser()

#class feedback analysis result model
class FeedbackAnalysisResult(BaseModel):
    sentiment: Literal["positive", "negative"] = Field(..., description="The sentiment of the feedback, either 'positive' or 'negative'.")
    reason: str = Field(..., description="A brief explanation of why the feedback was classified as positive or negative.")

parser2=PydanticOutputParser(pydantic_object=FeedbackAnalysisResult)


prompt1 = PromptTemplate(
    template="Analyze the following feedback and determine if it is positive or negative: {feedback} \n {format_instructions}",
    input_variables=["feedback"],
    partial_variables={"format_instructions": parser2.get_format_instructions()}
)

classifier_chain= prompt1 | model | parser2

prompt2 = PromptTemplate(
    template="write an acknowledgment message for the following positive feedback: {feedback}",
    input_variables=["feedback"]
)

prompt3 = PromptTemplate(
    template="write an acknowledgment message for the following negative  feedback: {feedback}",
    input_variables=["feedback"]
)

Postive_chain= prompt2 | model | parser
Negative_chain= prompt3 | model | parser

branch_chain=RunnableBranch(
    (lambda inputs: inputs["sentiment"] == "positive", Postive_chain),
    (lambda inputs: inputs["sentiment"] == "negative", Negative_chain),   
    RunnableLambda(lambda inputs: "Invalid sentiment value") #default case if sentiment is neither positive nor negative (should not happen due to Pydantic validation
)
    
    
#final chain that combines the classifier and the branch
final_chain=classifier_chain | RunnableLambda(lambda analysis: {
        "sentiment": analysis.sentiment,
        "feedback": analysis.reason  # or original feedback if you want
    }) |branch_chain 

result=final_chain.invoke({"feedback": "I love the new features, app is working good."})
print(result)
final_chain.get_graph().print_ascii()