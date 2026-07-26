from rich.console import Console
from rich.panel import Panel

from src.prompts.json_mode import run_json_mode

console = Console()

def main():
    console.print(
        Panel.fit(
            "[bold cyan]Tecnicas de prompting\n"
        )
    )
    
    run_json_mode()
    
    console.print("\n[bold green]Ejecucion completada\n")
    
if __name__ == "__main__":
    main()