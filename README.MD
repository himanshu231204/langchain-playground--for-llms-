# 🚀 LangChain Playground for LLMs

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green)
![GenAI](https://img.shields.io/badge/Generative%20AI-LLMs-orange)
![Ollama](https://img.shields.io/badge/Local%20LLM-Ollama-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

> 🎯 A Complete Beginner → Advanced LangChain & Generative AI Learning Repository  
> Build RAG Systems, AI Agents & Production-Ready LLM Applications Step-by-Step.

---

# 📌 Why This Repository?

Most LangChain & GenAI resources are scattered.

This repository is designed as a:

✔ Structured Learning Path  
✔ Practical Code Reference  
✔ RAG & Agent Playground  
✔ Local + API LLM Implementation Hub  
✔ One-Stop Solution for Students  

If you're learning **Generative AI, LLMs, LangChain, or RAG**, this repository provides everything in one place.

---

# 🗺️ Complete Learning Roadmap

Follow this order 👇

## 1️⃣ Generative AI Fundamentals
- What are LLMs?
- Tokens, embeddings & inference
- How modern AI systems work

## 2️⃣ LangChain Core Concepts
- Chat models
- Prompt templates
- Message objects
- Structured outputs

## 3️⃣ Output Control & Reliability
- JSON schema outputs
- Pydantic & TypedDict
- Output parsers
- Format enforcement

## 4️⃣ Chains & Runnables (LCEL)
- Sequential chains
- Parallel execution
- LangChain Expression Language
- Advanced workflow composition

## 5️⃣ Document Processing
- PDF loaders
- Text splitters
- Chunking strategies
- Data preprocessing

## 6️⃣ Embeddings & Vector Databases
- Embedding generation
- Similarity search
- Chroma Vector DB
- Retriever pipelines

## 7️⃣ RAG (Retrieval Augmented Generation)
- RAG architecture
- Context injection
- End-to-end pipeline
- Modular RAG components

## 8️⃣ Tools & AI Agents
- Tool calling
- Agent workflows
- Autonomous execution logic

## 9️⃣ Mini Projects
- End-to-end LLM apps
- Practical GenAI use cases
- Applied RAG systems

---

# 🧠 Local LLM (Ollama) Integration

This repository also supports **Local LLM execution using Ollama**.

You can run models locally without relying on paid APIs.

### Install Ollama
Download from: https://ollama.com

Pull a model:

```bash
ollama pull llama3
```

Run locally:

```bash
ollama run llama3
```

### Using Ollama with LangChain

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

response = llm.invoke("Explain Retrieval Augmented Generation in simple words")
print(response.content)
```

This allows:
- 100% local inference
- No API cost
- Privacy-focused development
- Offline experimentation

---

# 🧱 Repository Structure

```
langchain-playground--for-llms-
│
├── Chain/                 
├── chatmodel/             
├── chroma_db/             
├── EmbeddingModel/        
├── Messages/              
├── Output_Parsers/        
├── Prompts/               
├── Structured_Output/     
├── RAG/                   
├── Rag_Components/        
├── Runnables/             
├── Tools/                 
├── Mini_projects/         
├── Sample_Data/           
│
├── notes.txt              
├── test.py                
├── requirements.txt
├── .env.example
└── README.md
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/himanshu231204/langchain-playground--for-llms-.git
cd langchain-playground--for-llms-
```

## 2️⃣ Create Virtual Environment

```bash
python -m venv genai_env
genai_env\Scripts\activate   # Windows
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Configure Environment Variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

⚠️ Never push `.env` files to GitHub.

---

# 🔐 Security Best Practices

- API keys are stored using environment variables
- `.env` files are ignored
- No secrets are hard-coded
- Modular & reusable architecture

---

# 🎯 Goals of This Repository

- Learn LangChain by writing real code
- Build reusable GenAI components
- Understand production-ready pipelines
- Develop RAG systems from scratch
- Experiment with Local & API-based LLMs

---

# 🚀 Future Enhancements

- Multi-agent systems
- Memory integration
- Evaluation & monitoring
- Deployment-ready GenAI apps
- Streamlit-based UI demos

---

# 🤝 Contributions

This repository is built for learning and experimentation.

Feel free to:
- Fork
- Improve
- Add examples
- Open pull requests

---

# ⭐ Support & Motivation

If this repository helped you:

- ⭐ Star the repo
- 🔗 Share it with others
- ☕ Support the journey

---

# 🔗 Connect With Me

- 💼 LinkedIn: https://www.linkedin.com/in/himanshu231204  
- 🐙 GitHub: https://github.com/himanshu231204  
- 🐦 Twitter/X: https://twitter.com/himanshu231204  
- ☕ Buy Me a Coffee: https://www.buymeacoffee.com/himanshu231204  

---

# 🎉 Final Note

This repository represents my structured journey learning Generative AI, LangChain, RAG, and Local LLM systems.

If you're learning too — let's build together 🚀