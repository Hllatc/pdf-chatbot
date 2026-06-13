# 📄 AI PDF Chatbot (RAG with FastAPI + Ollama)

A lightweight **Retrieval-Augmented Generation (RAG)** system that allows users to upload PDFs and ask questions about their content using a local LLM.

Built with **FastAPI, LangChain, ChromaDB, HuggingFace Embeddings, and Ollama**.

---

## 🚀 Features

* 📄 Upload PDF documents
* ✂️ Automatic text chunking
* 🧠 Semantic search with embeddings
* 📦 Vector storage using ChromaDB
* 🤖 Local LLM via Ollama (free, no API cost)
* 🔍 Context-aware question answering (RAG pipeline)
* ⚡ FastAPI backend (REST API)

---

## 🧱 Tech Stack

* **Backend:** FastAPI
* **RAG Framework:** LangChain
* **Vector DB:** ChromaDB
* **Embeddings:** HuggingFace (`multilingual-e5-base`)
* **LLM:** Ollama (Qwen2.5 / LLaMA 3.2)
* **PDF Processing:** PyPDFLoader

---

## 📁 Project Structure

```
pdf-chatbot/
│
├── app/
│   ├── services/
│   │   ├── rag.py
│   │   ├── llm.py
│   │   ├── prompt.py
│   │
│   ├── database.py
│   ├── app.py
│   ├── uploads/
|   ├── chroma_db/
|   ├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone repo

```bash
git clone https://github.com/your-username/pdf-chatbot.git
cd pdf-chatbot
```

---

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If no requirements file:

```bash
pip install fastapi uvicorn
pip install langchain langchain-community langchain-chroma langchain-huggingface
pip install chromadb sentence-transformers
pip install python-dotenv
```

---

### 4. Install Ollama

Download:
👉 https://ollama.com

Pull model:

```bash
ollama pull qwen2.5:3b
```

---

### 5. Run server

```bash
uvicorn app.app:app --reload
```

---

## 📌 API Endpoints

### 📤 Upload PDF

```
POST /upload
```

Upload a PDF file to index it into vector database.

---

### ❓ Ask question

```
POST /ask
```

Example request:

```json
{
  "question": "What is this document about?"
}
```

Example response:

```json
{
  "answer": "The document explains ...",
  "sources": [2, 5]
}
```

---

## 🧠 How it works (RAG Pipeline)

```
PDF → Chunking → Embeddings → ChromaDB
                                ↓
User Question → Similarity Search → Context
                                ↓
                        Ollama LLM Answer
```

---

## 📌 Notes

* This project runs fully locally (no OpenAI API required)
* Uses free models via Ollama
* Designed for learning and portfolio use
* Can be extended with streaming, memory, and frontend UI

---

## 🔥 Future Improvements

* [ ] Streaming responses (like ChatGPT typing effect)
* [ ] Chat memory (conversation history)
* [ ] React frontend UI
* [ ] Multi-PDF management
* [ ] Docker support
* [ ] Authentication system

---

## 👨‍💻 Author

Built as a learning project for RAG systems, LLM integration, and modern AI backend architecture.

---

## ⭐ If you like this project

Give it a star ⭐ and feel free to fork it!
