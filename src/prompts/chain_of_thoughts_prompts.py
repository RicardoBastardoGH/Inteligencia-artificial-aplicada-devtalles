from rich.console import Console
from rich.panel import Panel
from rich.markdown import Markdown
from rich.rule import Rule

from src.helpers.ai_client import call_ai

console = Console()

def run_chain_of_thought():
    console.print(Rule("[bold yellow]Chain of Thought"))
    
    problem = """
    Una empresa tiene 3 servidores. Cada servidor maneja 1200 request/hora.
    Tiene picos de 4500 request/hora los lunes.
    Cuantos servidores adicionales se necesitan para los picos?
    """
    console.print(
        Panel(problem.strip(), title="Problema", border_style="blue")
    )
    
    without_cot = call_ai([
        {"role":"user", "content": f"Responde solo el numero: {problem}"}
    ])
    
    with_cot = call_ai([
            {"role":"user", "content": f"""
            {problem}
            
            Piensa paso a paso:
            1. Calcula la capacidad actual
            2. calcula el deficit en pico
            3. deetermina cuantos servidores adicionales se necesitan
            4. Da la respuesta final 
            """}
        ])
    
    console.print(
        Panel(Markdown(without_cot), title="Con CoT", border_style="green")
    )
    
