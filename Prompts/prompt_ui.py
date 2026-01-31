from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv  

import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

# calling api key from .env file
load_dotenv()
#loading the model
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

# Streamlit app title
st.header('Student Research Tool')

# User selections
paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)


template = load_prompt("template.json")



# creating button for user interaction
if st.button('Get Research Summary'):
    chain = template | model #creating chain 
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    st.write(result.content)
