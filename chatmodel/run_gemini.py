from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0) #max_output_tokens=100000)


result= model.invoke('what is Genai?how we can use it in python programming? Give me example code')

print("Response:\n",result.content)