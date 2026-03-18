import streamlit as st
from langchain_groq import ChatGroq
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

# ---------------- TOOLS ---------------- #
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=250)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

wiki_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=250)
wikipedia = WikipediaQueryRun(api_wrapper=wiki_wrapper)

search = DuckDuckGoSearchRun(name="Search")

tools = [search, arxiv, wikipedia]

# ---------------- UI ---------------- #
st.title("AI Search Assistant")

st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your GROQ API KEY:", type="password")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi  Ask me anything!"}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# ---------------- CHAT ---------------- #
if prompt := st.chat_input("Ask anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(
        api_key=api_key,
        model="openai/gpt-oss-120b",
        temperature=0
    )

    #  TOOL CALLING PROMPT
    prompt_template = ChatPromptTemplate.from_messages([
            ("system", """You are a highly intelligent AI assistant.

        Your goals:
        - Provide accurate, clear, and concise answers.
        - Prefer answering directly using your knowledge.
        - Use tools ONLY when necessary.

        Tool usage rules:
        - Use at most ONE tool per question.
        - Do NOT call the same tool multiple times.
        - Do NOT use tools for simple or common knowledge questions.
        - Only use tools for:
        • Real-time information
        • Recent events
        • External data lookup (research papers, web info)

        Behavior rules:
        - If you already know the answer → respond immediately.
        - If you use a tool → summarize the result clearly.
        - Do NOT mention tools in the final answer.
        - Do NOT show internal reasoning.

        Answer style:
        - Be direct and structured.
        - Use bullet points when helpful.
        - Keep answers easy to understand.
        """),
            ("user", "{input}"),
            ("placeholder", "{agent_scratchpad}")
        ])

    #  TOOL CALLING AGENT
    agent = create_tool_calling_agent(llm, tools, prompt_template)

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=False   # no logs
    )

    with st.chat_message("assistant"):
        response = agent_executor.invoke({"input": prompt})

        output = response.get("output", " No response generated")

        st.session_state.messages.append({
            "role": "assistant",
            "content": output
        })

        st.write(output)