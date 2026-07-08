<div align="center">



\# 🤖 NEXUS

\### \*A multi-agent AI system that knows which brain to call\*



\[!\[Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)

\[!\[Ollama](https://img.shields.io/badge/Local\_LLM-Ollama-000000?style=for-the-badge)](https://ollama.com/)

\[!\[Llama](https://img.shields.io/badge/Model-Llama\_3.2\_3B-FFD21E?style=for-the-badge)](https://ollama.com/library/llama3.2)

\[!\[Colorama](https://img.shields.io/badge/UI-Terminal-4D4D4D?style=for-the-badge)](https://pypi.org/project/colorama/)



</div>



\---



\## 🎯 The Problem



Most AI assistants are one brain trying to do everything — scheduling, emailing, task tracking, note-taking — with no real specialization. NEXUS takes a different approach: instead of one generalist, it's a team of specialists that automatically figures out who should handle each request.



\## ⚡ What It Does



NEXUS routes every user request through an AI-powered router that decides which of its four specialized agents should respond — then hands off the request and returns a focused, role-appropriate answer.



Type a request in plain English. NEXUS figures out whether it's a calendar task, an email draft, a to-do priority call, or a note to save — and responds accordingly.



\## 🧠 The Agents



| Agent | Role |

|---|---|

| 📅 \*\*Calendar Agent\*\* | Manages schedules, appointments, and reminders |

| ✉️ \*\*Email Agent\*\* | Drafts, organizes, and helps manage email communication |

| ✅ \*\*Task Agent\*\* | Coordinates to-do items, priorities, and deadlines |

| 🗒️ \*\*Notes Agent\*\* | Saves and retrieves notes — with real persistent storage |



\## 🛠️ How It's Built

User Input → AI Router (classifies intent) → Specialized Agent → Response

↓

Notes Agent → Persistent JSON storage



\*\*Routing:\*\* Instead of hardcoded keyword rules, NEXUS asks the LLM itself to classify each request and pick the right agent — genuine agent-to-agent coordination logic, not a simple if/else chain.



\*\*Persistence:\*\* Unlike a typical chatbot demo, the Notes Agent actually writes to disk. Notes survive across sessions and can be retrieved on demand.



\*\*Local inference:\*\* NEXUS runs entirely on Ollama with Llama 3.2 (3B) — no external API costs, no internet dependency once set up.



\## 🧰 Tech Stack



`Python` · `Ollama` · `Llama 3.2 (3B)` · `Colorama` · `Requests` · `JSON`



\## 📁 Repository Structure

├── main.py             # Entry point — terminal UI and main loop

├── router.py            # AI-based request classification and routing

├── agent.py             # Base Agent class shared by all 4 agents

├── agents\_setup.py       # Instantiates the 4 specialized agents

├── notes\_storage.py      # Persistent JSON-based note storage

├── test\_\*.py            # Individual test scripts for agents/router

└── requirements.txt



\## 🚀 Run It Yourself



```bash

\# 1. Install Ollama and pull the model

ollama pull llama3.2:3b



\# 2. Clone the repo

git clone https://github.com/AkshayEtukuri/nexus.git

cd nexus



\# 3. Install dependencies

pip install requests colorama



\# 4. Run NEXUS

python main.py

```



\## 🌐 Future Plans — NEXUS 2.0



\- 🔍 RAG pipeline for agents to reason over personal documents

\- 🧬 ChromaDB vector database for semantic memory

\- ⚡ FastAPI backend with a React.js frontend

\- 🌐 Real-time web search integration

\- 📡 Streaming responses, ChatGPT-style



\## 👤 Author



\*\*Akshay Etukuri\*\*

\[GitHub](https://github.com/AkshayEtukuri)



\---



<div align="center">

<i>Part of an ongoing portfolio applying AI system design to real-world assistant workflows.</i>

</div>

