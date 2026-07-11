import os
# from genai import Client
from google import genai
from dotenv import load_dotenv
from google import genai

# Cargamos tu archivo .env (buena práctica)
load_dotenv()

# Al inicializar Client() sin argumentos, busca automáticamente 
# una variable de entorno llamada GEMINI_API_KEY en tu .env
client = genai.Client()

# Imprime los modelos que tienes disponibles HOY
# print("--- MODELOS DISPONIBLES EN TU CUENTA ---")
# Listamos todos los modelos usando el nuevo SDK
# for model in client.models.list():
#     # Imprimimos el nombre del modelo y su acción/descripción asociada
#     print(f"Modelo: {model.name}")
#     # Si tiene supported_actions, las mostramos para saber qué hace
#     if hasattr(model, 'supported_actions'):
#         print(f"  Acciones: {model.supported_actions}")
#     print("-" * 40)

response = client.models.generate_content(
    model="gemini-3.1-flash-lite",
    contents="Explica que es una API en una oracion",
)

print(response.text)

