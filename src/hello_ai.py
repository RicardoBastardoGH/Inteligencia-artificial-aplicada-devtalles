from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI()

response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL"),
    messages=[
        {
            "role": "user",
            "content": "Explica que es una API en una oracion"
        }
    ]
)


text = response.choices[0].message.content
print(text)