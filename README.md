<div align="center">

# 🤖 NEXUS
### *A multi-agent AI system that knows which brain to call*

[![Streamlit](https://img.shields.io/badge/🚀_Live_Demo-Streamlit-FF4B4B?style=for-the-badge)](https://readmemd-5tuak6cu6j5kkkbuf3eb36.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Groq](https://img.shields.io/badge/Cloud_LLM-Groq-F55036?style=for-the-badge)](https://groq.com/)
[![Llama](https://img.shields.io/badge/Model-Llama_3.1_8B-FFD21E?style=for-the-badge)](https://console.groq.com/docs/models)
[![Streamlit](https://img.shields.io/badge/UI-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)

</div>

---

## 🎯 The Problem

Most AI assistants are one brain trying to do everything — scheduling, emailing, task tracking, note-taking — with no real specialization. NEXUS takes a different approach: instead of one generalist, it's a team of specialists that automatically figures out who should handle each request.

## ⚡ What It Does

NEXUS routes every user request through an AI-powered router that decides which of its four specialized agents should respond — then hands off the request and returns a focused, role-appropriate answer.

Type a request in plain English. NEXUS figures out whether it's a calendar task, an email draft, a to-do priority call, or a note to save — and responds accordingly.

🔗 **Try it live:** [Streamlit Cloud →](https://readmemd-5tuak6cu6j5kkkbuf3eb36.streamlit.app/)

## 🧠 The Agents

| Agent | Role |
|---|---|
| 📅 **Calendar Agent** | Manages schedules, appointments, and reminders |
| ✉️ **Email Agent** | Drafts, organizes, and helps manage email communication |
| ✅ **Task Agent** | Coordinates to-do items, priorities, and deadlines |
| 🗒️ **Notes Agent** | Saves and retrieves notes — with real persistent storage |

## 🛠️ How It's Built
User Input → AI Router (classifies intent) → Specialized Agent → Response
↓
Notes Agent → Persistent JSON storage

**Routing:** Instead of hardcoded keyword rules, NEXUS asks the LLM itself to classify each request and pick the right agent — genuine agent-to-agent coordination logic, not a simple if/else chain.

**Persistence:** Unlike a typical chatbot demo, the Notes Agent actually writes to disk. Notes survive across sessions and can be retrieved on demand.

**Two interfaces:**
- A **terminal version** (`main.py`) with a colored CLI, originally built to run fully locally using Ollama with Llama 3.2 (3B) — no external API, no internet dependency.
- A **deployed web version** (`app.py`) built with Streamlit, using Groq's cloud API (Llama 3.1 8B) for inference so it can run as a live, publicly accessible demo.

## 🧰 Tech Stack

`Python` · `Groq API` · `Llama 3.1 (8B)` · `Streamlit` · `Ollama` (local mode) · `Colorama` · `Requests` · `JSON`

## 📁 Repository Structure
├── main.py               # Terminal entry point — CLI UI and main loop
├── app.py                # Streamlit entry point — web UI (deployed version)
├── router.py             # AI-based request classification and routing
├── agent.py              # Base Agent class shared by all 4 agents
├── agents_setup.py       # Instantiates the 4 specialized agents
├── notes_storage.py      # Persistent JSON-based note storage
├── test_*.py             # Individual test scripts for agents/router
└── requirements.txt

## 🚀 Run It Yourself

**Option 1 — Terminal version (local, free, using Ollama):**

```bash
# 1. Install Ollama and pull the model
ollama pull llama3.2:3b

# 2. Clone the repo
git clone https://github.com/AkshayEtukuri/NEXUS-Multi-Agent-AI.git
cd NEXUS-Multi-Agent-AI

# 3. Install dependencies
pip install requests colorama

# 4. Run NEXUS
python main.py
```

**Option 2 — Web version (using Groq API):**

```bash
# 1. Get a free API key from console.groq.com
# 2. Set it as an environment variable
set GROQ_API_KEY=your_key_here

# 3. Install dependencies
pip install groq streamlit

# 4. Run the app
streamlit run app.py
```

## 🌐 Future Plans — NEXUS 2.0

- 🔍 RAG pipeline for agents to reason over personal documents
- 🧬 ChromaDB vector database for semantic memory
- ⚡ FastAPI backend with a React.js frontend
- 🌐 Real-time web search integration
- 📡 Streaming responses, ChatGPT-style

## 👤 Author

**Akshay Etukuri**
[GitHub](https://github.com/AkshayEtukuri)

---

<div align="center">
<i>Part of an ongoing portfolio applying AI system design to real-world assistant workflows.</i>
</div>
