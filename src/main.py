from rich.console import Console
from rich.panel import Panel

# from src.prompts.zero_few_shot import run_zero_few_shot
from src.prompts.chain_of_thoughts_prompts import run_chain_of_thought

console = Console()

def main():
    console.print(
        Panel.fit(
            "[bold cyan]Tecnicas de prompting\n"
        )
    )
    
    # run_zero_few_shot()
    run_chain_of_thought()
    
    console.print("\n[bold green]Ejecucion completada\n")
    
if __name__ == "__main__":
    main()