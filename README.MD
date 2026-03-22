<div align="center">

# 🦜 LangChain Playground for LLMs

### *The most complete, hands-on LangChain learning repository on GitHub*

[![GitHub Stars](https://img.shields.io/github/stars/himanshu231204/langchain-playground--for-llms-?style=for-the-badge&logo=github&color=gold)](https://github.com/himanshu231204/langchain-playground--for-llms-/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/himanshu231204/langchain-playground--for-llms-?style=for-the-badge&logo=github&color=blue)](https://github.com/himanshu231204/langchain-playground--for-llms-/network/members)
[![GitHub Watchers](https://img.shields.io/github/watchers/himanshu231204/langchain-playground--for-llms-?style=for-the-badge&logo=github&color=green)](https://github.com/himanshu231204/langchain-playground--for-llms-/watchers)
[![GitHub Issues](https://img.shields.io/github/issues/himanshu231204/langchain-playground--for-llms-?style=for-the-badge&color=red)](https://github.com/himanshu231204/langchain-playground--for-llms-/issues)

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-v1.0.3-1C3C3C?style=flat-square&logo=chainlink&logoColor=white)](https://langchain.com)
[![LangGraph](https://img.shields.io/badge/LangGraph-v1.0.2-FF6B6B?style=flat-square)](https://langchain-ai.github.io/langgraph/)
[![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-blueviolet?style=flat-square)](https://ollama.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-412991?style=flat-square&logo=openai&logoColor=white)](https://openai.com)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini-4285F4?style=flat-square&logo=google&logoColor=white)](https://ai.google.dev)
[![Streamlit](https://img.shields.io/badge/Streamlit-UI-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-lightgrey?style=flat-square)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)

<br/>

> **Build, learn, and ship production-ready LLM applications** — from your first prompt to full-scale RAG pipelines and autonomous AI agents.

<br/>

**⭐ If this repo helps you, please give it a star — it helps others discover it too! ⭐**

</div>

---

## 🚀 Why This Repository?

Most LangChain resources are scattered across tutorials, notebooks, and outdated blog posts. This repository brings **everything into one place** — structured, runnable, and ready for production.

| 🎯 | What You Get |
|----|-------------|
| 📚 | **Structured learning path** — progress from zero to LLM expert in a logical sequence |
| 💻 | **100% runnable code** — every concept has a working example you can run immediately |
| 🔍 | **RAG pipelines** — full retrieval-augmented generation with Chroma, FAISS, and more |
| 🤖 | **AI Agents** — ReAct-pattern agents with custom tools and LangGraph workflows |
| 🏠 | **Local LLM support** — run everything offline with Ollama (zero API costs) |
| 🌐 | **Multi-provider** — OpenAI, Google Gemini, Hugging Face, and Ollama side-by-side |
| 📝 | **Rich notes & docs** — detailed markdown notes for every topic covered |
| 🔧 | **Production patterns** — LCEL, tool calling, structured output, and memory |

---

## Table of Contents

- [Why This Repository?](#-why-this-repository)
- [Learning Roadmap](#learning-roadmap)
- [Repository Structure](#repository-structure)
- [Notes Index](#notes-index)
- [Getting Started](#getting-started)
- [Local LLM Support (Ollama)](#local-llm-support-ollama)
- [Tech Stack](#tech-stack)
- [Security](#security)
- [Future Enhancements](#future-enhancements)
- [GitHub Topics](#github-topics)
- [Contributing](#contributing)
- [Connect](#connect)

---

## Learning Roadmap

The content is organized to be followed in order:

| # | Topic | Description |
|---|-------|-------------|
| 1 | **Chat Models** | LLM initialization with Ollama, Gemini, and OpenAI (`chatmodel/`) |
| 2 | **Messages** | SystemMessage, HumanMessage, AIMessage, and chat history (`Messages/`) |
| 3 | **Prompt Engineering** | Prompt templates, dynamic generation, and a Streamlit prompt UI (`Prompts/`) |
| 4 | **Structured Output** | Enforcing JSON schema, Pydantic, and TypedDict outputs (`Structured Output/`) |
| 5 | **Output Parsers** | JSON, Pydantic, string, and structured output parsers (`Output_Parsers/`) |
| 6 | **Chains** | Sequential, parallel, and conditional chains (`Chain/`) |
| 7 | **Runnables (LCEL)** | LangChain Expression Language — sequences, parallelism, branching, lambdas, passthrough (`Runnables/`) |
| 8 | **Embeddings** | Document similarity using embedding models (`EmbeddingModel/`) |
| 9 | **RAG Components** | Document loaders, text splitters, vector stores (Chroma), and retrievers (`Rag Components/`) |
| 10 | **Tools & Agents** | Custom tool creation, tool calling, built-in tools, and agent workflows (`Tools/`) |
| 11 | **Mini Projects** | Applied projects — AI agents, currency conversion, agent templates (`Mini_projects/`) |

---

## Repository Structure

```
langchain-playground--for-llms-/
├── Chain/                    # Sequential, parallel, and conditional chain examples
├── chatmodel/                # LLM initialization (Ollama, Gemini)
├── chroma_db/                # Persisted Chroma vector database
├── EmbeddingModel/           # Document similarity with embeddings
├── Messages/                 # Chat message types and prompt templates
├── Mini_projects/            # End-to-end LLM applications
├── Output_Parsers/           # JSON, Pydantic, string, and structured parsers
├── Prompts/                  # Prompt templates and Streamlit UI
├── Rag Components/           # RAG pipeline modules
│   ├── Document Loaders/     #   PDF, CSV, text, web, and directory loaders
│   ├── Retrievers/           #   MultiQuery, contextual compression, MMR
│   ├── Text Splitters/       #   Length, markdown, code, and semantic splitting
│   └── Vectors Stores/       #   Chroma vector database integration
├── Runnables/                # LCEL runnables (sequence, parallel, branch, lambda)
├── Sample Data/              # Reference PDFs for RAG examples
├── Structured Output/        # JSON schema, Pydantic, and TypedDict outputs
├── Tools/                    # Custom and built-in tool calling, agent toolkits
├── notes.md                  # Core LangChain concept notes (Chat Models, Prompts, Messages)
├── requirements.txt          # Python dependencies
├── test.py                   # Quick-start test script
├── sample.pdf                # Sample document for loader testing
├── sample_data.md            # Sample text data for RAG testing
├── Titanic-Dataset.csv       # Sample dataset for data-loading examples
└── README.MD
```

---

## Notes Index

All concept notes are organized by topic. Click any link to jump directly to the notes.

### 🧠 Foundations

| Topic | Notes File |
|-------|-----------|
| Chat Models, Prompts & Messages | [notes.md](notes.md) |
| Chat History | [Messages/chat_history.md](Messages/chat_history.md) |

---

### ⛓️ Chains

| Topic | Notes File |
|-------|-----------|
| Simple & Sequential Chains | [Chain/chain.md](Chain/chain.md) |
| Parallel Chain | [Chain/parallel_chain.md](Chain/parallel_chain.md) |
| Conditional Chain (IF/ELSE routing) | [Chain/conditional_Chain.md](Chain/conditional_Chain.md) |

---

### 🔄 Runnables (LCEL)

| Topic | Notes File |
|-------|-----------|
| Runnables, LCEL, Primitive vs Task-Specific | [Runnables/Runnables.md](Runnables/Runnables.md) |

---

### 📤 Output Parsers & Structured Output

| Topic | Notes File |
|-------|-----------|
| Output Parsers Overview & Ollama | [Output_Parsers/notes1.md](Output_Parsers/notes1.md) |
| String Output Parser | [Output_Parsers/stringoutputParser.md](Output_Parsers/stringoutputParser.md) |
| JSON Output Parser | [Output_Parsers/jsonoutput_parser.md](Output_Parsers/jsonoutput_parser.md) |
| Pydantic Output Parser | [Output_Parsers/PydanticOutputParser.md](Output_Parsers/PydanticOutputParser.md) |
| Structured Output Parser (legacy) | [Output_Parsers/Structured Output Parser.md](Output_Parsers/Structured%20Output%20Parser.md) |
| TypedDict vs Pydantic vs JSON Schema | [Structured Output/structured.md](Structured%20Output/structured.md) |

---

### 📚 RAG Components

| Topic | Notes File |
|-------|-----------|
| Document Loaders (PDF, Web, CSV, Directory) | [Rag Components/rag_notes.md](Rag%20Components/rag_notes.md) |
| Text Splitters | [Rag Components/text_splitter_langchain_notes.md](Rag%20Components/text_splitter_langchain_notes.md) |
| Vector Stores Overview | [Rag Components/Vectors Stores/vector_store_notes.md](Rag%20Components/Vectors%20Stores/vector_store_notes.md) |
| Chroma DB | [Rag Components/Vectors Stores/chroma_db_notes.md](Rag%20Components/Vectors%20Stores/chroma_db_notes.md) |
| Chroma Internal Architecture | [Rag Components/Vectors Stores/chroma_internal_architecture.md](Rag%20Components/Vectors%20Stores/chroma_internal_architecture.md) |
| FAISS vs Chroma vs Pinecone Comparison | [Rag Components/Vectors Stores/vector_db_architecture_comparison.md](Rag%20Components/Vectors%20Stores/vector_db_architecture_comparison.md) |
| Retrievers Overview | [Rag Components/Retrievers/retriver.md](Rag%20Components/Retrievers/retriver.md) |
| MMR Retriever | [Rag Components/Retrievers/mmr.md](Rag%20Components/Retrievers/mmr.md) |
| MultiQuery Retriever | [Rag Components/Retrievers/MultiQuery_Retriever_Notes.md](Rag%20Components/Retrievers/MultiQuery_Retriever_Notes.md) |
| Contextual Compression Retriever | [Rag Components/Retrievers/Contextual_Compression_Retriever_Notes.md](Rag%20Components/Retrievers/Contextual_Compression_Retriever_Notes.md) |

---

### 🔧 Tools & Agents

| Topic | Notes File |
|-------|-----------|
| Tools Overview | [Tools/tools.md](Tools/tools.md) |
| Tool Binding | [Tools/tool_binding.md](Tools/tool_binding.md) |
| Tool Calling | [Tools/tools_calling .md](Tools/tools_calling%20.md) |
| Custom Tools | [Tools/custom_tools.md](Tools/custom_tools.md) |
| Toolkits | [Tools/toolkit.md](Tools/toolkit.md) |
| AI Agents (ReAct Pattern) | [Mini_projects/agent_notes.md](Mini_projects/agent_notes.md) |

---

### 📄 Sample Data

| File | Description |
|------|-------------|
| [sample_data.md](sample_data.md) | AI overview text for RAG testing |
| [sample.pdf](sample.pdf) | Sample PDF for document loader testing |
| [Titanic-Dataset.csv](Titanic-Dataset.csv) | Sample CSV for data loading examples |

---

## Getting Started

### Prerequisites

- Python 3.10 or higher
- [Ollama](https://ollama.com) (optional, for local LLM inference)

### 1. Clone the Repository

```bash
git clone https://github.com/himanshu231204/langchain-playground--for-llms-.git
cd langchain-playground--for-llms-
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_key
GOOGLE_API_KEY=your_google_api_key
HUGGINGFACEHUB_API_TOKEN=your_hf_token
```

> **Note:** The `.env` file is listed in `.gitignore` and should never be committed.

---

## Local LLM Support (Ollama)

This repository supports **local LLM inference** via [Ollama](https://ollama.com), allowing experimentation without API costs or internet access.

### Setup

```bash
# Install Ollama from https://ollama.com, then:
ollama pull llama3
ollama run llama3
```

### Usage with LangChain

```python
from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3")
response = llm.invoke("Explain Retrieval Augmented Generation in simple words")
print(response.content)
```

**Benefits of local inference:**

- No API costs
- Full data privacy
- Offline development
- Faster iteration for prototyping

---

## Security

- API keys are managed through environment variables (`.env`)
- `.env` is excluded from version control via `.gitignore`
- No secrets are hard-coded in source files

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| **LLM Providers** | OpenAI GPT-4, Google Gemini, Ollama (Llama 3, Mistral), Hugging Face |
| **Frameworks** | LangChain v1.0, LangGraph v1.0, LangChain Expression Language (LCEL) |
| **Vector Stores** | Chroma DB, FAISS |
| **Embeddings** | OpenAI Embeddings, HuggingFace Sentence Transformers |
| **Output Validation** | Pydantic v2, TypedDict, JSON Schema |
| **UI** | Streamlit |
| **Data** | Pandas, CSV, PDF, Markdown document loaders |
| **Language** | Python 3.10+ |

---

## Future Enhancements

- Multi-agent systems with LangGraph
- Conversational memory integration
- Evaluation and monitoring pipelines
- Deployment-ready GenAI applications
- Streamlit-based interactive demos

---

## GitHub Topics

> 📌 **Maintainer note:** Add the following topics in your repository settings (*About → Topics*) to maximize discoverability and stars on GitHub.

```
langchain  llm  generative-ai  rag  retrieval-augmented-generation
langchain-python  ai-agents  openai  google-gemini  ollama
vector-database  chromadb  pydantic  lcel  langchain-expression-language
huggingface  streamlit  python  machine-learning  nlp
large-language-models  prompt-engineering  ai  deep-learning  chatbot
langsmith  langgraph  embeddings  transformers  tutorial
```

---

## Contributing

Contributions are welcome. To get started:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes (`git commit -m "Add my feature"`)
4. Push to the branch (`git push origin feature/my-feature`)
5. Open a pull request

---

## Connect

- [LinkedIn](https://www.linkedin.com/in/himanshu231204)
- [GitHub](https://github.com/himanshu231204)
- [Twitter / X](https://twitter.com/himanshu231204)
- [Buy Me a Coffee](https://www.buymeacoffee.com/himanshu231204)

---

<div align="center">

### 🌟 Found this useful? Star the repo and share it with fellow AI enthusiasts!

[![Star History Chart](https://api.star-history.com/svg?repos=himanshu231204/langchain-playground--for-llms-&type=Date)](https://star-history.com/#himanshu231204/langchain-playground--for-llms-&Date)

**Made with ❤️ by [Himanshu](https://github.com/himanshu231204) — Happy Learning! 🚀**

</div>
