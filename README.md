# LearningPython_simpleAIAgent
The Agent has access to tools to do math Operations.

ILO : 

## Initialize the uv project
```
uv init .

```

## Install Dependencies
```
uv add langgraph langchain python-dotenv langchain-openai

```
## Set up an API Key from OpenAI

1. Create a .env file in the root directory of the project.
2. Add the following line to the .env file:
OPENAI_API_KEY=your_openai_api_key_here
3. Get the API key from openrouter.ai https://youtu.be/uCq40-sRrKE?si=IChR8y5msbUpAS8l

## Writing code - main.py

1. Import
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
2. Load the API key and initialize the OpenAI LLM
    ```python
    load_dotenv()
    ```

3. Initialize the LLM with OpenRouter (optional but recommended for OpenRouter keys)
    ```python
    model = ChatOpenAI(
        model="openai/gpt-4o-mini",
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
    agent_executor = create_agent(model, tools)
    ```
