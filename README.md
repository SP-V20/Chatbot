[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-n7csjzkbpqfddqxfqlmqih.streamlit.app/)

# 🤖 AI Chatbot (Streamlit + Groq)

A simple conversational AI chatbot built using **Streamlit** and the **Groq API**.
It supports chat history, session-based memory, and an exit command to end conversations.

---

## 🚀 Live Demo
👉 [Click here to try the chatbot](https://chatbot-n7csjzkbpqfddqxfqlmqih.streamlit.app/)


## 🚀 Features

* 💬 Interactive chat UI using Streamlit
* 🧠 Maintains conversation history (context-aware responses)
* ⚡ Fast responses using Groq (`llama-3.3-70b-versatile`)
* 🚪 Exit command (`exit`, `quit`, `bye`) to end chat
* 🔄 Session-based state management
* 🧹 Auto-limits chat history to avoid token overflow

---

## 📂 Project Structure

```
.
├── main.py          # Main Streamlit app
├── .env             # Environment variables (API key)
├── requirements.txt # Dependencies
└── README.md        # Project documentation
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-chatbot.git
cd ai-chatbot
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Setup Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

---

## 🧠 How It Works

1. User enters a message in the chat input
2. Message is stored in `st.session_state.chat_history`
3. Full conversation (last 50 messages) is sent to the LLM
4. Groq API generates a response
5. Response is displayed and stored

---

## 🚪 Exit Command

Type any of the following to end the chat:

```
exit
quit
bye
```

* Stops further input
* Displays a goodbye message
* Disables chat interaction

---

## 🛠️ Tech Stack

* **Frontend/UI**: Streamlit
* **LLM API**: Groq
* **Model**: `llama-3.3-70b-versatile`
* **Environment Management**: python-dotenv

----

