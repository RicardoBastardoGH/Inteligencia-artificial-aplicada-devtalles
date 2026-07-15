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
            "content": "Di hoa en 3 idiomas diferentes"
        }
    ]
)

print(response.choices[0].message.content)


# Uso de los tokends
print("\nUso de tokens:")
print(f"Tokens de entrada: {response.usage.prompt_tokens}")
print(f"Tokens de salida: {response.usage.completion_tokens}")
print(f"Tokens totales: {response.usage.total_tokens}")

cost_input = (response.usage.prompt_tokens / 1_000_000) * 0.0015  # Costo por millón de tokens de entrada
cost_output = (response.usage.completion_tokens / 1_000_000) * 0.60  # Costo por millón de tokens de salida
total_cost = cost_input + cost_output


print(f"\nCosto de entrada: ${cost_input:.6f} USD")
print(f"Costo de salida: ${cost_output:.6f} USD")
print(f"Costo total estimado: ${total_cost:.6f} USD")


print ("\n--- Información de la respuesta ---")
print(f"ID de la respuesta: {response.id}")
print(f"Modelo utilizado: {response.model}")