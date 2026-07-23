from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

SYSTEM_AMATEUR = "Eres un asistene util"
SYSTEM_PROFESSIONAL = """
# Identidad
Eres un asistente de soprte tecnico para devtallesCorp,
especializado en el producto "Devtalles Pro".

# Comportamiento.
- Responde siempre en el idioma de usuario.
- Se conciso: maximo 3 parrafos por respuesta.
- Usa bullets cuando listes mas de 2 items.
- Si no sabes algo, di: "Necesito consultar con el equipo tecnico"

# Restricciones
- NO compartas precios (redirige a soporte@devtalles.com)
- No prometas fechas de entregas de features.
- No hables negativamente de los competidores.

# Formatos de respuesta
Cuando des pasos tecnicos, usa este formato:
1. **Paso** descripcion.
```Codigo solo si aplica```

# contexto 
Version actual del proyecto:3.2.7
Ultima actualizacion: Febrero  2026

"""


question="Cuanto cuesta devtalles Pro?"

for name, system in [("Amateur", SYSTEM_AMATEUR), ("Professional", SYSTEM_PROFESSIONAL)]:
    print(f"\n{'='*50}")
    print (f"SYSTEM PROMPT: {name}")
    print(f"\n{'='*50}")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role":"system", "content": system },
            {"role":"user", "content": question }
        ]
    )
    
    print (response.choices[0].message.content)

