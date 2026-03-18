
# 🚀 AI Search Assistant (LangChain + Groq + Streamlit)

An intelligent AI-powered search assistant that can answer questions using:

* 🌐 Web Search
* 📚 Wikipedia
* 📄 ArXiv Research Papers

Built using **LangChain Tool-Calling Agents**, **Groq LLM**, and **Streamlit UI**.

---

## ✨ Features

* ⚡ Fast responses using Groq LLM
* 🧠 Smart tool usage (only when needed)
* 🔍 Multi-source search:

  * DuckDuckGo (Web)
  * Wikipedia
  * ArXiv
* 💬 Chat-based UI with memory
* 🚫 No ReAct parsing errors (uses tool-calling agent)
* 🎯 Clean and structured answers

---

## 🛠️ Tech Stack

* **Frontend:** Streamlit
* **LLM:** Groq (`llama-3.1-8b-instant`)
* **Framework:** LangChain
* **Tools:**

  * DuckDuckGo Search
  * Wikipedia API
  * ArXiv API

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/ai-search-assistant.git
cd ai-search-assistant
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file in root:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💡 How It Works

1. User enters a query
2. LLM decides:

   * Answer directly OR
   * Use a tool (Search / Wikipedia / ArXiv)
3. Tool fetches data
4. LLM generates final answer

---

## 🧠 Architecture

```
User Input
   ↓
Groq LLM (Tool Decision)
   ↓
Tool (if needed)
   ↓
Final Answer
   ↓
Streamlit UI
```

---

## ⚡ Optimization Features

* Limited tool usage (max 1 call)
* Smart prompt engineering
* Reduced latency by avoiding unnecessary tools

---

## 📸 Screenshot

*Add your project screenshot here*

---

## 🚀 Future Improvements

* 🔊 Voice assistant integration
* 📄 PDF / Document RAG system
* 💾 Chat memory with vector database
* 🌐 Multi-step reasoning agents
* ⚡ Caching for faster responses

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork and submit a PR.

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* LangChain
* Groq
* Streamlit

---

## 👨‍💻 Author

**Prathmesh Wavhal**
AI & Data Science Enthusiast 🚀

---

⭐ If you like this project, give it a star on GitHub!
