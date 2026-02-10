"""
Parallel Chain Example:
Input → Notes + Quiz (parallel) → Merge → Final Output


from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel


# -------------------- Prompts --------------------

prompt_notes = PromptTemplate(
    template="Write very short and simple notes on {topic}.",
    input_variables=["topic"]
)

prompt_quiz = PromptTemplate(
    template="Generate a 3-question short quiz on {topic}.",
    input_variables=["topic"]
)

prompt_merge = PromptTemplate(
    template=(
        "Combine the following into one output:\n\n"
        "Notes:\n{notes}\n\n"
        "Quiz:\n{quiz}"
    ),
    input_variables=["notes", "quiz"]
)

# -------------------- Model --------------------

model = ChatOllama(
    model="mistral",
    temperature=0.2,
    base_url="http://127.0.0.1:11434"
)

# -------------------- Parser --------------------

parser = StrOutputParser()

# -------------------- Parallel Chain --------------------

parallel_chain = RunnableParallel(
    notes=prompt_notes | model | parser,
    quiz=prompt_quiz | model | parser,
)

# -------------------- Merge Chain --------------------

merge_chain = prompt_merge | model | parser

# -------------------- Final Chain --------------------

final_chain = parallel_chain | merge_chain

# -------------------- Invoke --------------------

final_result = final_chain.invoke({"topic": "Artificial Intelligence"})
print(final_result)
"""

# Parallel chains may fail on local LLM servers due to concurrent connection limits; controlling concurrency or sharing the model instance fixes this.

#----------------------------------*----------------------------we will use gemani-2.5-flash   for this example------------------*----------------------------



from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

# -------------------- Prompts --------------------

prompt_notes = PromptTemplate(
    template="Write very short and simple notes on {topic}.",
    input_variables=["topic"]
)

prompt_quiz = PromptTemplate(
    template="Generate a 3-question short quiz on {topic}.",
    input_variables=["topic"]
)

prompt_merge = PromptTemplate(
    template=(
        "Combine the following into one output:\n\n"
        "Notes:\n{notes}\n\n"
        "Quiz:\n{quiz}"
    ),
    input_variables=["notes", "quiz"]
)

# -------------------- Gemini Model (ONE model) --------------------

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0
)

# -------------------- Parser --------------------

parser = StrOutputParser()

# -------------------- Parallel Chain --------------------

parallel_chain = RunnableParallel(
    notes=prompt_notes | model | parser,
    quiz=prompt_quiz | model | parser,
)

# -------------------- Merge Chain --------------------

merge_chain = prompt_merge | model | parser

# -------------------- Final Chain --------------------

final_chain = parallel_chain | merge_chain

# -------------------- Invoke --------------------

final_result = final_chain.invoke(
    {"topic": "Artificial Intelligence"}
)

print(final_result)
final_chain.get_graph().print_ascii()