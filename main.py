from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import create_agent
from dotenv import load_dotenv

load_dotenv()

@tool
def calculator(a: float, b: float, operation: str) -> str:
    # Specify the operation - a description of tool
    """Performs arithmetic operations. Valid operations are: add, subtract, multiply, divide."""
    print("Tool is being used")
    if operation == "add":
        return f"{a} + {b} = {a + b}"
    elif operation == "subtract":
        return f"{a} - {b} = {a - b}"
    elif operation == "multiply":
        return f"{a} * {b} = {a * b}"
    elif operation == "divide":
        return f"{a} / {b} = {a / b}"
    return "Invalid operation."

def main():
    # When using OpenRouter, you need to specify the base_url and a model name.
    model = ChatOpenAI(
        model="openai/gpt-4o-mini",
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    ) 

    tools = [calculator]

    agent_executor = create_agent(model, tools) # create the agent using the new recommended function

    print("Welcome! I'm yout AI agent. Type `quit` to exit.")
    print("You can ask me to perform calculations or chat with me")   
    
    while True: 
        user_input = input("\nYou: ").strip() 
        if user_input.lower() == "quit":
            break
        print("\nAssistant: ", end="")
        # stream the response of the LLM using `agent_executor`   
        for chunk, metadata in agent_executor.stream(
            {"messages": [HumanMessage(content=user_input)]},
            stream_mode="messages"
        ):    
            # Print the content of the message chunk as it arrives
            if chunk.content:
                print(chunk.content, end="", flush=True)

        print()

# A simple convention in python to run the main function when the file is run as a script
if __name__ == "__main__":
    main()






        