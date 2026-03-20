🧠 Chat Model Params (Gemini)

temperature: controls creativity (0 = factual, 1+ = creative).

max_completion_tokens: limits output length (# of tokens).
✅ Low temp = accurate; High temp = imaginative.
✅ More tokens = longer reply.

------------------------------------------------------------------

🧠 Prompts in LangChain

Prompts = Input instructions given to LLMs.

Define what and how the model should respond.

Can be static or dynamic.

📘 Static Prompts

Fixed, unchanging text.

Example: "Explain photosynthesis in simple terms."

✅ Simple, consistent.

❌ Not flexible for user input.

⚙️ Dynamic Prompts

Use placeholders filled at runtime.

Example: "Explain {topic} in simple terms."

✅ Flexible, reusable.

❌ Requires correct variable formatting.

🧩 Use in LangChain

Managed with PromptTemplate or ChatPromptTemplate.

Often used in chains or retrieval (RAG) setups.

Supports combining system (static) + user (dynamic) prompts.



==============================================>>>>

🧩 CHAT MESSAGE TYPES IN LANGCHAIN / GENAI
------------------------------------------

In a chat-based AI system (like Gemini or OpenAI models),
every message in the conversation belongs to one of three main types.


1️⃣ SYSTEMMESSAGE
-----------------
Purpose: Defines the role, behavior, or context of the AI.
Think of it as: The instruction manual for the model before conversation starts.

Example:
SystemMessage(content="You are a helpful AI assistant.")

Used for:
- Setting tone or role (teacher, coder, etc.)
- Controlling the style of responses
- Maintaining consistent behavior


2️⃣ HUMANMESSAGE
----------------
Purpose: Represents what the user inputs during the chat.
Think of it as: The prompt or question coming from the user.

Example:
HumanMessage(content="Explain how chat history works in GenAI.")

Used for:
- Capturing user queries
- Passing new instructions to the AI


3️⃣ AIMESSAGE
--------------
Purpose: Stores the model’s reply or output.
Think of it as: The AI’s response that gets appended to the conversation.

Example:
AIMessage(content="Chat history helps the model remember previous context...")

Used for:
- Maintaining response history
- Displaying output in chat UI
- Feeding back into model for context continuity


🔁 HOW THEY WORK TOGETHER
-------------------------
The conversation is stored as a list of messages:

chat_history = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hi!"),
    AIMessage(content="Hello! How can I help you today?")
]

Each new user input and AI reply is appended to this list,
allowing the model to remember previous context across turns.


⚡ QUICK SUMMARY TABLE
----------------------

| Message Type   | Represents    | Purpose             | Example                           |
|----------------|----------------|---------------------|-----------------------------------|
| SystemMessage  | AI setup/role  | Defines behavior    | "You are a helpful assistant."    |
| HumanMessage   | User input     | Captures query      | "Explain AIMessage."              |
| AIMessage      | Model output   | Returns response    | "AIMessage stores model replies." |

------------------------------------------
🧠 TIP: Together, these messages make the conversation
context-aware and help the AI respond more naturally.
------------------------------------------


🎯 WHY CHAT PROMPT TEMPLATE IS USED
-----------------------------------

✅ The main purpose of a ChatPromptTemplate is to create **dynamic messages**.

That means — instead of writing a new prompt each time, 
you can write a reusable template with placeholders 
(like {name}, {topic}, {question}) that get filled automatically at runtime.

-----------------------------------
🧠 EXAMPLE:

from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain the topic: {topic}")
])

# Now you can fill it dynamically:
messages = prompt.format_messages(topic="Neural Networks")

→ Output:
System: "You are a helpful assistant."
Human: "Explain the topic: Neural Networks"

-----------------------------------
⚡ WHY THIS IS IMPORTANT:

- Makes your chatbot **flexible** and **reusable**
- Avoids hardcoding text in multiple places
- Allows easy personalization (like user name, task, topic)
- Helps integrate with dynamic user inputs or app data

-----------------------------------
💬 In short:
ChatPromptTemplate = “Dynamic message generator”
It creates personalized, structured prompts on the fly before sending them to the model.
-----------------------------------


🧩 MESSAGE PLACEHOLDER
----------------------

💡 DEFINITION:
A *message placeholder* is a variable or placeholder name 
inside a **Chat Prompt Template** that gets replaced with 
real data when the prompt is formatted.

It’s written inside curly braces { }.

--------------------------------------
🧠 SIMPLE IDEA:

Think of it like a “fill-in-the-blank” in your message.

Example:
"You are explaining the topic: {topic}"

Here, {topic} is the placeholder.

When the user provides a topic, 
the template automatically replaces it.

--------------------------------------
⚙️ EXAMPLE IN CODE:

from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful AI assistant."),
    ("human", "Explain the concept of {subject}.")
])

# Fill the placeholder dynamically
messages = prompt.format_messages(subject="Machine Learning")

Output:
System: "You are a helpful AI assistant."
Human: "Explain the concept of Machine Learning."

--------------------------------------
🎯 PURPOSE OF PLACEHOLDERS:

✅ To make prompts **dynamic** (change based on user input)
✅ To avoid hardcoding multiple similar messages
✅ To easily reuse one template for different situations

--------------------------------------
⚡ KEY POINTS:

- Placeholders are written as `{variable_name}`
- They are filled when you call `.format_messages()`
- You can have multiple placeholders in one template
  Example: "Hello {name}, explain {topic} briefly."

--------------------------------------
🪄 QUICK EXAMPLE WITH MULTIPLE PLACEHOLDERS:

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful tutor."),
    ("human", "Hi {name}, can you explain {concept}?")
])

messages = prompt.format_messages(name="Himanshu", concept="AI Chatbots")

→ Human: "Hi Himanshu, can you explain AI Chatbots?"

--------------------------------------
💬 SUMMARY:
Message placeholders = Variables inside templates 
that make prompts flexible, reusable, and dynamic.
--------------------------------------
