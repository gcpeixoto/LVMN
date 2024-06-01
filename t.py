from rich.console import Console
from rich.table import Table

console = Console()

table = Table(title="Tabela de Exemplo")

table.add_column("Nome", style="cyan", no_wrap=True)
table.add_column("Idade", style="magenta")
table.add_column("País", style="green")

table.add_row("Alice", "24", "EUA")
table.add_row("Bob", "19", "Canadá")
table.add_row("Charlie", "22", "Reino Unido")

console.print(table)
