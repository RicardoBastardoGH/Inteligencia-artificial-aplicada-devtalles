from rich.console import Console
from rich.panel import Panel

from src.prompts.function_calling import run_chat_with_tools
from src.prompts.json_mode import run_json_mode

console = Console()

def main():
    console.print(
        Panel.fit(
            "[bold cyan]Tecnicas de prompting\n"
        )
    )
    
    run_chat_with_tools(user_message="Que clima hace en Madrid?")
    run_chat_with_tools(user_message="Cual es la capital de España?")
    
    console.print("\n[bold green]Ejecucion completada\n")
    
if __name__ == "__main__":
    main()