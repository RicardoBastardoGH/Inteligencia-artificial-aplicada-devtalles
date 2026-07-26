"""
JSON mode
"""
import json
from src.helpers.ai_client import call_ai
# from rich.console import Console
# from rich.panel import Panel
# from rich.markdown import Markdown
# from rich.syntax import Syntax
# from rich.rule import Rule

def run_json_mode():
    # print("Texto libre")
    # print("="*40)
    
    # response_text = call_ai([
    #     { "role": "user",
    #      "content": "Dame informacion sobre Python: año de creacion, creador y sus usos principales"}
    # ])
    
    # print(f"Respuesta: \n{response_text}")
    
    print("\nJSON Mode\n")
    print("="*40)
    
    response_json = call_ai([
        {
            "role": "system",
            "content": "responde siempre en formato JSON Valido"
        },
        {
            "user": "user",
            "content": """Dame informacion sobre Python en este formato exacto
            {
                "language": "nombre",
                "creation_year": numero,
                "creator": "nombre",
                "principal_uses": ["uso1", "uso2","uso3"]
            }
            """
        }
        ],
        0.1,
        "json_object"
    )
    
    json_data = json.loads(response_json)
    print("JSON: ", json_data)
    print(f"Año de creacion: {json_data['creation_year']}")
    print(f"Creador: {json_data['creator']}")
    
    
