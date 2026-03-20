# 🦜 LangChain Playground for LLMs

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![LangChain](https://img.shields.io/badge/LangChain-v1.0.3-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-blueviolet)
![Status](https://img.shields.io/badge/Status-Active-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A hands-on learning repository covering **LangChain**, **Generative AI**, and **Large Language Models (LLMs)** — from fundamentals to production-ready patterns such as RAG pipelines and AI agents.

---

## Table of Contents

- [Overview](#overview)
- [Learning Roadmap](#learning-roadmap)
- [Repository Structure](#repository-structure)
- [Notes Index](#notes-index)
- [Getting Started](#getting-started)
- [Local LLM Support (Ollama)](#local-llm-support-ollama)
- [Security](#security)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Connect](#connect)

---

## Overview

Most LangChain and GenAI resources are scattered across tutorials, notebooks, and blog posts. This repository consolidates them into a single, structured workspace that serves as:

- **Structured learning path** — progressing from basics to advanced topics
- **Practical code reference** — runnable examples for every core LangChain concept
- **RAG & Agent playground** — end-to-end retrieval-augmented generation and agent implementations
- **Local + API LLM hub** — examples using Ollama (local), Google Gemini, OpenAI, and Hugging Face

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

## Future Enhancements

- Multi-agent systems with LangGraph
- Conversational memory integration
- Evaluation and monitoring pipelines
- Deployment-ready GenAI applications
- Streamlit-based interactive demos

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
