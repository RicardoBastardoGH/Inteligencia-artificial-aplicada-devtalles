import os
# from genai import Client
from google import genai
from dotenv import load_dotenv
from google import genai

# Cargamos tu archivo .env (buena práctica)
load_dotenv()

# Al inicializar Client() sin argumentos, busca automáticamente 
client = genai.Client()

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Di hola en 3 idiomas diferentes",
)

print(response.text)
print(response)

# print("\n--Uso de Tokens--")
# print(f"Tokens de entrada: {response.usage.input_tokens}")
# print(f"Tokens de salida: {response.usage.output_tokens}")
# print(f"Tokens totales: {response.usage.total_tokens}")


# # Costos
# cost_input = response.usage.input_tokens * 0.000001
# cost_output = response.usage.output_tokens * 0.000002
# total_cost = cost_input + cost_output

# print(f"\n--Costo estimado--")
# print(f"Coste de entrada: ${cost_input:.6f}")
# print(f"Coste de salida: ${cost_output:.6f}")
# print(f"Coste total: ${total_cost:.6f}")

# print(f"\nId de la respuesta: {response.id}")
# print(f"Modelo usado: {response.model}")
