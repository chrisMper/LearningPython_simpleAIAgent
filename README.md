# Simple AI Agent with LangGraph

A Python-based AI agent built using LangChain and LangGraph that can perform real-time calculations and chat via OpenRouter.

## 🎯 Intended Learning Outcomes (ILO)

By completing this project, you will have learned how to:
- **Build an AI Agent**: Use `langchain` and `langgraph` to create an autonomous agent.
- **Integrate Tools**: Create custom Python functions (like the `calculator`) and register them as tools for an AI to use.
- **Manage API Connections**: Securely connect to LLM providers using OpenRouter and environment variables.
- **Handle Streaming**: Implement real-time token streaming for a smoother "typing" effect in the terminal.
- **Modern Python Tooling**: Use `uv` for lightning-fast dependency management and virtual environments.
- **Security Best Practices**: Protect API keys using `.gitignore` and `.env` patterns.

## 🛠️ Setup & Installation

### 1. Initialize the project
This project uses `uv` for dependency management.
```bash
uv init .
```

### 2. Install Dependencies
```bash
uv add langgraph langchain python-dotenv langchain-openai langchain-core
```

### 3. Set up an API Key from OpenAI
1. Create a `.env` file in the root directory.
2. Add your OpenRouter API key:
   ```bash
   OPENAI_API_KEY=your_openrouter_key_here
   ```
*(A `.env.example` file is provided as a template.)*
3. Get the API key from openrouter.ai https://youtu.be/uCq40-sRrKE?si=IChR8y5msbUpAS8l

### 4. Writing code - main.py

4.1. Import
    ```python
    #langchain is a high level python library that allows us to create an AI agent
    from langchain_core.messages import HumanMessage
    #connect to openai and have the LLM running
    from langchain_openai import ChatOpenAI
    #to register the tool that our AI agent can use
    from langchain.tools import tool
    #langgraph is a complex library that allows us to create an AI agent
    from langchain.agents import create_agent
    #to load the API key from the .env file
    from dotenv import load_dotenv

    ```
4.2. Load the API key and initialize the OpenAI LLM
    ```python
    load_dotenv()
    ```

4.3. Initialize the LLM with OpenRouter (optional but recommended for OpenRouter keys)
    ```python
    model = ChatOpenAI(
        model="openai/gpt-4o-mini",
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
    agent_executor = create_agent(model, tools)
    ```

## 🚀 Running the Agent

To start the interactive agent, run:
```bash
uv run python main.py
```

### Features to try:
- **Direct Chat**: Just say "Hi" or ask "How are you?".
- **Math Operations**: Ask "What is 15 multiplied by 4?" or "Divide 100 by 5".
- **Streaming**: Watch the assistant's reply appear in real-time.
- **Exit**: Type `quit` to close the session.

## 🧮 How the Calculator Works
The agent uses a custom Python tool decorated with `@tool`. When you ask a math question, the AI identifies that the `calculator` tool is needed, extracts the numbers and the operation, and executes the local Python code to ensure 100% mathematical accuracy.

## 📝 Technical Notes
- **Provider**: OpenRouter.ai (GPT-4o-mini)
- **Framework**: LangChain Agents (moving towards LangGraph V2 standards)
- **Streaming**: Enabled via `stream_mode="messages"`
