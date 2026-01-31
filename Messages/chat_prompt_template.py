"""
🎯 WHY CHAT PROMPT TEMPLATE IS USED
-----------------------------------

✅ The main purpose of a ChatPromptTemplate is to create **dynamic messages**.
"""

from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'a googly'})

print(prompt)