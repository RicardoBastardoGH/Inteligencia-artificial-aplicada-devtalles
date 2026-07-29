from openai import OpenAI, omit
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def call_ai(messages:list, temperature: float = 0.1, response_format:str="texto") -> str:
    """Funcion que ejecuta el cliente"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature,
        response_format={"type":response_format}
    )
    return response.choices[0].message.content

def call_ai_tools(messages:list, temperature: float = 0.1, response_format:str="texto", tools: list= omit, tool_choice: str= omit) -> str:
    """Funcion que ejecuta el cliente con tools"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=temperature,
        response_format={"type":response_format},
        tools=tools,
        tool_choice= tool_choice
    )
    return response.choices[0].message


